# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelegramBotDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_telegramBotDialog(object):
    def setupUi(self, telegramBotDialog):
        telegramBotDialog.setObjectName("telegramBotDialog")
        telegramBotDialog.resize(550, 358)
        self.tipLabel = QtWidgets.QLabel(telegramBotDialog)
        self.tipLabel.setGeometry(QtCore.QRect(170, 20, 241, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.tipLabel.setFont(font)
        self.tipLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tipLabel.setObjectName("tipLabel")
        self.tokenLineEdit = QtWidgets.QLineEdit(telegramBotDialog)
        self.tokenLineEdit.setGeometry(QtCore.QRect(160, 60, 281, 21))
        self.tokenLineEdit.setToolTip("")
        self.tokenLineEdit.setClearButtonEnabled(False)
        self.tokenLineEdit.setObjectName("tokenLineEdit")
        self.telegramIDLineEdit = QtWidgets.QLineEdit(telegramBotDialog)
        self.telegramIDLineEdit.setGeometry(QtCore.QRect(160, 110, 281, 21))
        self.telegramIDLineEdit.setToolTip("")
        self.telegramIDLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.telegramIDLineEdit.setObjectName("telegramIDLineEdit")
        self.tokenLabel = QtWidgets.QLabel(telegramBotDialog)
        self.tokenLabel.setGeometry(QtCore.QRect(90, 54, 61, 31))
        self.tokenLabel.setObjectName("tokenLabel")
        self.telegramIDLabel = QtWidgets.QLabel(telegramBotDialog)
        self.telegramIDLabel.setGeometry(QtCore.QRect(93, 104, 61, 31))
        self.telegramIDLabel.setObjectName("telegramIDLabel")
        self.socksLabel = QtWidgets.QLabel(telegramBotDialog)
        self.socksLabel.setGeometry(QtCore.QRect(90, 154, 61, 31))
        self.socksLabel.setObjectName("socksLabel")
        self.okButton = QtWidgets.QPushButton(telegramBotDialog)
        self.okButton.setGeometry(QtCore.QRect(200, 300, 161, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.socksLineEdit = QtWidgets.QLineEdit(telegramBotDialog)
        self.socksLineEdit.setGeometry(QtCore.QRect(160, 160, 281, 21))
        self.socksLineEdit.setToolTip("")
        self.socksLineEdit.setObjectName("socksLineEdit")
        self.messageLabel = QtWidgets.QLabel(telegramBotDialog)
        self.messageLabel.setGeometry(QtCore.QRect(90, 220, 61, 31))
        self.messageLabel.setObjectName("messageLabel")
        self.messagePlainTextEdit = QtWidgets.QPlainTextEdit(telegramBotDialog)
        self.messagePlainTextEdit.setGeometry(QtCore.QRect(160, 200, 281, 81))
        self.messagePlainTextEdit.setObjectName("messagePlainTextEdit")

        self.retranslateUi(telegramBotDialog)
        QtCore.QMetaObject.connectSlotsByName(telegramBotDialog)

    def retranslateUi(self, telegramBotDialog):
        _translate = QtCore.QCoreApplication.translate
        telegramBotDialog.setWindowTitle(_translate("telegramBotDialog", "OpenCV Face Recognition System - TelegramBot"))
        self.tipLabel.setText(_translate("telegramBotDialog", "请谨慎修改以下内容"))
        self.tokenLineEdit.setPlaceholderText(_translate("telegramBotDialog", "请填写TelegramBot的API Token"))
        self.telegramIDLineEdit.setPlaceholderText(_translate("telegramBotDialog", "请填写接收方的Telegram ID"))
        self.tokenLabel.setText(_translate("telegramBotDialog", "API Token："))
        self.telegramIDLabel.setText(_translate("telegramBotDialog", "发送给谁："))
        self.socksLabel.setText(_translate("telegramBotDialog", "socks代理："))
        self.okButton.setText(_translate("telegramBotDialog", "更新配置"))
        self.socksLineEdit.setPlaceholderText(_translate("telegramBotDialog", "请填写proxy_url，留空则使用直连"))
        self.messageLabel.setText(_translate("telegramBotDialog", "发送内容："))
        self.messagePlainTextEdit.setPlaceholderText(_translate("telegramBotDialog", "请填写要发送的消息内容，仅支持纯文本"))
