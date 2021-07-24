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

import DTPySide.DT_rc

class Ui_Lobby(object):
    def setupUi(self, Lobby):
        if not Lobby.objectName():
            Lobby.setObjectName(u"Lobby")
        Lobby.resize(925, 663)
        self.verticalLayout = QVBoxLayout(Lobby)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_diary = QPushButton(Lobby)
        self.btn_diary.setObjectName(u"btn_diary")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_diary.sizePolicy().hasHeightForWidth())
        self.btn_diary.setSizePolicy(sizePolicy)
        self.btn_diary.setMinimumSize(QSize(64, 64))
        self.btn_diary.setMaximumSize(QSize(64, 64))
        icon = QIcon()
        icon.addFile(u":/icon/white/white_feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_diary.setIcon(icon)
        self.btn_diary.setIconSize(QSize(64, 64))
        self.btn_diary.setFlat(False)

        self.gridLayout.addWidget(self.btn_diary, 0, 0, 1, 1)

        self.btn_concept = QPushButton(Lobby)
        self.btn_concept.setObjectName(u"btn_concept")
        sizePolicy.setHeightForWidth(self.btn_concept.sizePolicy().hasHeightForWidth())
        self.btn_concept.setSizePolicy(sizePolicy)
        self.btn_concept.setMinimumSize(QSize(64, 64))
        self.btn_concept.setMaximumSize(QSize(64, 64))
        icon1 = QIcon()
        icon1.addFile(u":/icon/white/white_hash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_concept.setIcon(icon1)
        self.btn_concept.setIconSize(QSize(64, 64))
        self.btn_concept.setFlat(False)

        self.gridLayout.addWidget(self.btn_concept, 0, 1, 1, 1)

        self.btn_library = QPushButton(Lobby)
        self.btn_library.setObjectName(u"btn_library")
        sizePolicy.setHeightForWidth(self.btn_library.sizePolicy().hasHeightForWidth())
        self.btn_library.setSizePolicy(sizePolicy)
        self.btn_library.setMinimumSize(QSize(64, 64))
        self.btn_library.setMaximumSize(QSize(64, 64))
        icon2 = QIcon()
        icon2.addFile(u":/icon/white/white_inbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_library.setIcon(icon2)
        self.btn_library.setIconSize(QSize(64, 64))
        self.btn_library.setFlat(False)

        self.gridLayout.addWidget(self.btn_library, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.plainTextEdit = QPlainTextEdit(Lobby)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.retranslateUi(Lobby)

        QMetaObject.connectSlotsByName(Lobby)
    # setupUi

    def retranslateUi(self, Lobby):
        Lobby.setWindowTitle(QCoreApplication.translate("Lobby", u"Lobby", None))
        self.btn_diary.setText("")
        self.btn_concept.setText("")
        self.btn_library.setText("")
        self.plainTextEdit.setPlainText("")
    # retranslateUi

