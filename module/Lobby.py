# # --
from DTPySide import *

from module.Ui_Lobby import Ui_Lobby
from session import LobbySession
class Lobby(Ui_Lobby, QWidget):
	def __init__(self, Headquarter: LobbySession):
		super().__init__(parent=Headquarter)
		self.setupUi(self)

		self.Headquarter=Headquarter
		self.desktop.setHeadquarter(self.Headquarter)

		self.btn_diary.clicked.connect(lambda:self.summon("diary","Diary"))
		self.btn_diary.setIcon(IconFromCurrentTheme("feather.svg"))

		self.btn_concept.clicked.connect(lambda:self.summon("concept","Concept"))
		self.btn_concept.setIcon(IconFromCurrentTheme("hash.svg"))

		self.btn_library.clicked.connect(lambda:self.summon("library","Library"))
		self.btn_library.setIcon(IconFromCurrentTheme("inbox.svg"))
	
		self.actionExport_Diary_to_Json.triggered.connect(lambda:self.ExportToJson(0))
		self.actionExport_Diary_to_Json.setIcon(IconFromCurrentTheme("upload-cloud.svg"))
		self.actionExport_Concept_to_Json.triggered.connect(lambda:self.ExportToJson(1))
		self.actionExport_Concept_to_Json.setIcon(IconFromCurrentTheme("upload-cloud.svg"))
		self.actionExport_Library_to_Json.triggered.connect(lambda:self.ExportToJson(2))
		self.actionExport_Library_to_Json.setIcon(IconFromCurrentTheme("upload-cloud.svg"))
		
		self.actionExport_Diary_to_Markdown.setIcon(IconFromCurrentTheme("upload-cloud.svg"))
		self.actionExport_Diary_to_Markdown.triggered.connect(self.ExportDiaryToMarkdown)


		self.actionCheck_Library.triggered.connect(self.checkLibrary)
		self.actionCheck_Library.setIcon(IconFromCurrentTheme("crosshair.svg"))

		self.actionCheck_Data_Completeness.triggered.connect(self.checkDataCompleteness)
		self.actionCheck_Data_Completeness.setIcon(IconFromCurrentTheme("shield.svg"))
		
		self.actionCheck_Unsaved_Data.triggered.connect(self.checkUnsavedData)
		self.actionCheck_Unsaved_Data.setIcon(IconFromCurrentTheme("git-pull-request.svg"))

		self.actionSave_Data.triggered.connect(lambda:self.Headquarter.saveData(force=True))
		self.actionSave_Data.setIcon(IconFromCurrentTheme("save.svg"))

		self.actionImport_Bookmarks.triggered.connect(self.ImportBookmarks)
		self.actionImport_Bookmarks.setIcon(IconFromCurrentTheme("bookmark.svg"))

		self.actionAdvanced_Search.triggered.connect(self.AdvanceSearch)
		self.actionAdvanced_Search.setIcon(IconFromCurrentTheme("database.svg"))

		self.lineEdit.setAlignment(Qt.AlignHCenter)
		self.lineEdit.returnPressed.connect(lambda:Open_Website(self.lineEdit.text()))
	
	def summon(self, へ_へ, ヘ＿ヘ):
		
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
	
	def ExportToJson(self,index):
		url=os.path.abspath("./Export_Data_%s.json"%WhatDayIsToday(1).toString("yyyyMMdd"))
		res=Json_Save(self.Headquarter.data[index],url)
		if res==True:
			self.Headquarter.app.showMessage("Information", "Data Export Successfully!", DTIcon.Information(), clicked_slot=lambda:Open_Explorer(url, True))
		else:
			self.Headquarter.app.showMessage("Error","Error occured during Data Export!",DTIcon.Error())
	
	def ExportDiaryToMarkdown(self):
		dlg=DTFrame.DTDialog(self,"Export Diary to Markdown")
		
		label=QLabel("Date Range:")
		date_begin=QDateEdit(WhatDayIsToday(1))
		date_begin.setDisplayFormat("yyyy.MM.dd")
		date_end=QDateEdit(WhatDayIsToday(1))
		date_end.setDisplayFormat("yyyy.MM.dd")

		checkbox_caption=QCheckBox("Remove image caption")

		checkbox_epub=QCheckBox("Convert to EPUB")
		def slot():
			if checkbox_epub.isChecked():
				label_yaml.setEnabled(True)
				yaml_edit.setEnabled(True)
				label_extra.setEnabled(True)
				extra_edit.setEnabled(True)
			else:
				label_yaml.setEnabled(False)
				yaml_edit.setEnabled(False)
				label_extra.setEnabled(False)
				extra_edit.setEnabled(False)

		checkbox_epub.stateChanged.connect(slot)
		hh=int(self.Headquarter.app.Font().pointSize()*0.7)
		label_yaml=QLabel("YAML Front Matter:")
		yaml_edit=QPlainTextEdit("""---
title: 
author: 
publisher: 
description: 
cover-image: cover.jpg
---""")
		yaml_edit.setMinimumHeight(hh*7*2)

		label_extra=QLabel("Pandoc Extra Arguments:")
		extra_edit=QLineEdit()
		extra_edit.setText("-c default.css")

		slot()

		layout_H=QHBoxLayout()
		layout_H.setMargin(0)
		layout_H.addWidget(label)
		layout_H.addWidget(date_begin)
		layout_H.addWidget(date_end)
		frame0=QFrame()
		frame0.setLayout(layout_H)

		layout_V=QVBoxLayout()
		layout_V.setMargin(0)
		layout_V.addWidget(checkbox_caption)
		layout_V.addWidget(checkbox_epub)
		layout_V.addWidget(label_yaml)
		layout_V.addWidget(yaml_edit)
		layout_V.addWidget(label_extra)
		layout_V.addWidget(extra_edit)
		frame1=QFrame()
		frame1.setLayout(layout_V)
		frame1.setStyleSheet("font-size:%spt"%hh)

		layout=QVBoxLayout()
		layout.setMargin(0)
		layout.addWidget(frame0)
		layout.addWidget(frame1)
		widget=QWidget()
		widget.setLayout(layout)
		dlg.setCentralWidget(widget)

		dlg.adjustSize()
		MoveToCenterOfScreen(dlg)
		
		from filetype import image_extension
		if dlg.exec_():
			begin=date_begin.date()
			end=date_end.date()

			if begin>end:
				DTFrame.DTMessageBox(self,"Warning","Wrong date range!",DTIcon.Warning())
				return
			
			if checkbox_epub.isChecked():
				text=yaml_edit.toPlainText()+"\n\n"
			else:
				text=""
			
			last_year=None
			last_month=None
			current=QDate(begin)
			while current<=end:
				y,m,d=map(str,QDate_to_Tuple(current))
				
				try:
					day=self.Headquarter.data[0][y][m][d]
					if last_year!=y:
						text+="# %s\n\n"%y
						last_year=y
					if last_month!=m:
						text+="## %s.%s\n\n"%(y,m)
						last_month=m
					text+="### "+QLocale().toString(QDate(int(y),int(m),int(d)),"yyyy.M.d dddd")+"\n\n"
					block=""
					for line in day:
						block+=line["text"]+"\n\n"
						if line["file"]!=[]:
							for file in line["file"]:
								name=file["name"]
								if file["type"]==2:
									block+="> Linked Url\n>\n> [%s](%s)\n\n"%(name,file["url"])
								else:
									url=os.path.join(os.path.abspath(self.Headquarter.library_base+"/").replace("\\","/"),file["url"])
									ext=os.path.splitext(url)[1][1:]
									if file["type"]==0:
										block+="> Linked Folder\n>\n> [%s](%s)\n\n"%(name,url)
									elif file["type"]==1:
										if ext.lower() in image_extension:
											block+="> Linked Image\n>\n> ![%s](%s)\n\n"%(name,url)
										else:
											block+="> Linked File\n>\n> [%s](%s)\n\n"%(name,url)

					if checkbox_caption.isChecked():
						text+=re.sub("(?<=!\[).*?(?=\])","",block)
					else:
						text+=block
				except:
					pass
					
				current=current.addDays(1)
			
			if text=="":
				DTFrame.DTMessageBox(self,"Warning","Nothing exists during %s to %s."%(begin.toString("yyyy.M.d"),end.toString("yyyy.M.d")),DTIcon.Warning())
				return

			dir_dlg=QFileDialog(self,"Select output directory")
			dir=dir_dlg.getExistingDirectory()
			if dir:
				try:
					url=os.path.abspath(dir+"/Diary_%s_%s.md"%(begin.toString("yyyyMMdd"),end.toString("yyyyMMdd")))
					with open(url,"w",encoding="utf-8") as f:
						f.write(text)
					
					if checkbox_epub.isChecked():
						if sys.platform=="win32":
							cmd="start powershell "
							cmd+="chcp 65001;"
							cmd+="pandoc -i %s -o %s -s %s;"%(url, url[:-2]+"epub", extra_edit.text())
							cmd+="pause;"
							os.system(cmd)
						elif sys.platform=="linux":
							cmd="gnome-terminal -- "
							cmd+="pandoc -i %s -o %s -s %s;"%(url, url[:-2]+"epub", extra_edit.text())
							os.system(cmd)
					
					self.Headquarter.app.showMessage("Information", "Diary Export Successfully!", DTIcon.Information(), clicked_slot=lambda:Open_Explorer(url, True))

				except Exception as e:
					DTFrame.DTMessageBox(self,"Error","Error occurs during output!\n\n%s"%e,DTIcon.Error())
	
	def checkLibrary(self):
		
		if not os.path.exists(self.Headquarter.library_base):
			DTFrame.DTMessageBox(self,"Error","Cannot access Library, please check the direction existence!")
			return

		from module import LibraryCheck
		dlg=DTFrame.DTDialog(self,"Library Check")
		# dlg.TitleBar.title_icon.setIcon(QIcon())
		# dlg.TitleBar.title_icon.setText("💩")
		# dlg.TitleBar.title_icon.setStyleSheet("font-size:25pt")
		
		module=LibraryCheck(self.Headquarter)
		dlg.setCentralWidget(module)
		dlg.buttonBox.hide()
		dlg.buttonBoxLayout.setContentsMargins(QMargins(0,0,32,0))

		dlg.adjustSize()
		MoveToCenterOfScreen(dlg)
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

			error="Check Started: %s\n\n"%QLocale().toString(QDateTime().currentDateTime(),"yyyy.M.d hh:mm:ss")
			# error+=str(diary_data)+"\n\n"+str(concept_data)+"\n\n"+str(library_data)+"\n\n"
			# Diary
			error+="------------------------Diary------------------------\n\n"
			for year in diary_data:
				for month in diary_data[year]:
					for day in diary_data[year][month]:
						line_index=0
						for line in diary_data[year][month][day]:
							
							try:
								if type(line["text"])!=str:
									error+="%s.%s.%s line_index:%s text is not str\n"%(year,month,day,line_index)
								if line["text"].strip()=="":
									error+="%s.%s.%s line_index:%s text is EMPTY!\n"%(year,month,day,line_index)
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
			error+="\n\n------------------------Concept------------------------\n\n"
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
					if name.strip()=="":
						error+="concept:%s name:%s is EMPTY\n"%(index,name)
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
			error+="\n\n------------------------Library------------------------\n\n"
			for year in library_data:
				for month in library_data[year]:
					for day in library_data[year][month]:
						for file_name in library_data[year][month][day]:
							
							if type(file_name)!=str:
								error+="%s.%s.%s file_name:%s is not str\n"%(year,month,day,file_name)
							if file_name.strip()=="":
								error+="%s.%s.%s file_name:%s is EMPTY\n"%(year,month,day,file_name)
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
			
			error+="\n\nCheck Finished: %s"%QLocale().toString(QDateTime().currentDateTime(),"yyyy.M.d hh:mm:ss")
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

			if sys.platform=="win32":
				self.DataChecker.TitleBar.btn_close.clicked.disconnect(self.DataChecker.close)
				self.DataChecker.TitleBar.btn_close.clicked.connect(slot)

			self.DataChecker.errorText=QPlainTextEdit(error)
			self.DataChecker.errorText.setReadOnly(True)
			self.DataChecker.setMinimumSize(500,500)
			self.DataChecker.setCentralWidget(self.DataChecker.errorText)
			self.DataChecker.adjustSize()
			MoveToCenterOfScreen(self.DataChecker)
			
		ShowUp(self.DataChecker)

	def checkUnsavedData(self):
		# Could be SLOW if data_size are large, WAIT PATIENTLY!

		from jsondiff import diff
		import pprint
		import deepdiff

		def diff1(old,new):
			return pprint.pformat(diff(old,new,syntax='symmetric'),indent=4,compact=True)
		
		def diff2(old,new):
			return deepdiff.DeepDiff(old,new,ignore_order=True).pretty()

		def check():
			
			old_data=Symmetric_Decrypt_Load(self.Headquarter.password(), os.path.join(self.Headquarter.app.DataDir(),"data.dlcw"), iteration=self.Headquarter.iteration())
			old_diary_data=old_data[0]
			old_concept_data=old_data[1]
			old_library_data=old_data[2]
			
			new_diary_data=self.Headquarter.getDiaryData()
			new_concept_data=self.Headquarter.getConceptData()
			new_library_data=self.Headquarter.getLibraryData()
			
			info=""
			info="Check Started: %s\n\n"%QLocale().toString(QDateTime().currentDateTime(),"yyyy.M.d hh:mm:ss")
			info+="----------Diary Data Difference----------\n\n"+diff1(old_diary_data,new_diary_data)+"\n\n"
			info+="----------Concept Data Difference----------\n\n"+diff2(old_concept_data,new_concept_data)+"\n\n"
			info+="----------Library Data Difference----------\n\n"+diff1(old_library_data,new_library_data)+"\n\n"
			info+="\n\nCheck Finished: %s"%QLocale().toString(QDateTime().currentDateTime(),"yyyy.M.d hh:mm:ss")
			
			return info

		def slot():
			self.DataChecker2.deleteLater()
			del self.DataChecker2
		
		info=check()
		
		try:
			self.DataChecker2.infoText.setPlainText(info)
		except:
			self.DataChecker2=DTFrame.DTMainWindow(self.Headquarter.app)
			self.DataChecker2.initialize()
			self.DataChecker2.setWindowTitle("Check Unsaved Data")

			self.DataChecker2.actionExit.triggered.disconnect(self.DataChecker2.close)
			self.DataChecker2.actionExit.triggered.connect(slot)
			
			if sys.platform=="win32":
				self.DataChecker2.TitleBar.btn_close.clicked.disconnect(self.DataChecker2.close)
				self.DataChecker2.TitleBar.btn_close.clicked.connect(slot)

			self.DataChecker2.infoText=QPlainTextEdit(info)
			self.DataChecker2.infoText.setReadOnly(True)
			self.DataChecker2.setMinimumSize(500,500)
			self.DataChecker2.setCentralWidget(self.DataChecker2.infoText)
			self.DataChecker2.adjustSize()
			MoveToCenterOfScreen(self.DataChecker2)
			
		ShowUp(self.DataChecker2)

	def ImportBookmarks(self):
		def slot():
			del self.bookmark_parser_window
		
		if hasattr(self,"bookmark_parser_window"):
			ShowUp(self.bookmark_parser_window)
			return
		
		from session import BookmarkParserSession
		self.bookmark_parser_window=BookmarkParserSession(self.Headquarter.app,self.Headquarter)
		self.bookmark_parser_window.closed.connect(slot)
		ShowUp(self.bookmark_parser_window)

	def AdvanceSearch(self):
		def slot():
			del self.advance_search_window
		
		if hasattr(self,"advance_search_window"):
			ShowUp(self.advance_search_window)
			return
		
		from session import AdvanceSearchSession
		self.advance_search_window=AdvanceSearchSession(self.Headquarter.app,self.Headquarter)
		self.advance_search_window.closed.connect(slot)
		ShowUp(self.advance_search_window)
