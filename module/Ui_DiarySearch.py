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
from DTPySide.DTWidget import MarkdownViewer


class Ui_DiarySearch(object):
    def setupUi(self, DiarySearch):
        if not DiarySearch.objectName():
            DiarySearch.setObjectName(u"DiarySearch")
        DiarySearch.resize(600, 500)
        DiarySearch.setMinimumSize(QSize(600, 500))
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

        self.tabWidget = QTabWidget(DiarySearch)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tab_textlist = QWidget()
        self.tab_textlist.setObjectName(u"tab_textlist")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_textlist)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.textList = TextList(self.tab_textlist)
        self.textList.setObjectName(u"textList")

        self.horizontalLayout_5.addWidget(self.textList)

        self.tabWidget.addTab(self.tab_textlist, "")
        self.tab_textviewer = QWidget()
        self.tab_textviewer.setObjectName(u"tab_textviewer")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_textviewer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textViewer = MarkdownViewer(self.tab_textviewer)
        self.textViewer.setObjectName(u"textViewer")
        self.textViewer.setOpenExternalLinks(True)

        self.horizontalLayout_3.addWidget(self.textViewer)

        self.tabWidget.addTab(self.tab_textviewer, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(DiarySearch)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DiarySearch)
    # setupUi

    def retranslateUi(self, DiarySearch):
        DiarySearch.setWindowTitle(QCoreApplication.translate("DiarySearch", u"DiarySearch", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("DiarySearch", u"text text (2000.1.1) (2001.1.1-2001.2.1) [conceptA] [conceptB]", None))
        self.checkBox.setText(QCoreApplication.translate("DiarySearch", u"Rank", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_textlist), QCoreApplication.translate("DiarySearch", u"Text List", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_textviewer), QCoreApplication.translate("DiarySearch", u"Text Viewer", None))
    # retranslateUi

