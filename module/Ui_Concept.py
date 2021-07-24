# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Concept.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widget import ConceptTable
from widget import FileTable
from DTPySide.DTWidget import DTPlainTextEdit
from widget import TextList
from widget import ConceptTree

import DTPySide.DT_rc

class Ui_Concept(object):
    def setupUi(self, Concept):
        if not Concept.objectName():
            Concept.setObjectName(u"Concept")
        Concept.resize(884, 585)
        self.actionAdd_Concept = QAction(Concept)
        self.actionAdd_Concept.setObjectName(u"actionAdd_Concept")
        icon = QIcon()
        icon.addFile(u":/icon/white/white_plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdd_Concept.setIcon(icon)
        self.actionDelete = QAction(Concept)
        self.actionDelete.setObjectName(u"actionDelete")
        icon1 = QIcon()
        icon1.addFile(u":/icon/white/white_trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete.setIcon(icon1)
        self.horizontalLayout_3 = QHBoxLayout(Concept)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.splitter_whole = QSplitter(Concept)
        self.splitter_whole.setObjectName(u"splitter_whole")
        self.splitter_whole.setOrientation(Qt.Horizontal)
        self.layoutWidget4 = QWidget(self.splitter_whole)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutSearch = QVBoxLayout(self.layoutWidget4)
        self.layoutSearch.setObjectName(u"layoutSearch")
        self.layoutSearch.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget4)
        self.label.setObjectName(u"label")

        self.layoutSearch.addWidget(self.label)

        self.lineEdit_search = QLineEdit(self.layoutWidget4)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setMinimumSize(QSize(200, 0))

        self.layoutSearch.addWidget(self.lineEdit_search)

        self.conceptTable = ConceptTable(self.layoutWidget4)
        self.conceptTable.setObjectName(u"conceptTable")
        self.conceptTable.setMinimumSize(QSize(200, 0))

        self.layoutSearch.addWidget(self.conceptTable)

        self.splitter_whole.addWidget(self.layoutWidget4)
        self.splitter_center = QSplitter(self.splitter_whole)
        self.splitter_center.setObjectName(u"splitter_center")
        self.splitter_center.setOrientation(Qt.Vertical)
        self.layoutWidget0 = QWidget(self.splitter_center)
        self.layoutWidget0.setObjectName(u"layoutWidget0")
        self.verticalLayout_info = QVBoxLayout(self.layoutWidget0)
        self.verticalLayout_info.setObjectName(u"verticalLayout_info")
        self.verticalLayout_info.setContentsMargins(0, 0, 0, 0)
        self.label_name = QLabel(self.layoutWidget0)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout_info.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.layoutWidget0)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(350, 0))

        self.verticalLayout_info.addWidget(self.lineEdit_name)

        self.label_detail = QLabel(self.layoutWidget0)
        self.label_detail.setObjectName(u"label_detail")

        self.verticalLayout_info.addWidget(self.label_detail)

        self.plainTextEdit_detail = DTPlainTextEdit(self.layoutWidget0)
        self.plainTextEdit_detail.setObjectName(u"plainTextEdit_detail")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_detail.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_detail.setSizePolicy(sizePolicy)
        self.plainTextEdit_detail.setMinimumSize(QSize(350, 0))

        self.verticalLayout_info.addWidget(self.plainTextEdit_detail)

        self.splitter_center.addWidget(self.layoutWidget0)
        self.layoutWidget9 = QWidget(self.splitter_center)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.verticalLayout_tab = QVBoxLayout(self.layoutWidget9)
        self.verticalLayout_tab.setObjectName(u"verticalLayout_tab")
        self.verticalLayout_tab.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.layoutWidget9)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setTristate(True)

        self.verticalLayout_tab.addWidget(self.checkBox)

        self.tabWidget = QTabWidget(self.layoutWidget9)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tab_file = QWidget()
        self.tab_file.setObjectName(u"tab_file")
        self.horizontalLayout = QHBoxLayout(self.tab_file)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fileTable = FileTable(self.tab_file)
        self.fileTable.setObjectName(u"fileTable")

        self.horizontalLayout.addWidget(self.fileTable)

        self.tabWidget.addTab(self.tab_file, "")
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
        self.textViewer = QTextBrowser(self.tab_textviewer)
        self.textViewer.setObjectName(u"textViewer")

        self.horizontalLayout_2.addWidget(self.textViewer)

        self.tabWidget.addTab(self.tab_textviewer, "")

        self.verticalLayout_tab.addWidget(self.tabWidget)

        self.splitter_center.addWidget(self.layoutWidget9)
        self.splitter_whole.addWidget(self.splitter_center)
        self.layoutWidget = QWidget(self.splitter_whole)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_PCR = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_PCR.setObjectName(u"verticalLayout_PCR")
        self.verticalLayout_PCR.setContentsMargins(0, 0, 0, 0)
        self.label_parent = QLabel(self.layoutWidget)
        self.label_parent.setObjectName(u"label_parent")

        self.verticalLayout_PCR.addWidget(self.label_parent)

        self.parentTable = ConceptTable(self.layoutWidget)
        self.parentTable.setObjectName(u"parentTable")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.parentTable.sizePolicy().hasHeightForWidth())
        self.parentTable.setSizePolicy(sizePolicy2)
        self.parentTable.setMinimumSize(QSize(250, 0))

        self.verticalLayout_PCR.addWidget(self.parentTable)

        self.label_child = QLabel(self.layoutWidget)
        self.label_child.setObjectName(u"label_child")

        self.verticalLayout_PCR.addWidget(self.label_child)

        self.childTree = ConceptTree(self.layoutWidget)
        self.childTree.setObjectName(u"childTree")
        sizePolicy1.setHeightForWidth(self.childTree.sizePolicy().hasHeightForWidth())
        self.childTree.setSizePolicy(sizePolicy1)
        self.childTree.setMinimumSize(QSize(250, 0))

        self.verticalLayout_PCR.addWidget(self.childTree)

        self.label_relative = QLabel(self.layoutWidget)
        self.label_relative.setObjectName(u"label_relative")

        self.verticalLayout_PCR.addWidget(self.label_relative)

        self.relativeTable = ConceptTable(self.layoutWidget)
        self.relativeTable.setObjectName(u"relativeTable")
        sizePolicy2.setHeightForWidth(self.relativeTable.sizePolicy().hasHeightForWidth())
        self.relativeTable.setSizePolicy(sizePolicy2)
        self.relativeTable.setMinimumSize(QSize(250, 0))

        self.verticalLayout_PCR.addWidget(self.relativeTable)

        self.splitter_whole.addWidget(self.layoutWidget)

        self.horizontalLayout_3.addWidget(self.splitter_whole)


        self.retranslateUi(Concept)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Concept)
    # setupUi

    def retranslateUi(self, Concept):
        Concept.setWindowTitle(QCoreApplication.translate("Concept", u"Concept", None))
        self.actionAdd_Concept.setText(QCoreApplication.translate("Concept", u"Add Concept", None))
#if QT_CONFIG(tooltip)
        self.actionAdd_Concept.setToolTip(QCoreApplication.translate("Concept", u"Add Concept", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAdd_Concept.setShortcut(QCoreApplication.translate("Concept", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(QCoreApplication.translate("Concept", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.actionDelete.setShortcut(QCoreApplication.translate("Concept", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("Concept", u"Search", None))
        self.label_name.setText(QCoreApplication.translate("Concept", u"Name", None))
        self.label_detail.setText(QCoreApplication.translate("Concept", u"Detail", None))
        self.checkBox.setText(QCoreApplication.translate("Concept", u"Only Root", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_file), QCoreApplication.translate("Concept", u" File ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_textlist), QCoreApplication.translate("Concept", u" Text List ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_textviewer), QCoreApplication.translate("Concept", u" Text Viewer ", None))
        self.label_parent.setText(QCoreApplication.translate("Concept", u"Parent", None))
        self.label_child.setText(QCoreApplication.translate("Concept", u"Child", None))
        self.label_relative.setText(QCoreApplication.translate("Concept", u"Relative", None))
    # retranslateUi

