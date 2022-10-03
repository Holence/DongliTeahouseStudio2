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

from widget import FileTab
from widget import ConceptTable
from DTPySide.DTWidget import DTPlainTextEdit
from widget import TextList
from widget import ConceptSearch
from DTPySide.DTWidget import MarkdownViewer
from widget import ConceptTree
from widget import BackButton

import DTPySide.DT_rc

class Ui_Concept(object):
    def setupUi(self, Concept):
        if not Concept.objectName():
            Concept.setObjectName(u"Concept")
        Concept.resize(886, 622)
        self.actionAdd_Concept = QAction(Concept)
        self.actionAdd_Concept.setObjectName(u"actionAdd_Concept")
        self.actionDelete = QAction(Concept)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionAdd_Parent = QAction(Concept)
        self.actionAdd_Parent.setObjectName(u"actionAdd_Parent")
        self.actionAdd_Child = QAction(Concept)
        self.actionAdd_Child.setObjectName(u"actionAdd_Child")
        self.actionAdd_Relative = QAction(Concept)
        self.actionAdd_Relative.setObjectName(u"actionAdd_Relative")
        self.actionSearch_Concept = QAction(Concept)
        self.actionSearch_Concept.setObjectName(u"actionSearch_Concept")
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
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_search = QLabel(self.layoutWidget4)
        self.label_search.setObjectName(u"label_search")

        self.horizontalLayout_6.addWidget(self.label_search)

        self.pushButton_back = BackButton(self.layoutWidget4)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.horizontalLayout_6.addWidget(self.pushButton_back)


        self.layoutSearch.addLayout(self.horizontalLayout_6)

        self.lineEdit_search = QLineEdit(self.layoutWidget4)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setMinimumSize(QSize(200, 0))

        self.layoutSearch.addWidget(self.lineEdit_search)

        self.conceptTable = ConceptTable(self.layoutWidget4)
        self.conceptTable.setObjectName(u"conceptTable")
        self.conceptTable.setMinimumSize(QSize(200, 0))

        self.layoutSearch.addWidget(self.conceptTable)

        self.splitter_whole.addWidget(self.layoutWidget4)
        self.layoutWidget = QWidget(self.splitter_whole)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_center = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_center.setObjectName(u"verticalLayout_center")
        self.verticalLayout_center.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_name = QVBoxLayout()
        self.verticalLayout_name.setObjectName(u"verticalLayout_name")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_name = QLabel(self.layoutWidget)
        self.label_name.setObjectName(u"label_name")

        self.horizontalLayout_7.addWidget(self.label_name)

        self.pushButton_delete = QPushButton(self.layoutWidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.horizontalLayout_7.addWidget(self.pushButton_delete)


        self.verticalLayout_name.addLayout(self.horizontalLayout_7)

        self.lineEdit_name = QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(425, 0))

        self.verticalLayout_name.addWidget(self.lineEdit_name)


        self.verticalLayout_center.addLayout(self.verticalLayout_name)

        self.splitter_center = QSplitter(self.layoutWidget)
        self.splitter_center.setObjectName(u"splitter_center")
        self.splitter_center.setOrientation(Qt.Vertical)
        self.layoutWidget_2 = QWidget(self.splitter_center)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.verticalLayout_detail = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_detail.setObjectName(u"verticalLayout_detail")
        self.verticalLayout_detail.setContentsMargins(0, 0, 0, 0)
        self.label_detail = QLabel(self.layoutWidget_2)
        self.label_detail.setObjectName(u"label_detail")

        self.verticalLayout_detail.addWidget(self.label_detail)

        self.plainTextEdit_detail = DTPlainTextEdit(self.layoutWidget_2)
        self.plainTextEdit_detail.setObjectName(u"plainTextEdit_detail")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_detail.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_detail.setSizePolicy(sizePolicy)
        self.plainTextEdit_detail.setMinimumSize(QSize(425, 100))

        self.verticalLayout_detail.addWidget(self.plainTextEdit_detail)

        self.splitter_center.addWidget(self.layoutWidget_2)
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
        self.fileTab = FileTab(self.tab_file)
        self.fileTab.setObjectName(u"fileTab")

        self.horizontalLayout.addWidget(self.fileTab)

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
        self.textViewer = MarkdownViewer(self.tab_textviewer)
        self.textViewer.setObjectName(u"textViewer")
        self.textViewer.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.textViewer)

        self.tabWidget.addTab(self.tab_textviewer, "")

        self.verticalLayout_tab.addWidget(self.tabWidget)

        self.splitter_center.addWidget(self.layoutWidget9)

        self.verticalLayout_center.addWidget(self.splitter_center)

        self.splitter_whole.addWidget(self.layoutWidget)
        self.layoutWidget_1 = QWidget(self.splitter_whole)
        self.layoutWidget_1.setObjectName(u"layoutWidget_1")
        self.verticalLayout_PCR = QVBoxLayout(self.layoutWidget_1)
        self.verticalLayout_PCR.setObjectName(u"verticalLayout_PCR")
        self.verticalLayout_PCR.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_parent = QHBoxLayout()
        self.horizontalLayout_parent.setObjectName(u"horizontalLayout_parent")
        self.label_parent = QLabel(self.layoutWidget_1)
        self.label_parent.setObjectName(u"label_parent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_parent.sizePolicy().hasHeightForWidth())
        self.label_parent.setSizePolicy(sizePolicy2)

        self.horizontalLayout_parent.addWidget(self.label_parent)

        self.lineEdit_parent = ConceptSearch(self.layoutWidget_1)
        self.lineEdit_parent.setObjectName(u"lineEdit_parent")

        self.horizontalLayout_parent.addWidget(self.lineEdit_parent)


        self.verticalLayout_PCR.addLayout(self.horizontalLayout_parent)

        self.parentTable = ConceptTable(self.layoutWidget_1)
        self.parentTable.setObjectName(u"parentTable")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.parentTable.sizePolicy().hasHeightForWidth())
        self.parentTable.setSizePolicy(sizePolicy3)
        self.parentTable.setMinimumSize(QSize(225, 0))

        self.verticalLayout_PCR.addWidget(self.parentTable)

        self.horizontalLayout_child = QHBoxLayout()
        self.horizontalLayout_child.setObjectName(u"horizontalLayout_child")
        self.label_child = QLabel(self.layoutWidget_1)
        self.label_child.setObjectName(u"label_child")
        sizePolicy2.setHeightForWidth(self.label_child.sizePolicy().hasHeightForWidth())
        self.label_child.setSizePolicy(sizePolicy2)

        self.horizontalLayout_child.addWidget(self.label_child)

        self.lineEdit_child = ConceptSearch(self.layoutWidget_1)
        self.lineEdit_child.setObjectName(u"lineEdit_child")

        self.horizontalLayout_child.addWidget(self.lineEdit_child)


        self.verticalLayout_PCR.addLayout(self.horizontalLayout_child)

        self.childTree = ConceptTree(self.layoutWidget_1)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.childTree.setHeaderItem(__qtreewidgetitem)
        self.childTree.setObjectName(u"childTree")
        sizePolicy1.setHeightForWidth(self.childTree.sizePolicy().hasHeightForWidth())
        self.childTree.setSizePolicy(sizePolicy1)
        self.childTree.setMinimumSize(QSize(225, 0))

        self.verticalLayout_PCR.addWidget(self.childTree)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_relative = QLabel(self.layoutWidget_1)
        self.label_relative.setObjectName(u"label_relative")
        sizePolicy2.setHeightForWidth(self.label_relative.sizePolicy().hasHeightForWidth())
        self.label_relative.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.label_relative)

        self.lineEdit_relative = ConceptSearch(self.layoutWidget_1)
        self.lineEdit_relative.setObjectName(u"lineEdit_relative")

        self.horizontalLayout_5.addWidget(self.lineEdit_relative)


        self.verticalLayout_PCR.addLayout(self.horizontalLayout_5)

        self.relativeTable = ConceptTable(self.layoutWidget_1)
        self.relativeTable.setObjectName(u"relativeTable")
        sizePolicy3.setHeightForWidth(self.relativeTable.sizePolicy().hasHeightForWidth())
        self.relativeTable.setSizePolicy(sizePolicy3)
        self.relativeTable.setMinimumSize(QSize(225, 0))

        self.verticalLayout_PCR.addWidget(self.relativeTable)

        self.splitter_whole.addWidget(self.layoutWidget_1)

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
        self.actionAdd_Parent.setText(QCoreApplication.translate("Concept", u"Add Parent", None))
