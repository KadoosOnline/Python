# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler
##
## WARNING! All changes made in this file will be lost when recompiling the
##          UI file. Never edit this file by hand -- edit window.ui in Qt
##          Designer and run `pyside6-uic window.ui -o ui_window.py` again.
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QListWidget,
                               QPushButton, QVBoxLayout)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(440, 320)
        self.mainLayout = QVBoxLayout(Form)
        self.mainLayout.setObjectName(u"mainLayout")
        self.inputLayout = QHBoxLayout()
        self.inputLayout.setObjectName(u"inputLayout")
        self.editTask = QLineEdit(Form)
        self.editTask.setObjectName(u"editTask")

        self.inputLayout.addWidget(self.editTask)

        self.btnAdd = QPushButton(Form)
        self.btnAdd.setObjectName(u"btnAdd")

        self.inputLayout.addWidget(self.btnAdd)

        self.mainLayout.addLayout(self.inputLayout)

        self.listTasks = QListWidget(Form)
        self.listTasks.setObjectName(u"listTasks")

        self.mainLayout.addWidget(self.listTasks)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.btnRemove = QPushButton(Form)
        self.btnRemove.setObjectName(u"btnRemove")

        self.buttonsLayout.addWidget(self.btnRemove)

        self.btnClear = QPushButton(Form)
        self.btnClear.setObjectName(u"btnClear")

        self.buttonsLayout.addWidget(self.btnClear)

        self.mainLayout.addLayout(self.buttonsLayout)

        self.labelCount = QLabel(Form)
        self.labelCount.setObjectName(u"labelCount")
        self.labelCount.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout.addWidget(self.labelCount)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate("Form", u"Kadoos - to-do list", None))
        self.editTask.setPlaceholderText(
            QCoreApplication.translate("Form", u"what has to be done?", None))
        self.btnAdd.setText(QCoreApplication.translate("Form", u"Add", None))
        self.btnRemove.setText(
            QCoreApplication.translate("Form", u"Remove the selected task",
                                       None))
        self.btnClear.setText(
            QCoreApplication.translate("Form", u"Remove all", None))
        self.labelCount.setText(
            QCoreApplication.translate("Form", u"0 tasks", None))
    # retranslateUi
