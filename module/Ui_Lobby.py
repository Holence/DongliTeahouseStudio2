# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Lobby.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widget import Desktop

import DTPySide.DT_rc

class Ui_Lobby(object):
    def setupUi(self, Lobby):
        if not Lobby.objectName():
            Lobby.setObjectName(u"Lobby")
        Lobby.resize(300, 184)
        self.actionCheck_Library = QAction(Lobby)
        self.actionCheck_Library.setObjectName(u"actionCheck_Library")
        self.actionCheck_Data_Completeness = QAction(Lobby)
        self.actionCheck_Data_Completeness.setObjectName(u"actionCheck_Data_Completeness")
        self.actionCheck_Data_Completeness.setShortcutContext(Qt.ApplicationShortcut)
        self.actionSave_Data = QAction(Lobby)
        self.actionSave_Data.setObjectName(u"actionSave_Data")
        self.actionSave_Data.setShortcutContext(Qt.ApplicationShortcut)
        self.actionImport_Bookmarks = QAction(Lobby)
        self.actionImport_Bookmarks.setObjectName(u"actionImport_Bookmarks")
        self.actionExport_Diary_to_Json = QAction(Lobby)
        self.actionExport_Diary_to_Json.setObjectName(u"actionExport_Diary_to_Json")
        self.actionExport_Concept_to_Json = QAction(Lobby)
        self.actionExport_Concept_to_Json.setObjectName(u"actionExport_Concept_to_Json")
        self.actionExport_Library_to_Json = QAction(Lobby)
        self.actionExport_Library_to_Json.setObjectName(u"actionExport_Library_to_Json")
        self.actionExport_Diary_to_Markdown = QAction(Lobby)
        self.actionExport_Diary_to_Markdown.setObjectName(u"actionExport_Diary_to_Markdown")
        self.actionCheck_Unsaved_Data = QAction(Lobby)
        self.actionCheck_Unsaved_Data.setObjectName(u"actionCheck_Unsaved_Data")
        self.actionCheck_Unsaved_Data.setShortcutContext(Qt.ApplicationShortcut)
        self.actionAdvanced_Search = QAction(Lobby)
        self.actionAdvanced_Search.setObjectName(u"actionAdvanced_Search")
        self.verticalLayout = QVBoxLayout(Lobby)
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(24, 28, 24, 12)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(24)
        self.btn_diary = QPushButton(Lobby)
        self.btn_diary.setObjectName(u"btn_diary")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_diary.sizePolicy().hasHeightForWidth())
        self.btn_diary.setSizePolicy(sizePolicy)
        self.btn_diary.setMinimumSize(QSize(52, 52))
        self.btn_diary.setMaximumSize(QSize(52, 52))
        self.btn_diary.setIconSize(QSize(52, 52))
        self.btn_diary.setFlat(False)

        self.gridLayout.addWidget(self.btn_diary, 0, 0, 1, 1)

        self.btn_concept = QPushButton(Lobby)
        self.btn_concept.setObjectName(u"btn_concept")
        sizePolicy.setHeightForWidth(self.btn_concept.sizePolicy().hasHeightForWidth())
        self.btn_concept.setSizePolicy(sizePolicy)
        self.btn_concept.setMinimumSize(QSize(52, 52))
        self.btn_concept.setMaximumSize(QSize(52, 52))
        self.btn_concept.setIconSize(QSize(52, 52))
        self.btn_concept.setFlat(False)

        self.gridLayout.addWidget(self.btn_concept, 0, 1, 1, 1)

        self.btn_library = QPushButton(Lobby)
        self.btn_library.setObjectName(u"btn_library")
        sizePolicy.setHeightForWidth(self.btn_library.sizePolicy().hasHeightForWidth())
        self.btn_library.setSizePolicy(sizePolicy)
        self.btn_library.setMinimumSize(QSize(52, 52))
        self.btn_library.setMaximumSize(QSize(52, 52))
        self.btn_library.setIconSize(QSize(52, 52))
        self.btn_library.setFlat(False)

        self.gridLayout.addWidget(self.btn_library, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(Lobby)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(250, 30))

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.desktop = Desktop(Lobby)
        self.desktop.setObjectName(u"desktop")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.desktop.sizePolicy().hasHeightForWidth())
        self.desktop.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.desktop)


        self.retranslateUi(Lobby)

        QMetaObject.connectSlotsByName(Lobby)
    # setupUi

    def retranslateUi(self, Lobby):
        Lobby.setWindowTitle(QCoreApplication.translate("Lobby", u"Lobby", None))
        self.actionCheck_Library.setText(QCoreApplication.translate("Lobby", u"Check Library", None))
        self.actionCheck_Data_Completeness.setText(QCoreApplication.translate("Lobby", u"Check Data Completeness", None))
#if QT_CONFIG(shortcut)
        self.actionCheck_Data_Completeness.setShortcut(QCoreApplication.translate("Lobby", u"F4", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_Data.setText(QCoreApplication.translate("Lobby", u"Save Data", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Data.setShortcut(QCoreApplication.translate("Lobby", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionImport_Bookmarks.setText(QCoreApplication.translate("Lobby", u"Import Bookmarks", None))
        self.actionExport_Diary_to_Json.setText(QCoreApplication.translate("Lobby", u"Export Diary to Json", None))
        self.actionExport_Concept_to_Json.setText(QCoreApplication.translate("Lobby", u"Export Concept to Json", None))
        self.actionExport_Library_to_Json.setText(QCoreApplication.translate("Lobby", u"Export Library to Json", None))
        self.actionExport_Diary_to_Markdown.setText(QCoreApplication.translate("Lobby", u"Export Diary to Markdown", None))
        self.actionCheck_Unsaved_Data.setText(QCoreApplication.translate("Lobby", u"Check Unsaved Data", None))
#if QT_CONFIG(tooltip)
        self.actionCheck_Unsaved_Data.setToolTip(QCoreApplication.translate("Lobby", u"Check Unsaved Data", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionCheck_Unsaved_Data.setShortcut(QCoreApplication.translate("Lobby", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdvanced_Search.setText(QCoreApplication.translate("Lobby", u"Advanced Search", None))
        self.btn_diary.setText("")
        self.btn_concept.setText("")
        self.btn_library.setText("")
    # retranslateUi