#if QT_CONFIG(shortcut)
        self.actionAdd_Parent.setShortcut(QCoreApplication.translate("Concept", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdd_Child.setText(QCoreApplication.translate("Concept", u"Add Child", None))
#if QT_CONFIG(shortcut)
        self.actionAdd_Child.setShortcut(QCoreApplication.translate("Concept", u"Ctrl+2", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdd_Relative.setText(QCoreApplication.translate("Concept", u"Add Relative", None))
#if QT_CONFIG(shortcut)
        self.actionAdd_Relative.setShortcut(QCoreApplication.translate("Concept", u"Ctrl+3", None))
#endif // QT_CONFIG(shortcut)
        self.actionSearch_Concept.setText(QCoreApplication.translate("Concept", u"Search Concept", None))
#if QT_CONFIG(shortcut)
        self.actionSearch_Concept.setShortcut(QCoreApplication.translate("Concept", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.label_search.setText(QCoreApplication.translate("Concept", u"Search", None))
        self.pushButton_back.setText("")
        self.label_name.setText(QCoreApplication.translate("Concept", u"Name", None))
        self.pushButton_delete.setText("")
        self.label_detail.setText(QCoreApplication.translate("Concept", u"Detail", None))
        self.checkBox.setText(QCoreApplication.translate("Concept", u"Only Root", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_file), QCoreApplication.translate("Concept", u"File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_textlist), QCoreApplication.translate("Concept", u"Text List", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_textviewer), QCoreApplication.translate("Concept", u"Text Viewer", None))
        self.label_parent.setText(QCoreApplication.translate("Concept", u"Parent", None))
        self.label_child.setText(QCoreApplication.translate("Concept", u"Child", None))
        self.label_relative.setText(QCoreApplication.translate("Concept", u"Relative", None))
    # retranslateUi

