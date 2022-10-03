# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Diary.ui'
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
from widget import BackButton

import DTPySide.DT_rc

class Ui_Diary(object):
    def setupUi(self, Diary):
        if not Diary.objectName():
            Diary.setObjectName(u"Diary")
        Diary.resize(1039, 603)
        self.actionSwitch_Eidt_View = QAction(Diary)
        self.actionSwitch_Eidt_View.setObjectName(u"actionSwitch_Eidt_View")
        self.actionPrevious_Day = QAction(Diary)
        self.actionPrevious_Day.setObjectName(u"actionPrevious_Day")
        self.actionNext_Day = QAction(Diary)
        self.actionNext_Day.setObjectName(u"actionNext_Day")
        self.actionAdd_Line = QAction(Diary)
        self.actionAdd_Line.setObjectName(u"actionAdd_Line")
        self.actionDelete = QAction(Diary)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionNext_Week = QAction(Diary)
        self.actionNext_Week.setObjectName(u"actionNext_Week")
        self.actionPrevious_Week = QAction(Diary)
        self.actionPrevious_Week.setObjectName(u"actionPrevious_Week")
        self.actionNext_Line = QAction(Diary)
        self.actionNext_Line.setObjectName(u"actionNext_Line")
        self.actionPrevious_Line = QAction(Diary)
        self.actionPrevious_Line.setObjectName(u"actionPrevious_Line")
        self.actionFirst_Line = QAction(Diary)
        self.actionFirst_Line.setObjectName(u"actionFirst_Line")
        self.actionLast_Line = QAction(Diary)
        self.actionLast_Line.setObjectName(u"actionLast_Line")
        self.actionFind_Text = QAction(Diary)
        self.actionFind_Text.setObjectName(u"actionFind_Text")
        self.actionAdd_Concept = QAction(Diary)
        self.actionAdd_Concept.setObjectName(u"actionAdd_Concept")
        self.actionImport_Text = QAction(Diary)
        self.actionImport_Text.setObjectName(u"actionImport_Text")
        self.actionGoto_Random_Day = QAction(Diary)
        self.actionGoto_Random_Day.setObjectName(u"actionGoto_Random_Day")
        self.horizontalLayout = QHBoxLayout(Diary)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter_whole = QSplitter(Diary)
        self.splitter_whole.setObjectName(u"splitter_whole")
        self.splitter_whole.setOrientation(Qt.Horizontal)
        self.stackedWidget = QStackedWidget(self.splitter_whole)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_edit = QWidget()
        self.page_edit.setObjectName(u"page_edit")
        self.verticalLayout = QVBoxLayout(self.page_edit)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter_left = QSplitter(self.page_edit)
        self.splitter_left.setObjectName(u"splitter_left")
        self.splitter_left.setOrientation(Qt.Vertical)
        self.splitter_left.setChildrenCollapsible(False)
        self.textList = TextList(self.splitter_left)
        self.textList.setObjectName(u"textList")
        self.textList.setMinimumSize(QSize(600, 259))
        self.splitter_left.addWidget(self.textList)
        self.textEdit = DTPlainTextEdit(self.splitter_left)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(600, 178))
        self.splitter_left.addWidget(self.textEdit)

        self.verticalLayout.addWidget(self.splitter_left)

        self.stackedWidget.addWidget(self.page_edit)
        self.page_view = QWidget()
        self.page_view.setObjectName(u"page_view")
        self.horizontalLayout_2 = QHBoxLayout(self.page_view)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textViewer = MarkdownViewer(self.page_view)
        self.textViewer.setObjectName(u"textViewer")
        self.textViewer.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.textViewer)

        self.stackedWidget.addWidget(self.page_view)
        self.splitter_whole.addWidget(self.stackedWidget)
        self.splitter_right = QSplitter(self.splitter_whole)
        self.splitter_right.setObjectName(u"splitter_right")
        self.splitter_right.setOrientation(Qt.Vertical)
        self.calendarWidget = QWidget(self.splitter_right)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMinimumSize(QSize(0, 259))
        self.calendarWidget.setMaximumSize(QSize(16777215, 259))
        self.verticalLayout_2 = QVBoxLayout(self.calendarWidget)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_calendar = QLabel(self.calendarWidget)
        self.label_calendar.setObjectName(u"label_calendar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_calendar.sizePolicy().hasHeightForWidth())
        self.label_calendar.setSizePolicy(sizePolicy)
        self.label_calendar.setMinimumSize(QSize(0, 15))
        self.label_calendar.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_3.addWidget(self.label_calendar)

        self.pushButton_back = BackButton(self.calendarWidget)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setMinimumSize(QSize(0, 15))

        self.horizontalLayout_3.addWidget(self.pushButton_back)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.calendar = QCalendarWidget(self.calendarWidget)
        self.calendar.setObjectName(u"calendar")
        sizePolicy.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy)
        self.calendar.setMinimumSize(QSize(0, 240))
        self.calendar.setMaximumSize(QSize(16777215, 240))
        self.calendar.setFirstDayOfWeek(Qt.Monday)
        self.calendar.setGridVisible(False)
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)
        self.calendar.setNavigationBarVisible(False)
        self.calendar.setDateEditEnabled(True)

        self.verticalLayout_2.addWidget(self.calendar)

        self.splitter_right.addWidget(self.calendarWidget)
        self.layoutWidget_4 = QWidget(self.splitter_right)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.verticalLayout_concept = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_concept.setSpacing(4)
        self.verticalLayout_concept.setObjectName(u"verticalLayout_concept")
        self.verticalLayout_concept.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.layoutWidget_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_concept = ConceptSearch(self.layoutWidget_4)
        self.lineEdit_concept.setObjectName(u"lineEdit_concept")

        self.horizontalLayout_4.addWidget(self.lineEdit_concept)


        self.verticalLayout_concept.addLayout(self.horizontalLayout_4)

        self.conceptTable = ConceptTable(self.layoutWidget_4)
        self.conceptTable.setObjectName(u"conceptTable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.conceptTable.sizePolicy().hasHeightForWidth())
        self.conceptTable.setSizePolicy(sizePolicy1)

        self.verticalLayout_concept.addWidget(self.conceptTable)

        self.splitter_right.addWidget(self.layoutWidget_4)
        self.layoutWidget1_2 = QWidget(self.splitter_right)
        self.layoutWidget1_2.setObjectName(u"layoutWidget1_2")
        self.verticalLayout_file = QVBoxLayout(self.layoutWidget1_2)
        self.verticalLayout_file.setSpacing(4)
        self.verticalLayout_file.setObjectName(u"verticalLayout_file")
        self.verticalLayout_file.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget1_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_file.addWidget(self.label_6)

        self.fileTab = FileTab(self.layoutWidget1_2)
        self.fileTab.setObjectName(u"fileTab")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fileTab.sizePolicy().hasHeightForWidth())
        self.fileTab.setSizePolicy(sizePolicy2)

        self.verticalLayout_file.addWidget(self.fileTab)

        self.splitter_right.addWidget(self.layoutWidget1_2)
        self.splitter_whole.addWidget(self.splitter_right)

        self.horizontalLayout.addWidget(self.splitter_whole)


        self.retranslateUi(Diary)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Diary)
    # setupUi

    def retranslateUi(self, Diary):
        Diary.setWindowTitle(QCoreApplication.translate("Diary", u"Diary", None))
        self.actionSwitch_Eidt_View.setText(QCoreApplication.translate("Diary", u"Switch Eidt / View", None))
