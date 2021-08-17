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
        Lobby.resize(792, 707)
        self.actionCheck_Library = QAction(Lobby)
        self.actionCheck_Library.setObjectName(u"actionCheck_Library")
        self.actionSwitch_Secure_Mode = QAction(Lobby)
        self.actionSwitch_Secure_Mode.setObjectName(u"actionSwitch_Secure_Mode")
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
        self.verticalLayout = QVBoxLayout(Lobby)
        self.verticalLayout.setSpacing(36)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(72, 36, 72, 12)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_library = QPushButton(Lobby)
        self.btn_library.setObjectName(u"btn_library")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_library.sizePolicy().hasHeightForWidth())
        self.btn_library.setSizePolicy(sizePolicy)
        self.btn_library.setMinimumSize(QSize(64, 64))
        self.btn_library.setMaximumSize(QSize(64, 64))
        self.btn_library.setIconSize(QSize(64, 64))
        self.btn_library.setFlat(False)

        self.gridLayout.addWidget(self.btn_library, 0, 2, 1, 1)

        self.btn_concept = QPushButton(Lobby)
        self.btn_concept.setObjectName(u"btn_concept")
        sizePolicy.setHeightForWidth(self.btn_concept.sizePolicy().hasHeightForWidth())
        self.btn_concept.setSizePolicy(sizePolicy)
        self.btn_concept.setMinimumSize(QSize(64, 64))
        self.btn_concept.setMaximumSize(QSize(64, 64))
        self.btn_concept.setIconSize(QSize(64, 64))
        self.btn_concept.setFlat(False)

        self.gridLayout.addWidget(self.btn_concept, 0, 1, 1, 1)

        self.btn_diary = QPushButton(Lobby)
        self.btn_diary.setObjectName(u"btn_diary")
        sizePolicy.setHeightForWidth(self.btn_diary.sizePolicy().hasHeightForWidth())
        self.btn_diary.setSizePolicy(sizePolicy)
        self.btn_diary.setMinimumSize(QSize(64, 64))
        self.btn_diary.setMaximumSize(QSize(64, 64))
        self.btn_diary.setIconSize(QSize(64, 64))
        self.btn_diary.setFlat(False)

        self.gridLayout.addWidget(self.btn_diary, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(Lobby)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(420, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.desktop = Desktop(Lobby)
        self.desktop.setObjectName(u"desktop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.desktop.sizePolicy().hasHeightForWidth())
        self.desktop.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.desktop)


        self.retranslateUi(Lobby)

        QMetaObject.connectSlotsByName(Lobby)
    # setupUi

    def retranslateUi(self, Lobby):
        Lobby.setWindowTitle(QCoreApplication.translate("Lobby", u"Lobby", None))
        self.actionCheck_Library.setText(QCoreApplication.translate("Lobby", u"Check Library", None))
        self.actionSwitch_Secure_Mode.setText(QCoreApplication.translate("Lobby", u"Secure Mode - Off", None))
#if QT_CONFIG(tooltip)
        self.actionSwitch_Secure_Mode.setToolTip(QCoreApplication.translate("Lobby", u"Password is needed when opening modules if turned on.", None))
#endif // QT_CONFIG(tooltip)
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
        self.btn_library.setText("")
        self.btn_concept.setText("")
        self.btn_diary.setText("")
    # retranslateUi

