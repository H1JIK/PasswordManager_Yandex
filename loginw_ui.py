# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_w.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_w(object):
    def setupUi(self, login_w):
        login_w.setObjectName("login_w")
        login_w.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(login_w)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 150, 320, 109))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.view_user = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.view_user.setObjectName("view_user")
        self.verticalLayout.addWidget(self.view_user)
        self.okb_user = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.okb_user.setObjectName("okb_user")
        self.verticalLayout.addWidget(self.okb_user)
        self.add_user = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_user.setObjectName("add_user")
        self.verticalLayout.addWidget(self.add_user)
        self.delete_user_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_user_button.setObjectName("delete_user_button")
        self.verticalLayout.addWidget(self.delete_user_button)
        self.label = QtWidgets.QLabel(login_w)
        self.label.setGeometry(QtCore.QRect(60, 90, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login_w)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.error_login = QtWidgets.QLabel(login_w)
        self.error_login.setGeometry(QtCore.QRect(40, 260, 321, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.error_login.setFont(font)
        self.error_login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.error_login.setAutoFillBackground(False)
        self.error_login.setText("")
        self.error_login.setAlignment(QtCore.Qt.AlignCenter)
        self.error_login.setObjectName("error_login")

        self.retranslateUi(login_w)
        QtCore.QMetaObject.connectSlotsByName(login_w)

    def retranslateUi(self, login_w):
        _translate = QtCore.QCoreApplication.translate
        login_w.setWindowTitle(_translate("login_w", "Password Manager - Вход"))
        self.okb_user.setText(_translate("login_w", "Войти"))
        self.add_user.setText(_translate("login_w", "Добавить нового пользователя"))
        self.delete_user_button.setText(_translate("login_w", "Удалить выбранного пользователя"))
        self.label.setText(_translate("login_w", "Выберите пользователя"))
        self.label_2.setText(_translate("login_w", "Password Manager🔒"))
