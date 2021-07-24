# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Setting.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(400, 300)
        self.page_diary = QWidget()
        self.page_diary.setObjectName(u"page_diary")
        self.gridLayout = QGridLayout(self.page_diary)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        Setting.addWidget(self.page_diary)
        self.page_concept = QWidget()
        self.page_concept.setObjectName(u"page_concept")
        self.gridLayout_2 = QGridLayout(self.page_concept)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        Setting.addWidget(self.page_concept)
        self.page_library = QWidget()
        self.page_library.setObjectName(u"page_library")
        self.gridLayout_3 = QGridLayout(self.page_library)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_library_base = QLabel(self.page_library)
        self.label_library_base.setObjectName(u"label_library_base")

        self.gridLayout_3.addWidget(self.label_library_base, 0, 0, 1, 1)

        self.pushButton_library_base = QPushButton(self.page_library)
        self.pushButton_library_base.setObjectName(u"pushButton_library_base")

        self.gridLayout_3.addWidget(self.pushButton_library_base, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.lineEdit_library_base = QLineEdit(self.page_library)
        self.lineEdit_library_base.setObjectName(u"lineEdit_library_base")
        self.lineEdit_library_base.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_library_base, 1, 0, 1, 1)

        Setting.addWidget(self.page_library)

        self.retranslateUi(Setting)

        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"Setting", None))
        self.label_library_base.setText(QCoreApplication.translate("Setting", u"Library Base", None))
        self.pushButton_library_base.setText(QCoreApplication.translate("Setting", u"Open", None))
    # retranslateUi

