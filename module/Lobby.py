# # --
from DTPySide import *

from module.Ui_Lobby import Ui_Lobby
from session import LobbySession
class Lobby(QWidget,Ui_Lobby):
	def __init__(self, Headquarter: LobbySession):
		super().__init__(parent=Headquarter)
		self.setupUi(self)

		self.Headquarter=Headquarter
		self.desktop.setHeadquarter(self.Headquarter)

		self.btn_diary.clicked.connect(lambda:self.summon("diary","Diary"))
		self.btn_concept.clicked.connect(lambda:self.summon("concept","Concept"))
		self.btn_library.clicked.connect(lambda:self.summon("library","Library"))
	
		self.actionExport_to_Json.triggered.connect(self.ExportToJson)
		self.actionCheck_Library.triggered.connect(self.checkLibrary)
		self.actionSwitch_Secure_Mode.triggered.connect(self.switchSecureMode)
		self.actionCheck_Data_Completeness.triggered.connect(self.checkDataCompleteness)
		self.actionSave_Data.triggered.connect(lambda:self.Headquarter.saveData(force=True))
		self.actionImport_Bookmarks.triggered.connect(self.ImportBookmarks)

		self.SecureMode=False
		
	def switchSecureMode(self):
		if self.SecureMode==False:
			self.SecureMode=True
			self.actionSwitch_Secure_Mode.setIcon(QIcon(":/icon/white/white_toggle-right.svg"))
			self.actionSwitch_Secure_Mode.setText("Secure Mode - On")
			DTFrame.DTMessageBox(self,"Information","Secure mode is on. Password will be needed opening modules.",DTIcon.Happy())
		else:
			if DTSession.DTLoginSession(self.Headquarter.UserSetting().value("BasicInfo/Password")).exec_():
				self.SecureMode=False
				self.actionSwitch_Secure_Mode.setIcon(QIcon(":/icon/white/white_toggle-left.svg"))
				self.actionSwitch_Secure_Mode.setText("Secure Mode - Off")
				DTFrame.DTMessageBox(self,"Information","Secure mode is off. Password will not be needed opening modules.",DTIcon.Happy())
	
	def summon(self, へ_へ, ヘ＿ヘ):
		if self.SecureMode==True:
			if not DTSession.DTLoginSession(self.Headquarter.UserSetting().value("BasicInfo/Password")).exec_():
				return
		
		exec(f"""
flag=False
for {へ_へ} in self.Headquarter.{へ_へ}_heap:
	if {へ_へ}.isHidden():
		{へ_へ}.show()
		{へ_へ}.setFocus()
		flag=True
		break

if flag==True:
	# 清理掉没有hidden的
	self.Headquarter.{へ_へ}_heap=[{へ_へ} for {へ_へ} in self.Headquarter.{へ_へ}_heap if {へ_へ}.isHidden()==False]
else:
	# 新建
	from session.{ヘ＿ヘ}Session import {ヘ＿ヘ}Session
	new_{へ_へ}={ヘ＿ヘ}Session(self.Headquarter.app,self.Headquarter)
	new_{へ_へ}.initialize()
	self.Headquarter.{へ_へ}_heap.append(new_{へ_へ})
	self.Headquarter.refreshModuleSingal()
	new_{へ_へ}.show()
	new_{へ_へ}.setFocus()

# print("{ヘ＿ヘ}",len(self.Headquarter.{へ_へ}_heap))
""")
	
	def ExportToJson(self):
		Json_Save(self.Headquarter.data,"Export_Data_%s.json"%WhatDayIsToday(1).toString("yyyyMMdd"))
	
	def checkLibrary(self):
		
		if self.SecureMode==True:
			if not DTSession.DTLoginSession(self.Headquarter.UserSetting().value("BasicInfo/Password")).exec_():
				return
		
		if not os.path.exists(self.Headquarter.library_base):
			DTFrame.DTMessageBox(self,"Error","Cannot access Library, please check the direction existence!")
			return

		from module import LibraryCheck
		dlg=DTFrame.DTDialog(self,"Library Check")
		dlg.TitleBar.title_icon.setIcon(QIcon())
		dlg.TitleBar.title_icon.setText("💩")
		dlg.TitleBar.title_icon.setStyleSheet("font-size:25pt")
		
		module=LibraryCheck(self.Headquarter)
		dlg.setCentralWidget(module)
		dlg.buttonBox.hide()
		dlg.setMinimumSize(1500,800)
		dlg.exec_()

		for diary in self.Headquarter.diary_heap:
			diary.diary_module.refresh()
		for concept in self.Headquarter.concept_heap:
			concept.concept_module.refresh()
		for library in self.Headquarter.library_heap:
			library.library_module.refresh()
	
	def checkDataCompleteness(self):

		def check():
			diary_data=self.Headquarter.getDiaryData()
			concept_data=self.Headquarter.getConceptData()
			library_data=self.Headquarter.getLibraryData()

			
			# Diary
			error="\n\n--------------------------------------------Diary--------------------------------------------\n\n"
			for year in diary_data:
				for month in diary_data[year]:
					for day in diary_data[year][month]:
						line_index=0
						for line in diary_data[year][month][day]:
							
							try:
								if type(line["text"])!=str:
									error+="%s.%s.%s line_index:%s text is not str\n"%(year,month,day,line_index)
							except Exception as e:
								error+="%s.%s.%s line_index:%s %s\n"%(year,month,day,line_index,e)
							
							# concept start
							try:
								concept=line["concept"]
								if type(concept)!=list:
									error+="%s.%s.%s line_index:%s \"concept\":%s is not list\n"%(year,month,day,line_index,concept)
								else:
									for id in concept:
										if type(id)!=int:
											error+="%s.%s.%s line_index:%s concept:%s is not int\n"%(year,month,day,line_index,id)
										elif id<0:
											error+="%s.%s.%s line_index:%s concept:%s < 0 \n"%(year,month,day,line_index,id)

										try:
											concept_data[id]
										except:
											error+="%s.%s.%s line_index:%s concept:%s is not in concept_data\n"%(year,month,day,line_index,id)
							except Exception as e:
								error+="%s.%s.%s line_index:%s %s\n"%(year,month,day,line_index,e)
							# concept end

							# file start
							try:
								file=line["file"]
								if type(file)!=list:
									error+="%s.%s.%s line_index:%s file:%s is not list\n"%(year,month,day,line_index,file)
								else:
									# file loop start
									file_index=0
									for file in line["file"]:
										# single file start
										try:

											y=file["y"]
											m=file["m"]
											d=file["d"]
											name=file["name"]
											
											try:
												library_file=library_data[str(y)][str(m)][str(d)][name]
												if library_file["type"]!=file["type"] or library_file["url"]!=file["url"]:
													error+="%s.%s.%s line_index:%s file_index:%s is not equals to file in library_data: \"y\":%s \"m\":%s \"d\":%s \"name\":%s\n"%(year,month,day,line_index,file_index,y,m,d,name)
											except:
												error+="%s.%s.%s line_index:%s file_index:%s \"y\":%s \"m\":%s \"d\":%s \"name\":%s is not in library_data\n"%(year,month,day,line_index,file_index,y,m,d,name)
											# single file end
											
										except Exception as e:
											error+="%s.%s.%s line_index:%s file_index:%s %s\n"%(year,month,day,line_index,file_index,e)
										
										file_index+=1
										# file loop end

							except Exception as e:
								error+="%s.%s.%s line_index:%s %s\n"%(year,month,day,line_index,e)
							# file end

							line_index+=1

			# Concept
			error+="\n\n--------------------------------------------Concept--------------------------------------------\n\n"
			index=0
			for concept in concept_data:
				try:
					concept_id=concept["id"]
					if type(concept_id)!=int:
						error+="concept:%s id:%s is not int\n"%(index,concept_id)
					elif concept_id<0:
						error+="concept:%s id:%s < 0 \n"%(index,concept_id)
					elif concept_id!=index:
						error+="concept:%s != id:%s\n"%(index,concept_id)
				except Exception as e:
					error+="concept:%s %s \n"%(index,e)
				
				try:
					name=concept["name"]
					if type(name)!=str:
						error+="concept:%s name:%s is not str\n"%(index,name)
				except Exception as e:
					error+="concept:%s %s \n"%(index,e)
				
				try:
					detail=concept["detail"]
					if type(detail)!=str:
						error+="concept:%s detail:%s is not str\n"%(index,detail)
				except Exception as e:
					error+="concept:%s %s \n"%(index,e)
				
				try:
					parent=concept["parent"]
					if type(parent)!=list:
						error+="concept:%s parent:%s is not list\n"%(index,parent)
					else:
						for id in parent:
							try:
								concept_data[id]
							except:
								error+="concept:%s parent:%s is not in concept_data\n"%(index,id)
							
							if concept_id not in concept_data[id]["child"]:
								error+="concept:%s parent:%s is not in concept:%s 's child\n"%(index,id,id)

				except Exception as e:
					error+="concept:%s %s \n"%(index,e)
				
				try:
					child=concept["child"]
					if type(child)!=list:
						error+="concept:%s child:%s is not list\n"%(index,child)
					else:
						for id in child:
							try:
								concept_data[id]
							except:
								error+="concept:%s child:%s is not in concept_data\n"%(index,id)
							
							if concept_id not in concept_data[id]["parent"]:
								error+="concept:%s child:%s is not in concept:%s 's parent\n"%(index,id,id)
				except Exception as e:
					error+="concept:%s %s \n"%(index,e)
				
				try:
					relative=concept["relative"]
					if type(relative)!=list:
						error+="concept:%s relative:%s is not list\n"%(index,relative)
					else:
						for id in relative:
							try:
								concept_data[id]
							except:
								error+="concept:%s relative:%s is not in concept_data\n"%(index,id)
							
							if concept_id not in concept_data[id]["relative"]:
								error+="concept:%s relative:%s is not in concept:%s 's relative\n"%(index,id,id)
				except Exception as e:
					error+="concept:%s %s \n"%(index,e)
				
				try:
					az=concept["az"]
					if type(az)!=str:
						error+="concept:%s az:%s is not str\n"%(index,az)
				except Exception as e:
					error+="concept:%s %s \n"%(index,e)
				
				# file start
				try:
					file=concept["file"]
					if type(file)!=list:
						error+="concept:%s file:%s is not list\n"%(index,file)
					else:
						# file loop start
						file_index=0
						for file in concept["file"]:
							# single file start
							try:

								y=file["y"]
								m=file["m"]
								d=file["d"]
								name=file["name"]
								
								try:
									library_file=library_data[str(y)][str(m)][str(d)][name]
									if library_file["type"]!=file["type"] or library_file["url"]!=file["url"]:
										error+="concept:%s file_index:%s is not equals to file in library_data: \"y\":%s \"m\":%s \"d\":%s \"name\":%s\n"%(index,file_index,y,m,d,name)
									if concept_id not in library_file["concept"]:
										error+="concept:%s file_index:%s is not in file in library_data: \"y\":%s \"m\":%s \"d\":%s \"name\":%s 's concept\n"%(index,file_index,y,m,d,name)
								except:
									error+="concept:%s file_index:%s \"y\":%s \"m\":%s \"d\":%s \"name\":%s is not in library_data\n"%(index,file_index,y,m,d,name)
								# single file end
								
							except Exception as e:
								error+="concept:%s file_index:%s %s\n"%(index,file_index,e)
							
							file_index+=1
							# file loop end

				except Exception as e:
					error+="concept:%s %s\n"%(index,e)
				# file end

				index+=1

			# Library
			error+="\n\n--------------------------------------------Library--------------------------------------------\n\n"
			for year in library_data:
				for month in library_data[year]:
					for day in library_data[year][month]:
						for file_name in library_data[year][month][day]:
							
							if type(file_name)!=str:
								error+="%s.%s.%s file_name:%s is not str\n"%(year,month,day,file_name)
							file=library_data[year][month][day][file_name]

							try:
								TYPE=file["type"]
								if TYPE not in [0,1,2]:
									error+="%s.%s.%s file_name:%s \"type\"%s is not in [0,1,2] \n"%(year,month,day,file_name,TYPE)
							except Exception as e:
								error+="%s.%s.%s file_name:%s %s\n"%(year,month,day,file_name,e)
							
							try:
								url=file["url"]
								if type(url)!=str:
									error+="%s.%s.%s file_name:%s \"url\":%s is not str\n"%(year,month,day,file_name,url)
								else:
									if TYPE==0 or TYPE==1:
										ss=url.split("/")
										if ss[0].isdigit() and ss[1].isdigit() and ss[2].isdigit() and len(ss)==4:
											pass
										else:
											error+="%s.%s.%s file_name:%s \"url\":%s wrong format \n"%(year,month,day,file_name,url)
									elif TYPE==2:
										pass
									else:
										error+="%s.%s.%s file_name:%s \"url\":%s check yourself\n"%(year,month,day,file_name,url)
							except Exception as e:
								error+="%s.%s.%s file_name:%s %s\n"%(year,month,day,file_name,e)
							
							try:
								concept=file["concept"]
								if type(concept)!=list:
									error+="%s.%s.%s file_name:%s \"concept\":%s is not list\n"%(year,month,day,file_name,concept)
								else:
									for id in concept:
										if type(id)!=int:
											error+="%s.%s.%s file_name:%s concept:%s is not int\n"%(year,month,day,file_name,id)
										elif id<0:
											error+="%s.%s.%s file_name:%s concept:%s < 0 \n"%(year,month,day,file_name,id)

										try:
											file_dict=self.Headquarter.generateDiaryConceptFileDict(QDate(int(year),int(month),int(day)),TYPE,file_name,url)
											if file_dict not in concept_data[id]["file"]:
												error+="%s.%s.%s file_name:%s is not in concept:%s 's file\n"%(year,month,day,file_name,id)
										except:
											error+="%s.%s.%s file_name:%s concept:%s is not in concept_data\n"%(year,month,day,file_name,id)
							except Exception as e:
								error+="%s.%s.%s file_name:%s %s\n"%(year,month,day,file_name,e)
			
			return error
		
		def slot():
			self.DataChecker.deleteLater()
			del self.DataChecker
		
		error=check()
		
		try:
			self.DataChecker.errorText.setPlainText(error)
		except:
			self.DataChecker=DTFrame.DTMainWindow(self.Headquarter.app)
			self.DataChecker.initialize()
			self.DataChecker.setWindowTitle("Check Data Completeness")

			self.DataChecker.actionExit.triggered.disconnect(self.DataChecker.close)
			self.DataChecker.actionExit.triggered.connect(slot)
			self.DataChecker.TitleBar.btn_close.clicked.disconnect(self.DataChecker.close)
			self.DataChecker.TitleBar.btn_close.clicked.connect(slot)

			self.DataChecker.errorText=QPlainTextEdit(error)
			self.DataChecker.setMinimumSize(300,500)
			self.DataChecker.setCentralWidget(self.DataChecker.errorText)
			self.DataChecker.show()
	
	def ImportBookmarks(self):
		def slot():
			del self.bookmark_parser_window
		
		if hasattr(self,"bookmark_parser_window"):
			self.bookmark_parser_window.setFocus()
			return
		
		from session import BookmarkParserSession
		self.bookmark_parser_window=BookmarkParserSession(self.Headquarter.app,self.Headquarter)
		self.bookmark_parser_window.closed.connect(slot)
		self.bookmark_parser_window.show()
