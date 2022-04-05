# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Library.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widget import FileTab
from widget import ConceptTable
from widget import TextList
from DTPySide.DTWidget import MarkdownViewer

import DTPySide.DT_rc

class Ui_Library(object):
    def setupUi(self, Library):
        if not Library.objectName():
            Library.setObjectName(u"Library")
        Library.resize(892, 650)
        Library.setMinimumSize(QSize(0, 650))
        self.actionDelete = QAction(Library)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionSearch_File = QAction(Library)
        self.actionSearch_File.setObjectName(u"actionSearch_File")
        self.horizontalLayout_3 = QHBoxLayout(Library)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.splitter = QSplitter(Library)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit_search = QLineEdit(self.layoutWidget)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setMinimumSize(QSize(465, 0))

        self.verticalLayout.addWidget(self.lineEdit_search)

        self.fileTab = FileTab(self.layoutWidget)
        self.fileTab.setObjectName(u"fileTab")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileTab.sizePolicy().hasHeightForWidth())
        self.fileTab.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.fileTab)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_date = QLabel(self.layoutWidget2)
        self.label_date.setObjectName(u"label_date")

        self.verticalLayout_2.addWidget(self.label_date)

        self.dateEdit = QDateEdit(self.layoutWidget2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.dateEdit)

        self.label_name = QLabel(self.layoutWidget2)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout_2.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.layoutWidget2)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.verticalLayout_2.addWidget(self.lineEdit_name)

        self.tabWidget = QTabWidget(self.layoutWidget2)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(300, 0))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tab_concept = QWidget()
        self.tab_concept.setObjectName(u"tab_concept")
        self.horizontalLayout = QHBoxLayout(self.tab_concept)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.conceptTable = ConceptTable(self.tab_concept)
        self.conceptTable.setObjectName(u"conceptTable")
        sizePolicy1.setHeightForWidth(self.conceptTable.sizePolicy().hasHeightForWidth())
        self.conceptTable.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.conceptTable)

        self.tabWidget.addTab(self.tab_concept, "")
        self.tab_textlist = QWidget()
        self.tab_textlist.setObjectName(u"tab_textlist")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_textlist)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.textList = TextList(self.tab_textlist)
        self.textList.setObjectName(u"textList")

        self.horizontalLayout_4.addWidget(self.textList)

        self.tabWidget.addTab(self.tab_textlist, "")
        self.tab_textviewer = QWidget()
        self.tab_textviewer.setObjectName(u"tab_textviewer")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_textviewer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textViewer = MarkdownViewer(self.tab_textviewer)
        self.textViewer.setObjectName(u"textViewer")
        self.textViewer.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.textViewer)

        self.tabWidget.addTab(self.tab_textviewer, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.splitter.addWidget(self.layoutWidget2)

        self.horizontalLayout_3.addWidget(self.splitter)


        self.retranslateUi(Library)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Library)
    # setupUi

    def retranslateUi(self, Library):
        Library.setWindowTitle(QCoreApplication.translate("Library", u"Library", None))
        self.actionDelete.setText(QCoreApplication.translate("Library", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.actionDelete.setShortcut(QCoreApplication.translate("Library", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionSearch_File.setText(QCoreApplication.translate("Library", u"Search File", None))
#if QT_CONFIG(shortcut)
        self.actionSearch_File.setShortcut(QCoreApplication.translate("Library", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("Library", u"Search", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("Library", u"file name (2000.1.1) (2001.1.1-2001.2.1) [conceptA] [conceptB] {1}", None))
        self.label_date.setText(QCoreApplication.translate("Library", u"Date", None))
        self.label_name.setText(QCoreApplication.translate("Library", u"Name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_concept), QCoreApplication.translate("Library", u"Concept", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_textlist), QCoreApplication.translate("Library", u"Text List ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_textviewer), QCoreApplication.translate("Library", u"Text Viewer", None))
    # retranslateUi

