# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoUI_Form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(675, 129)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.NewButton = QtWidgets.QPushButton(Form)
        self.NewButton.setObjectName("NewButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.NewButton)
        self.NewObject = QtWidgets.QLabel(Form)
        self.NewObject.setObjectName("NewObject")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.NewObject)
        self.GoButton = QtWidgets.QPushButton(Form)
        self.GoButton.setObjectName("GoButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.GoButton)
        self.GoObject = QtWidgets.QLabel(Form)
        self.GoObject.setObjectName("GoObject")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.GoObject)
        self.PreviousButton = QtWidgets.QPushButton(Form)
        self.PreviousButton.setObjectName("PreviousButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.PreviousButton)
        self.PreviousObject = QtWidgets.QLabel(Form)
        self.PreviousObject.setObjectName("PreviousObject")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.PreviousObject)
        self.Output = QtWidgets.QTextBrowser(Form)
        self.Output.setObjectName("Output")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.Output)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.NewButton, self.GoButton)
        Form.setTabOrder(self.GoButton, self.PreviousButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.NewButton.setText(_translate("Form", "New"))
        self.NewObject.setText(_translate("Form", "New File"))
        self.GoButton.setText(_translate("Form", "Go"))
        self.GoObject.setText(_translate("Form", "Go File"))
        self.PreviousButton.setText(_translate("Form", "Previous"))
        self.PreviousObject.setText(_translate("Form", "Previous File"))
