# # --
from DTPySide import *

from session import LobbySession
from module.Ui_AdvanceSearch import Ui_AdvanceSearch
class AdvanceSearch(Ui_AdvanceSearch, QWidget):
	def __init__(self, parent, Headquarter:LobbySession):
		super().__init__(parent=parent)
		self.setupUi(self)
		self.Headquarter=Headquarter
		
		self.pushButton.clicked.connect(self.exec)
		self.splitter_h.setStretchFactor(0,3)
		self.splitter_h.setStretchFactor(1,2)
		self.splitter_v.setStretchFactor(0,3)
		self.splitter_v.setStretchFactor(1,2)
		
		self.setStyleSheet("""
		QPlainTextEdit{
			font-family:consolas;
			font-size:12pt;
		}

		QLabel, QPushButton{
			font-size:12pt;
		}
		""")
		self.code_input.setTabStopWidth(24)
		self.code_help.setTabStopWidth(24)
		self.code_output.setTabStopWidth(24)

		self.code_input.setPlainText("# your code here...\n\noutput = \"your output\"")
		self.code_help.setPlainText("""Diary:

for year in Diary:
	for month in Diary[year]:
		for day in Diary[year][month]:
			for line_dict in Diary[year][month][day]:
			
			# line_text (str)
			line_text = line_dict["text"]
			
			# list of concept's id (int)
			concept_list = line_dict["concept"]
			
			# list of file_dict (dict)
			file_list = line_dict["file"]
			for file_dict in file_list:
				
				# date (int)
				file_year = file_dict["y"]
				file_month = file_dict["m"]
				file_day = file_dict["d"]

				# name (str)
				file_name = file_dict["name"]

				# url (str)
				# "file_year/file_month/file_day/file_name" or "https://..."
				file_url = file_dict["url"]

				# type (int)
				# 0-folder, 1-file, 2-link
				file_type = file_dict["type"]

------------------------------------------------------------

Concept (list of concept_dict):

for concept_dict in Concept:
	
	# id (int)
	concept_id = concept_dict["id"]

	# name (str)
	concept_name = concept_dict["name"]
	
	# detail (str)
	concept_detail = concept_dict["detail"]

	# list of parents' id (int)
	concept_parent = concept_dict["parent"]
	
	# list of children's id (int)
	concept_child = concept_dict["child"]
	
	# list of relatives' id (int)
	concept_relative = concept_dict["relative"]
	
	# az (str)
	concept_az = concept_dict["az"]

	# list of file_dict (dict)
	file_list = line["file"]
	for file_dict in file_list:
		
		# date (int)
		file_year = file_dict["y"]
		file_month = file_dict["m"]
		file_day = file_dict["d"]

		# name (str)
		file_name = file_dict["name"]

		# url (str)
		# "file_year/file_month/file_day/file_name" or "https://..."
		file_url = file_dict["url"]

		# type (int)
		# 0-folder, 1-file, 2-link
		file_type = file_dict["type"]

------------------------------------------------------------

Library:

for year in Library:
	for month in Library[year]:
		for day in Library[year][month]:
			for file_name in Library[year][month][day]:
				file_dict = Library[year][month][day][file_name]

				# tpe (int)
				# 0-folder, 1-file, 2-link
				file_type = file_dict["type"]

				# url (str)
				# "file_year/file_month/file_day/file_name" or "https://..."
				file_url = file_dict["url"]

				# list of concept's id (int)
				concept_list = file_dict["concept"]

""")
	
	def exec(self):
		code=self.code_input.toPlainText()
		
		Diary=self.Headquarter.data[0].copy()
		Concept=self.Headquarter.data[1].copy()
		Library=self.Headquarter.data[2].copy()

		try:
			exec("global output\n"+code)
		except Exception as e:
			self.code_output.setPlainText(str(e))
			return

		global output
		self.code_output.setPlainText(str(output))