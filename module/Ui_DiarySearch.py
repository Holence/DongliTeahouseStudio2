# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DiarySearch.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widget import TextList


class Ui_DiarySearch(object):
    def setupUi(self, DiarySearch):
        if not DiarySearch.objectName():
            DiarySearch.setObjectName(u"DiarySearch")
        DiarySearch.resize(485, 566)
        self.verticalLayout = QVBoxLayout(DiarySearch)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(DiarySearch)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.checkBox = QCheckBox(DiarySearch)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidget = TextList(DiarySearch)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.retranslateUi(DiarySearch)

        QMetaObject.connectSlotsByName(DiarySearch)
    # setupUi

    def retranslateUi(self, DiarySearch):
        DiarySearch.setWindowTitle(QCoreApplication.translate("DiarySearch", u"DiarySearch", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("DiarySearch", u"text text (2000.1.1) (2001.1.1-2001.2.1) [conceptA] [conceptB]", None))
        self.checkBox.setText(QCoreApplication.translate("DiarySearch", u"Rank", None))
    # retranslateUi

