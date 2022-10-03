# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_BookmarkParser.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widget import FileTab


class Ui_BookmarkParser(object):
    def setupUi(self, BookmarkParser):
        if not BookmarkParser.objectName():
            BookmarkParser.setObjectName(u"BookmarkParser")
        BookmarkParser.resize(1000, 600)
        BookmarkParser.setMinimumSize(QSize(1000, 600))
        self.verticalLayout_3 = QVBoxLayout(BookmarkParser)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_open = QPushButton(BookmarkParser)
        self.pushButton_open.setObjectName(u"pushButton_open")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open.sizePolicy().hasHeightForWidth())
        self.pushButton_open.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.pushButton_open)

        self.splitter = QSplitter(BookmarkParser)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label)

        self.folderList = QListWidget(self.layoutWidget)
        self.folderList.setObjectName(u"folderList")

        self.verticalLayout.addWidget(self.folderList)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.bookmarkTab = FileTab(self.layoutWidget1)
        self.bookmarkTab.setObjectName(u"bookmarkTab")

        self.verticalLayout_2.addWidget(self.bookmarkTab)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_3.addWidget(self.splitter)


        self.retranslateUi(BookmarkParser)

        QMetaObject.connectSlotsByName(BookmarkParser)
    # setupUi

    def retranslateUi(self, BookmarkParser):
        BookmarkParser.setWindowTitle(QCoreApplication.translate("BookmarkParser", u"BookmarkParser", None))
        self.pushButton_open.setText(QCoreApplication.translate("BookmarkParser", u" Open ", None))
        self.label.setText(QCoreApplication.translate("BookmarkParser", u"Folder", None))
        self.label_2.setText(QCoreApplication.translate("BookmarkParser", u"Boomark", None))
    # retranslateUi

