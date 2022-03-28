# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AdvanceSearch.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AdvanceSearch(object):
    def setupUi(self, AdvanceSearch):
        if not AdvanceSearch.objectName():
            AdvanceSearch.setObjectName(u"AdvanceSearch")
        AdvanceSearch.resize(828, 538)
        self.horizontalLayout = QHBoxLayout(AdvanceSearch)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter_h = QSplitter(AdvanceSearch)
        self.splitter_h.setObjectName(u"splitter_h")
        self.splitter_h.setOrientation(Qt.Horizontal)
        self.splitter_v = QSplitter(self.splitter_h)
        self.splitter_v.setObjectName(u"splitter_v")
        self.splitter_v.setOrientation(Qt.Vertical)
        self.widget = QWidget(self.splitter_v)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.code_input = QPlainTextEdit(self.widget)
        self.code_input.setObjectName(u"code_input")
        self.code_input.setMinimumSize(QSize(400, 150))
        self.code_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.code_input.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.verticalLayout.addWidget(self.code_input)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.splitter_v.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter_v)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.code_output = QPlainTextEdit(self.widget1)
        self.code_output.setObjectName(u"code_output")
        self.code_output.setMinimumSize(QSize(400, 150))
        self.code_output.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.code_output.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.verticalLayout_3.addWidget(self.code_output)

        self.splitter_v.addWidget(self.widget1)
        self.splitter_h.addWidget(self.splitter_v)
        self.widget2 = QWidget(self.splitter_h)
        self.widget2.setObjectName(u"widget2")
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.code_help = QPlainTextEdit(self.widget2)
        self.code_help.setObjectName(u"code_help")
        self.code_help.setMinimumSize(QSize(400, 500))
        self.code_help.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.code_help.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.code_help.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.code_help)

        self.splitter_h.addWidget(self.widget2)

        self.horizontalLayout.addWidget(self.splitter_h)


        self.retranslateUi(AdvanceSearch)

        QMetaObject.connectSlotsByName(AdvanceSearch)
    # setupUi

    def retranslateUi(self, AdvanceSearch):
        AdvanceSearch.setWindowTitle(QCoreApplication.translate("AdvanceSearch", u"Form", None))
        self.label.setText(QCoreApplication.translate("AdvanceSearch", u"Python Script:", None))
        self.pushButton.setText(QCoreApplication.translate("AdvanceSearch", u"Run", None))
        self.label_4.setText(QCoreApplication.translate("AdvanceSearch", u"Output:", None))
        self.label_2.setText(QCoreApplication.translate("AdvanceSearch", u"Accessing data with:", None))
    # retranslateUi

