# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_excel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_export_excel(object):
    def setupUi(self, export_excel):
        export_excel.setObjectName("export_excel")
        export_excel.resize(1104, 823)
        self.gridLayout_2 = QtWidgets.QGridLayout(export_excel)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(export_excel)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_sqlTable = QtWidgets.QTableWidget(self.groupBox)
        self.show_sqlTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.show_sqlTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.show_sqlTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.show_sqlTable.setObjectName("show_sqlTable")
        self.show_sqlTable.setColumnCount(1)
        self.show_sqlTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.show_sqlTable.setHorizontalHeaderItem(0, item)
        self.show_sqlTable.horizontalHeader().setCascadingSectionResizes(False)
        self.show_sqlTable.horizontalHeader().setStretchLastSection(False)
        self.show_sqlTable.verticalHeader().setCascadingSectionResizes(True)
        self.verticalLayout.addWidget(self.show_sqlTable)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select_table_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.select_table_pushButton.setObjectName("select_table_pushButton")
        self.horizontalLayout.addWidget(self.select_table_pushButton)
        self.DelpushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.DelpushButton.setEnabled(False)
        self.DelpushButton.setObjectName("DelpushButton")
        self.horizontalLayout.addWidget(self.DelpushButton)
        self.export_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.export_pushButton.setEnabled(False)
        self.export_pushButton.setObjectName("export_pushButton")
        self.horizontalLayout.addWidget(self.export_pushButton)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.StuCheckTable = QtWidgets.QTableWidget(self.groupBox_2)
        self.StuCheckTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.StuCheckTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.StuCheckTable.setObjectName("StuCheckTable")
        self.StuCheckTable.setColumnCount(4)
        self.StuCheckTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.StuCheckTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.StuCheckTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.StuCheckTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.StuCheckTable.setHorizontalHeaderItem(3, item)
        self.StuCheckTable.horizontalHeader().setCascadingSectionResizes(False)
        self.StuCheckTable.horizontalHeader().setStretchLastSection(False)
        self.StuCheckTable.verticalHeader().setCascadingSectionResizes(True)
        self.verticalLayout_2.addWidget(self.StuCheckTable)
        self.attendance_label = QtWidgets.QLabel(self.groupBox_2)
        self.attendance_label.setText("")
        self.attendance_label.setObjectName("attendance_label")
        self.verticalLayout_2.addWidget(self.attendance_label)
        self.horizontalLayout_2.addWidget(self.splitter)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.retranslateUi(export_excel)
        QtCore.QMetaObject.connectSlotsByName(export_excel)

    def retranslateUi(self, export_excel):
        _translate = QtCore.QCoreApplication.translate
        export_excel.setWindowTitle(_translate("export_excel", "导出签到表"))
        self.groupBox_3.setTitle(_translate("export_excel", "签到表管理"))
        self.groupBox.setTitle(_translate("export_excel", "表格选择"))
        self.show_sqlTable.setSortingEnabled(True)
        item = self.show_sqlTable.horizontalHeaderItem(0)
        item.setText(_translate("export_excel", "签到表"))
        self.groupBox_4.setTitle(_translate("export_excel", "表格操作"))
        self.select_table_pushButton.setText(_translate("export_excel", "选择"))
        self.DelpushButton.setText(_translate("export_excel", "删除"))
        self.export_pushButton.setText(_translate("export_excel", "导出"))
        self.groupBox_2.setTitle(_translate("export_excel", "表格预览"))
        self.StuCheckTable.setSortingEnabled(True)
        item = self.StuCheckTable.horizontalHeaderItem(0)
        item.setText(_translate("export_excel", "学号"))
        item = self.StuCheckTable.horizontalHeaderItem(1)
        item.setText(_translate("export_excel", "姓名"))
        item = self.StuCheckTable.horizontalHeaderItem(2)
        item.setText(_translate("export_excel", "是否出勤"))
        item = self.StuCheckTable.horizontalHeaderItem(3)
        item.setText(_translate("export_excel", "签到时间"))