#if QT_CONFIG(tooltip)
        self.actionSwitch_Eidt_View.setToolTip(QCoreApplication.translate("Diary", u"Switch Eidt / View", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSwitch_Eidt_View.setShortcut(QCoreApplication.translate("Diary", u"F9", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrevious_Day.setText(QCoreApplication.translate("Diary", u"Previous Day", None))
#if QT_CONFIG(tooltip)
        self.actionPrevious_Day.setToolTip(QCoreApplication.translate("Diary", u"Previous Day", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPrevious_Day.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+Alt+Left", None))
#endif // QT_CONFIG(shortcut)
        self.actionNext_Day.setText(QCoreApplication.translate("Diary", u"Next Day", None))
#if QT_CONFIG(tooltip)
        self.actionNext_Day.setToolTip(QCoreApplication.translate("Diary", u"Next Day", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionNext_Day.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+Alt+Right", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdd_Line.setText(QCoreApplication.translate("Diary", u"Add Line", None))
#if QT_CONFIG(tooltip)
        self.actionAdd_Line.setToolTip(QCoreApplication.translate("Diary", u"Add Line", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAdd_Line.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(QCoreApplication.translate("Diary", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.actionDelete.setShortcut(QCoreApplication.translate("Diary", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionNext_Week.setText(QCoreApplication.translate("Diary", u"Next Week", None))
#if QT_CONFIG(shortcut)
        self.actionNext_Week.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+Alt+Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrevious_Week.setText(QCoreApplication.translate("Diary", u"Previous Week", None))
#if QT_CONFIG(shortcut)
        self.actionPrevious_Week.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+Alt+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionNext_Line.setText(QCoreApplication.translate("Diary", u"Next Line", None))
#if QT_CONFIG(shortcut)
        self.actionNext_Line.setShortcut(QCoreApplication.translate("Diary", u"Alt+Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrevious_Line.setText(QCoreApplication.translate("Diary", u"Previous Line", None))
#if QT_CONFIG(shortcut)
        self.actionPrevious_Line.setShortcut(QCoreApplication.translate("Diary", u"Alt+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionFirst_Line.setText(QCoreApplication.translate("Diary", u"First Line", None))
#if QT_CONFIG(shortcut)
        self.actionFirst_Line.setShortcut(QCoreApplication.translate("Diary", u"Alt+Left", None))
#endif // QT_CONFIG(shortcut)
        self.actionLast_Line.setText(QCoreApplication.translate("Diary", u"Last Line", None))
#if QT_CONFIG(shortcut)
        self.actionLast_Line.setShortcut(QCoreApplication.translate("Diary", u"Alt+Right", None))
#endif // QT_CONFIG(shortcut)
        self.actionFind_Text.setText(QCoreApplication.translate("Diary", u"Find Text", None))
#if QT_CONFIG(shortcut)
        self.actionFind_Text.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdd_Concept.setText(QCoreApplication.translate("Diary", u"Add Concept", None))
#if QT_CONFIG(shortcut)
        self.actionAdd_Concept.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionImport_Text.setText(QCoreApplication.translate("Diary", u"Import Text", None))
#if QT_CONFIG(shortcut)
        self.actionImport_Text.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionGoto_Random_Day.setText(QCoreApplication.translate("Diary", u"Goto Random Day", None))
#if QT_CONFIG(shortcut)
        self.actionGoto_Random_Day.setShortcut(QCoreApplication.translate("Diary", u"F8", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_back.setText("")
        self.label_5.setText(QCoreApplication.translate("Diary", u"Concept", None))
        self.label_6.setText(QCoreApplication.translate("Diary", u"File", None))
    # retranslateUi

