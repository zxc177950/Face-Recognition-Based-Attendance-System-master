# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateClass.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateClass(object):
    def setupUi(self, CreateClass):
        CreateClass.setObjectName("CreateClass")
        CreateClass.resize(1505, 793)
        self.DelpushButton = QtWidgets.QPushButton(CreateClass)
        self.DelpushButton.setGeometry(QtCore.QRect(680, 370, 121, 51))
        self.DelpushButton.setObjectName("DelpushButton")
        self.AllStuTable = QtWidgets.QTableWidget(CreateClass)
        self.AllStuTable.setGeometry(QtCore.QRect(10, 20, 631, 751))
        self.AllStuTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.AllStuTable.setObjectName("AllStuTable")
        self.AllStuTable.setColumnCount(5)
        self.AllStuTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.AllStuTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.AllStuTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.AllStuTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.AllStuTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.AllStuTable.setHorizontalHeaderItem(4, item)
        self.AllStuTable.horizontalHeader().setCascadingSectionResizes(False)
        self.AllStuTable.horizontalHeader().setStretchLastSection(False)
        self.AllStuTable.verticalHeader().setCascadingSectionResizes(True)
        self.AddStuTable = QtWidgets.QTableWidget(CreateClass)
        self.AddStuTable.setGeometry(QtCore.QRect(840, 20, 631, 751))
        self.AddStuTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.AddStuTable.setObjectName("AddStuTable")
        self.AddStuTable.setColumnCount(5)
        self.AddStuTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.AddStuTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.AddStuTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.AddStuTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.AddStuTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.AddStuTable.setHorizontalHeaderItem(4, item)
        self.AddStuTable.horizontalHeader().setCascadingSectionResizes(False)
        self.AddStuTable.horizontalHeader().setStretchLastSection(False)
        self.AddStuTable.verticalHeader().setCascadingSectionResizes(True)
        self.AddpushButton = QtWidgets.QPushButton(CreateClass)
        self.AddpushButton.setGeometry(QtCore.QRect(680, 290, 121, 51))
        self.AddpushButton.setObjectName("AddpushButton")
        self.CreatepushButton = QtWidgets.QPushButton(CreateClass)
        self.CreatepushButton.setGeometry(QtCore.QRect(680, 700, 121, 61))
        self.CreatepushButton.setObjectName("CreatepushButton")
        self.ClassNameLineEdit = QtWidgets.QLineEdit(CreateClass)
        self.ClassNameLineEdit.setGeometry(QtCore.QRect(650, 630, 181, 41))
        self.ClassNameLineEdit.setToolTip("")
        self.ClassNameLineEdit.setClearButtonEnabled(True)
        self.ClassNameLineEdit.setObjectName("ClassNameLineEdit")

        self.retranslateUi(CreateClass)
        QtCore.QMetaObject.connectSlotsByName(CreateClass)

    def retranslateUi(self, CreateClass):
        _translate = QtCore.QCoreApplication.translate
        CreateClass.setWindowTitle(_translate("CreateClass", "创建班级"))
        self.DelpushButton.setText(_translate("CreateClass", "←删除学生"))
        self.AllStuTable.setSortingEnabled(True)
        item = self.AllStuTable.horizontalHeaderItem(0)
        item.setText(_translate("CreateClass", "学号"))
        item = self.AllStuTable.horizontalHeaderItem(1)
        item.setText(_translate("CreateClass", "姓名"))
        item = self.AllStuTable.horizontalHeaderItem(2)
        item.setText(_translate("CreateClass", "专业"))
        item = self.AllStuTable.horizontalHeaderItem(3)
        item.setText(_translate("CreateClass", "年级"))
        item = self.AllStuTable.horizontalHeaderItem(4)
        item.setText(_translate("CreateClass", "班级"))
        self.AddStuTable.setSortingEnabled(True)
        item = self.AddStuTable.horizontalHeaderItem(0)
        item.setText(_translate("CreateClass", "学号"))
        item = self.AddStuTable.horizontalHeaderItem(1)
        item.setText(_translate("CreateClass", "姓名"))
        item = self.AddStuTable.horizontalHeaderItem(2)
        item.setText(_translate("CreateClass", "专业"))
        item = self.AddStuTable.horizontalHeaderItem(3)
        item.setText(_translate("CreateClass", "年级"))
        item = self.AddStuTable.horizontalHeaderItem(4)
        item.setText(_translate("CreateClass", "班级"))
        self.AddpushButton.setText(_translate("CreateClass", "增加学生→"))
        self.CreatepushButton.setText(_translate("CreateClass", "创建签到表"))
        self.ClassNameLineEdit.setPlaceholderText(_translate("CreateClass", "请输入课程名称"))
