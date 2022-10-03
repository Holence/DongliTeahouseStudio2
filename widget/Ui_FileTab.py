# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_FileTab.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widget import FileTable
from widget import FileList

import DTPySide.DT_rc

class Ui_FileTab(object):
    def setupUi(self, FileTab):
        if not FileTab.objectName():
            FileTab.setObjectName(u"FileTab")
        FileTab.resize(789, 679)
        self.verticalLayout = QVBoxLayout(FileTab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(FileTab)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_2 = QHBoxLayout(self.page)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fileTable = FileTable(self.page)
        self.fileTable.setObjectName(u"fileTable")

        self.horizontalLayout_2.addWidget(self.fileTable)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_3 = QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fileList = FileList(self.page_2)
        self.fileList.setObjectName(u"fileList")

        self.horizontalLayout_3.addWidget(self.fileList)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_count = QLabel(FileTab)
        self.label_count.setObjectName(u"label_count")

        self.horizontalLayout.addWidget(self.label_count)

        self.label_info = QLabel(FileTab)
        self.label_info.setObjectName(u"label_info")

        self.horizontalLayout.addWidget(self.label_info)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_table = QPushButton(FileTab)
        self.pushButton_table.setObjectName(u"pushButton_table")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_table.sizePolicy().hasHeightForWidth())
        self.pushButton_table.setSizePolicy(sizePolicy)
        self.pushButton_table.setMinimumSize(QSize(24, 24))
        self.pushButton_table.setMaximumSize(QSize(24, 24))
        self.pushButton_table.setIconSize(QSize(16, 16))
        self.pushButton_table.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_table)

        self.pushButton_list = QPushButton(FileTab)
        self.pushButton_list.setObjectName(u"pushButton_list")
        sizePolicy.setHeightForWidth(self.pushButton_list.sizePolicy().hasHeightForWidth())
        self.pushButton_list.setSizePolicy(sizePolicy)
        self.pushButton_list.setMinimumSize(QSize(24, 24))
        self.pushButton_list.setMaximumSize(QSize(24, 24))
        self.pushButton_list.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_list)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(FileTab)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FileTab)
    # setupUi

    def retranslateUi(self, FileTab):
        FileTab.setWindowTitle(QCoreApplication.translate("FileTab", u"FileTab", None))
        self.label_count.setText("")
        self.label_info.setText("")
        self.pushButton_table.setText("")
        self.pushButton_list.setText("")
    # retranslateUi

