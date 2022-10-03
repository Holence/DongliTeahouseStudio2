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

from DTPySide.DTWidget.DTApplyButton import DTApplyButton


class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(486, 396)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_library_base = QLabel(self.page)
        self.label_library_base.setObjectName(u"label_library_base")

        self.gridLayout_3.addWidget(self.label_library_base, 0, 0, 1, 1)

        self.pushButton_library_base = DTApplyButton(self.page)
        self.pushButton_library_base.setObjectName(u"pushButton_library_base")

        self.gridLayout_3.addWidget(self.pushButton_library_base, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.lineEdit_library_base = QLineEdit(self.page)
        self.lineEdit_library_base.setObjectName(u"lineEdit_library_base")
        self.lineEdit_library_base.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_library_base, 1, 0, 1, 1)

        Setting.addWidget(self.page)

        self.retranslateUi(Setting)

        Setting.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"Setting", None))
        self.label_library_base.setText(QCoreApplication.translate("Setting", u"Library Base", None))
        self.pushButton_library_base.setText("")
    # retranslateUi

