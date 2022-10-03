# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_LibraryCheck.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LibraryCheck(object):
    def setupUi(self, LibraryCheck):
        if not LibraryCheck.objectName():
            LibraryCheck.setObjectName(u"LibraryCheck")
        LibraryCheck.resize(1400, 900)
        LibraryCheck.setMinimumSize(QSize(1400, 900))
        self.horizontalLayout_14 = QHBoxLayout(LibraryCheck)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton_refresh = QPushButton(LibraryCheck)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_refresh.sizePolicy().hasHeightForWidth())
        self.pushButton_refresh.setSizePolicy(sizePolicy)

        self.verticalLayout_12.addWidget(self.pushButton_refresh)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(LibraryCheck)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.label_2)

        self.missing = QTableWidget(LibraryCheck)
        if (self.missing.columnCount() < 5):
            self.missing.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.missing.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.missing.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.missing.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.missing.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.missing.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.missing.setObjectName(u"missing")
        self.missing.setMinimumSize(QSize(300, 0))
        self.missing.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.missing.setTabKeyNavigation(False)
        self.missing.setDragDropOverwriteMode(False)
        self.missing.setDragDropMode(QAbstractItemView.DragOnly)
        self.missing.setDefaultDropAction(Qt.MoveAction)
        self.missing.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.missing.horizontalHeader().setStretchLastSection(True)
        self.missing.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.missing)

        self.pushButton_erase = QPushButton(LibraryCheck)
        self.pushButton_erase.setObjectName(u"pushButton_erase")
        sizePolicy.setHeightForWidth(self.pushButton_erase.sizePolicy().hasHeightForWidth())
        self.pushButton_erase.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.pushButton_erase)


        self.horizontalLayout_13.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(LibraryCheck)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_9.addWidget(self.label_3)

        self.redundant = QListWidget(LibraryCheck)
        self.redundant.setObjectName(u"redundant")
        self.redundant.setMinimumSize(QSize(300, 0))
        self.redundant.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.redundant.setDragDropMode(QAbstractItemView.DragOnly)
        self.redundant.setDefaultDropAction(Qt.MoveAction)
        self.redundant.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_9.addWidget(self.redundant)

        self.pushButton_add = QPushButton(LibraryCheck)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)

        self.verticalLayout_9.addWidget(self.pushButton_add)


        self.horizontalLayout_13.addLayout(self.verticalLayout_9)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.left = QTableWidget(LibraryCheck)
        if (self.left.columnCount() < 5):
            self.left.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.left.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.left.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.left.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.left.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.left.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.left.setObjectName(u"left")
        self.left.setMinimumSize(QSize(300, 0))
        self.left.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.left.setDragDropMode(QAbstractItemView.DropOnly)
        self.left.setDefaultDropAction(Qt.MoveAction)
        self.left.setSelectionMode(QAbstractItemView.NoSelection)
        self.left.horizontalHeader().setVisible(False)
        self.left.horizontalHeader().setStretchLastSection(True)
        self.left.verticalHeader().setVisible(False)

        self.verticalLayout_10.addWidget(self.left)


        self.horizontalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.right = QListWidget(LibraryCheck)
        self.right.setObjectName(u"right")
        self.right.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.right.setDragDropMode(QAbstractItemView.DropOnly)
        self.right.setDefaultDropAction(Qt.MoveAction)
        self.right.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_11.addWidget(self.right)


        self.horizontalLayout_12.addLayout(self.verticalLayout_11)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.pushButton_replace = QPushButton(LibraryCheck)
        self.pushButton_replace.setObjectName(u"pushButton_replace")

        self.verticalLayout_12.addWidget(self.pushButton_replace)

        self.pushButton_move_replace = QPushButton(LibraryCheck)
        self.pushButton_move_replace.setObjectName(u"pushButton_move_replace")

        self.verticalLayout_12.addWidget(self.pushButton_move_replace)


        self.horizontalLayout_14.addLayout(self.verticalLayout_12)

        self.plainTextEdit = QPlainTextEdit(LibraryCheck)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy2)
        self.plainTextEdit.setMinimumSize(QSize(300, 0))
        self.plainTextEdit.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.plainTextEdit)


        self.retranslateUi(LibraryCheck)

        QMetaObject.connectSlotsByName(LibraryCheck)
    # setupUi

    def retranslateUi(self, LibraryCheck):
        LibraryCheck.setWindowTitle(QCoreApplication.translate("LibraryCheck", u"LibraryCheck", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("LibraryCheck", u" Refresh ", None))
        self.label_2.setText(QCoreApplication.translate("LibraryCheck", u"Missing Files", None))
        ___qtablewidgetitem = self.missing.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LibraryCheck", u"Type", None));
        ___qtablewidgetitem1 = self.missing.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LibraryCheck", u"Date", None));
        ___qtablewidgetitem2 = self.missing.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LibraryCheck", u"Ext", None));
        ___qtablewidgetitem3 = self.missing.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("LibraryCheck", u"File", None));
        ___qtablewidgetitem4 = self.missing.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("LibraryCheck", u"Url", None));
        self.pushButton_erase.setText(QCoreApplication.translate("LibraryCheck", u" Erase ", None))
        self.label_3.setText(QCoreApplication.translate("LibraryCheck", u"Redundant Files", None))
        self.pushButton_add.setText(QCoreApplication.translate("LibraryCheck", u" Add ", None))
        ___qtablewidgetitem5 = self.left.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("LibraryCheck", u"Type", None));
        ___qtablewidgetitem6 = self.left.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("LibraryCheck", u"Date", None));
        ___qtablewidgetitem7 = self.left.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("LibraryCheck", u"Ext", None));
        ___qtablewidgetitem8 = self.left.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("LibraryCheck", u"File", None));
        ___qtablewidgetitem9 = self.left.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("LibraryCheck", u"Url", None));
        self.pushButton_replace.setText(QCoreApplication.translate("LibraryCheck", u"<--\n"
" Replace", None))
        self.pushButton_move_replace.setText(QCoreApplication.translate("LibraryCheck", u"<--\n"
" Move and Replace", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("LibraryCheck", u"This is a log.", None))
    # retranslateUi

