# # --
from DTPySide import *
from DTPySide.DTFrame.DTMainWindow import DTMainWindow
from web_func import *

class LobbySession(DTSession.DTMainSession):
	
	def eventFilter(self, watched: QObject, event:QMouseEvent) -> bool:
		# 为了实现重新focusIn窗体的时候刷新界面，虽然手动把一堆子控件installEventFilter一遍，但也只能这样了
		# focusInEvent和mousePressEvent都试了，都不可能捕获子控件的事件，所以只有点击到TitleBar或者window的空白区域，才可能被触发
		if (event.type()==QEvent.MouseButtonPress and event.button()==Qt.LeftButton) or event.type()==QEvent.FocusIn:
			# print(watched)
			# if hasattr(self.lobby,"DataChecker"):
			# 	self.lobby.checkDataCompleteness()
			if self.WindowFocusing()!=self:
				self.setWindowFocusing(self)
				# print("Now focused in",self.WindowFocusing())
		return False # 这里是让继续延续event的处理，不要被filter掉了

	def __init__(self, app):
		super().__init__(app)
		self.__WindowFocusing=None #记录点击的window，如果focus的window改变，对应被focusIn的window就要刷新画面
		self.qlock=QMutex(QMutex.NonRecursive)
	
	def WindowFocusing(self):
		return self.__WindowFocusing
	
	def setWindowFocusing(self,which:DTMainWindow):
		self.__WindowFocusing=which
	
	def loadData(self):
		data_dir=os.path.join(self.app.DataDir(),"data.dlcw")
		if os.path.exists(data_dir):
			self.data=Fernet_Decrypt_Load(self.password(),data_dir)
			if self.data==False:
				DTFrame.DTMessageBox(self,"Error","Data error!")
				self.app.quit()
			
		else:
			self.data=[{},[],{}]
			Fernet_Encrypt_Save(self.password(),self.data,data_dir)

		if os.path.exists("cache"):
			self.cache=Fernet_Decrypt_Load(self.password(),os.path.abspath("cache"))
			if self.cache==False:
				DTFrame.DTMessageBox(self,"Error","Cache data error!")
				self.app.quit()
		else:
			self.cache={}
			Fernet_Encrypt_Save(self.password(),self.cache,os.path.abspath("cache"))
			
		if os.path.exists("confreq"):
			self.concept_frequency=Fernet_Decrypt_Load(self.password(),os.path.abspath("confreq"))
			if self.concept_frequency==False:
				DTFrame.DTMessageBox(self,"Error","Concept Frequency data error!")
				self.app.quit()
		else:
			self.concept_frequency={}
			Fernet_Encrypt_Save(self.password(),self.concept_frequency,os.path.abspath("confreq"))
		
		self.library_base=Fernet_Decrypt(self.password(),self.UserSetting().value("LibraryBase"))
		if self.library_base==False:
			dlg=QFileDialog(self)
			while not self.library_base:
				DTFrame.DTMessageBox(self,"Information","You need to set Library Base first!",DTIcon.Information())
				self.library_base=dlg.getExistingDirectory()
			self.UserSetting().setValue("LibraryBase",Fernet_Encrypt(self.password(),self.library_base))
	
	def dataValidityCheck(self):
		return True
	
	def initializeWindow(self):
		super().initializeWindow()

		from module import Lobby
		self.lobby=Lobby(self)
		self.setCentralWidget(self.lobby)
		
		from session.DiarySession import DiarySession
		self.diary_heap=[]
		diary=DiarySession(self.app,self)
		diary.initialize()
		self.diary_heap.append(diary)

		from session.ConceptSession import ConceptSession
		self.concept_heap=[]
		concept=ConceptSession(self.app,self)
		concept.initialize()
		self.concept_heap.append(concept)

		from session.LibrarySession import LibrarySession
		self.library_heap=[]
		library=LibrarySession(self.app,self)
		library.initialize()
		self.library_heap.append(library)

	def restoreWindowStatus(self):
		try:
			self.resize(self.UserSetting().value("WindowStatus/LobbySize"))
			self.move(self.UserSetting().value("WindowStatus/LobbyPos"))
		except:
			self.resize(self.minimumWidth(),self.minimumHeight())
			self.adjustSize()
			MoveToCenterOfScreen(self)

	def initializeSignal(self):
		super().initializeSignal()
		self.installEventFilter(self)
		self.refreshModuleSingal()
		self.addAction(self.lobby.actionSave_Data)
		self.addAction(self.lobby.actionCheck_Data_Completeness)
		self.addAction(self.lobby.actionCheck_Unsaved_Data)


		# 全局快捷键
		self.actionBoss_Key.setShortcutContext(Qt.ApplicationShortcut)
	
	def initializeMenu(self):

		menuDataSecurity=QMenu(QCoreApplication.translate("Lobby","Data Security"),self)
		menuDataSecurity.setIcon(IconFromCurrentTheme("shield.svg"))
		menuDataSecurity.addAction(self.lobby.actionCheck_Library)
		menuDataSecurity.addAction(self.lobby.actionCheck_Data_Completeness)
		menuDataSecurity.addAction(self.lobby.actionCheck_Unsaved_Data)
		self.addMenuToMainMenu(menuDataSecurity)

		menuDataTransfer=QMenu(QCoreApplication.translate("Lobby","Data Transfer"),self)
		menuDataTransfer.setIcon(IconFromCurrentTheme("send.svg"))
		menuDataTransfer.addAction(self.lobby.actionExport_Diary_to_Json)
		menuDataTransfer.addAction(self.lobby.actionExport_Diary_to_Markdown)
		menuDataTransfer.addAction(self.lobby.actionExport_Concept_to_Json)
		menuDataTransfer.addAction(self.lobby.actionExport_Library_to_Json)
		menuDataTransfer.addAction(self.lobby.actionImport_Bookmarks)
		menuDataTransfer.addAction(self.lobby.actionAdvanced_Search)
		self.addMenuToMainMenu(menuDataTransfer)
		
		self.addActionToMainMenu(self.lobby.actionSave_Data)
		super().initializeMenu()

	
	def refreshModuleSingal(self):
		"""模块间交互的信号与槽
		"""

		def slot(id):
			"""diary、library的concept列表点击concept，在所有可见的concept中showConcept

			Args:
				id (int): ConceptId
			"""
			flag=False
			for concept in self.concept_heap:
				if concept.isVisible()==True:
					flag=True
					ShowUp(concept)
					concept.concept_module.showConcept(id)
			#如果全部都隐藏着，开启一个
			if flag==False:
				ShowUp(self.concept_heap[0])
				self.concept_heap[0].concept_module.showConcept(id)
		
		def slot2(line):
			"""concept、Library的text列表点击line，在所有可见的diary中showDay和showLine

			Args:
				line (dict): 从textList中传出来的标准line字典
			"""
			y=line["y"]
			m=line["m"]
			d=line["d"]
			index=line["index"]

			flag=False
			for diary in self.diary_heap:
				if diary.isVisible()==True:
					flag=True
					ShowUp(diary)
					diary.diary_module.showDay(QDate(y,m,d))
					diary.diary_module.textList.clearSelection()
					diary.diary_module.textList.setCurrentRow(index)
					diary.diary_module.showLine()
			#如果全部都隐藏着，开启一个
			if flag==False:
				ShowUp(self.diary_heap[0])
				self.diary_heap[0].diary_module.showDay(QDate(y,m,d))
				self.diary_heap[0].diary_module.textList.clearSelection()
				self.diary_heap[0].diary_module.textList.setCurrentRow(index)
				self.diary_heap[0].diary_module.showLine()

		for diary in self.diary_heap:
			diary.diary_module.conceptTable.conceptDoubleClicked.connect(slot)
		
		for library in self.library_heap:
			library.library_module.conceptTable.conceptDoubleClicked.connect(slot)
			library.library_module.textList.textClicked.connect(slot2)
		
		for concept in self.concept_heap:
			concept.concept_module.textList.textClicked.connect(slot2)

	def saveWindowStatus(self):
		self.UserSetting().setValue("WindowStatus/LobbySize",self.size())
		self.UserSetting().setValue("WindowStatus/LobbyPos",self.pos())
		self.UserSetting().setValue("WindowStatus/DiarySize",self.diary_heap[0].size())
		self.UserSetting().setValue("WindowStatus/DiaryPos",self.diary_heap[0].pos())
		self.UserSetting().setValue("WindowStatus/ConceptSize",self.concept_heap[0].size())
		self.UserSetting().setValue("WindowStatus/ConceptPos",self.concept_heap[0].pos())
		self.UserSetting().setValue("WindowStatus/LibrarySize",self.library_heap[0].size())
		self.UserSetting().setValue("WindowStatus/LibraryPos",self.library_heap[0].pos())

	def saveData(self,force=False):
		
		try:
			data_dir=os.path.join(self.app.DataDir(),"data.dlcw")
			Fernet_Encrypt_Save(self.password(), self.data, data_dir)
			Fernet_Encrypt_Save(self.password(), self.cache, os.path.abspath("cache"))
			Fernet_Encrypt_Save(self.password(), self.concept_frequency, os.path.abspath("confreq"))
			if force==True:
				self.app.showMessage("Information","Data Saved Successfully!",DTIcon.Information(),clicked_slot=lambda:os.popen("explorer /select,\"%s\""%os.path.abspath(data_dir)))
		except Exception as e:
			self.app.showMessage("Error","Error occured during Data Saving!\n\n%s"%e,DTIcon.Error())

	def saveAllEncryptData(self):
		super().saveAllEncryptData()
		self.saveData()
		self.UserSetting().setValue("LibraryBase",Fernet_Encrypt(self.password(),self.library_base))
	
	def backup(self):
		self.saveData()
		super().backup()

	def setting(self):
		
		from session.SettingSession import SettingSession
		dlg=SettingSession(self,self.app)
		dlg.exec_()

	def bossComing(self):
		for diary in self.diary_heap:
			diary.hide()
		for concept in self.concept_heap:
			concept.hide()
		for library in self.library_heap:
			library.hide()
		
		if hasattr(self.lobby,"DataChecker"):
			self.lobby.DataChecker.hide()
		if hasattr(self.lobby,"DataChecker2"):
			self.lobby.DataChecker2.hide()
		if hasattr(self.lobby,"bookmark_parser_window"):
			self.lobby.bookmark_parser_window.hide()
		if hasattr(self.lobby,"advance_search_window"):
			self.lobby.advance_search_window.hide()
		
		super().bossComing()


	#################################################################

	def getDiaryData(self):
		return self.data[0]

	def getDiaryDay(self, date:QDate):
		"""获取一日的diary_data，若存在则返回该日字典，若不存在则返回None

		Args:
			date (QDate): 要读取的日期

		Returns:
			[type]: 该日的diary_data字典
		"""

		year, month, day= map(str, QDate_to_Tuple(date))
		try:
			return self.data[0][year][month][day]
		except:
			return None
	
	def getRandomDiaryDate(self):
		import random
		y=random.choice(list(self.data[0].keys()))
		m=random.choice(list(self.data[0][y].keys()))
		d=random.choice(list(self.data[0][y][m].keys()))
		return QDate(int(y),int(m),int(d))

	def getDiaryDayLine(self, date:QDate, index:int):
		year, month, day= map(str, QDate_to_Tuple(date))
		try:
			return self.data[0][year][month][day][index]
		except:
			return None
	
	def getDiaryDayLineTooltip(self, date:QDate, index:int):
		line=self.getDiaryDayLine(date, index)
		tooltip=f"""Concept: {", ".join([self.getConcept(i)["name"] for i in line["concept"]])}"""
		return tooltip

	def deleteDiaryDayLine(self, day:QDate, delete_index_list):
		y,m,d=map(str,QDate_to_Tuple(day))
		day_data=self.getDiaryDay(day)
		self.data[0][y][m][d]=[day_data[index] for index in range(len(day_data)) if index not in delete_index_list]
		
		if len(self.data[0][y][m][d])==0:
			self.data[0][y][m].pop(d)
			
			if len(self.data[0][y][m])==0:
				self.data[0][y].pop(m)
				
				if len(self.data[0][y])==0:
					self.data[0].pop(y)
		
	def getDiaryLineList(self,search_list=[],date_range_list=[],concept_name_list=[],rank=False):
		
		def add_all_lines():
			for year in self.data[0]:
				for month in self.data[0][year]:
					for day in self.data[0][year][month]:
						index=0
						for line in self.data[0][year][month][day]:
							line_list.append({
								"y":int(year),
								"m":int(month),
								"d":int(day),
								"text":line["text"],
								"concept":line["concept"],
								"file":line["file"],
								"index":index,
								"rank":0
							})
							index+=1
							
			
		def add_line_in_dates(begin:QDate,end:QDate=None):
			if end==None:
				end=QDate(begin)

			# 因为Diary Data的dict是排好序的，就可以最直接遍历了
			for year in self.data[0]:
				for month in self.data[0][year]:
					for day in self.data[0][year][month]:
						current_date=QDate(int(year),int(month),int(day))
						if begin<=current_date<=end:
							index=0
							for line in self.data[0][str(year)][str(month)][str(day)]:
								line_list.append({
									"y":int(year),
									"m":int(month),
									"d":int(day),
									"text":line["text"],
									"concept":line["concept"],
									"file":line["file"],
									"index":index,
									"rank":0
								})
								index+=1
		
		def namelist_in_text(text):
			# 判断文本是否包含搜索列表中的所有元素，如果全部包含则返回非零值（True），否则返回0（False）
			return not len([i for i in search_list if i not in text.lower()])
		
		line_list=[]
		if date_range_list==[]:
			add_all_lines()
		else:
			for date_range in date_range_list:
				if type(date_range)==tuple:
					add_line_in_dates(*date_range)
				else:
					add_line_in_dates(date_range)
		
		if concept_name_list==None:
			# 搜索没有链接concept的内容
			line_list=[line for line in line_list if line["concept"]==[] ]
		elif concept_name_list!=[]:
			if rank==True:
				new_list=[]
				for line in line_list:
					if List_Difference(concept_name_list,[self.data[1][id]["name"].lower() for id in line["concept"]])==[]:
						line["rank"]=len(List_Intersection(concept_name_list,[self.data[1][id]["name"].lower() for id in line["concept"]]))*2
						new_list.append(line)
				line_list=new_list
			else:
				line_list=[line for line in line_list if List_Difference(concept_name_list,[self.data[1][id]["name"].lower() for id in line["concept"]])==[] ]
		
		if search_list!=[]:
			if rank==True:
				new_list=[]
				for line in line_list:
					text=line["text"]
					if namelist_in_text(text):
						line["rank"]+=sum( [ text.lower().count(i) for i in search_list if i in text.lower()] )
						new_list.append(line)
				line_list=new_list
			else:
				line_list=[line for line in line_list if namelist_in_text(line["text"])]

		if rank==True:
			line_list=sorted(line_list,key=lambda x:x["rank"],reverse=True)
		return line_list

	def addDiaryDay(self, date:QDate):
		"""在diary_data中创建对应date的列表容器，并返回该列表容器

		Args:
			date (QDate): 要创建的日期

		Returns:
			[type]: 返回该列表容器
		"""

		year, month, day= map(str, QDate_to_Tuple(date))
		
		if self.data[0].get(year)==None:
			self.data[0][year]={}
			self.data[0]=dict(sorted(self.data[0].items(),key=lambda x:int(x[0])))
		
		if self.data[0][year].get(month)==None:
			self.data[0][year][month]={}
			self.data[0][year]=dict(sorted(self.data[0][year].items(),key=lambda x:int(x[0])))
		
		if self.data[0][year][month].get(day)==None:
			self.data[0][year][month][day]=[]
			self.data[0][year][month]=dict(sorted(self.data[0][year][month].items(),key=lambda x:int(x[0])))
		
		return self.data[0][year][month][day]
	
	#################################################################

	def getConceptData(self):
		return self.data[1]

	def getConcept(self, id:int):
		"""获取指定的concept，若存在则返回该concept字典，若不存在则返回None

		Args:
			id (int): 要读取的concept

		Returns:
			[type]: 该concept的字典
		"""
		try:
			return self.data[1][id]
		except:
			return None
	
	def getConceptTooltip(self, id:int):
		concept=self.getConcept(id)
		tooltip=f"""ID: {concept["id"]}
Name: {concept["name"]}
Detail: {concept["detail"] if len(concept["detail"])<20 else concept["detail"][:20]+"..."}
Parent: {", ".join([self.getConcept(i)["name"] for i in concept["parent"]])}
Child: {", ".join([self.getConcept(i)["name"] for i in concept["child"]])}
Relative: {", ".join([self.getConcept(i)["name"] for i in concept["relative"]])}"""
		return tooltip
	
	def getConceptIDList(self,search:str,rank=False):
		id_list=[]
		if search=="\^p":
			# no parent
			id_list=[concept["id"] for concept in self.data[1] if concept["parent"]==[] ]
		elif search=="\^c":
			# no child
			id_list=[concept["id"] for concept in self.data[1] if concept["child"]==[] ]
		elif search=="\^pc" or search=="\^cp":
			# no parent and no child
			id_list=[concept["id"] for concept in self.data[1] if concept["parent"]==[] and concept["child"]==[] ]
		else:
			for concept in self.data[1]:
				if search in concept["name"] or search.lower() in concept["az"] or search.lower() in concept["detail"].lower() or search.lower() in Str_to_AZ(concept["detail"]):
					id_list.append(concept["id"])
		
		# 用concept_frequency记录的频度排序
		if rank==True:
			chosen={}
			new_id_list=id_list.copy()
			for i in id_list:
				if i in self.concept_frequency.keys():
					new_id_list.remove(i)
					chosen[i]=self.concept_frequency[i]
			chosen=sorted(chosen.items(),key=lambda x:x[1],reverse=True)
			id_list=[i[0] for i in chosen]+new_id_list
		
		return id_list

	def appendConcept(self):
		"""在concept_data中append concept字典容器，返回该字典容器

		Returns:
			[type]: 返回该字典容器
		"""
		self.data[1].append({
			"id": len(self.data[1]),
			"name": "",
			"detail": "", 
			"parent": [],
			"child": [],
			"relative": [],
			"az": "",
			"file": [],
		})
		return self.data[1][-1]
	
	def deleteConcept(self,delete_id_list:list):
		
		def CalcNewID(id): # 计算前移后的id
			offset=0
			for delete_id in delete_id_list:
				if id < delete_id:
					return id-offset
				else:
					offset+=1
			return id-offset
		
		def Bake_ID_List(raw_list:list): #把raw_list，先剔除delete_id_list中的id，再改需要前移的id
			baked_list=[]
			for id in List_Difference(raw_list,delete_id_list):
				baked_list.append(New_ID_Dict[id])
			return baked_list
		
		delete_id_list=sorted(delete_id_list)
		
		New_ID_Dict={} # 存储 原id 以及 对应的前移id
		for i in range(len(self.data[1])):
			New_ID_Dict[i]=CalcNewID(i)
		
		# Diary链接的concept中，剔除delete_id_list中的id，并且改需要前移的id
		for year in self.data[0]:
			for month in self.data[0][year]:
				for day in self.data[0][year][month]:
					for line in self.data[0][year][month][day]:
						line["concept"]=Bake_ID_List(line["concept"])

		# Library链接的concept中，剔除delete_id_list中的id，并且改需要前移的id
		for year in self.data[2]:
			for month in self.data[2][year]:
				for day in self.data[2][year][month]:
					for file in self.data[2][year][month][day]:
						file=self.data[2][year][month][day][file]
						file["concept"]=Bake_ID_List(file["concept"])

		# 还是别在for循环中用remove或者pop了，太麻烦了，这样一句话就完事，运算效率还高
		self.data[1]=[concept for concept in self.data[1] if concept["id"] not in delete_id_list]

		# Concept中改需要前移的id
		for concept in self.data[1]:
			concept["id"]=New_ID_Dict[concept["id"]]
			concept["parent"]=Bake_ID_List(concept["parent"])
			concept["child"]=Bake_ID_List(concept["child"])
			concept["relative"]=Bake_ID_List(concept["relative"])
		
		# 改concept_frequency中的id
		new_concept_frequency={}
		for id in self.concept_frequency.keys():
			if id not in delete_id_list:
				new_concept_frequency[New_ID_Dict[id]]=self.concept_frequency[id]
		self.concept_frequency=new_concept_frequency

		# 改concept_history_queue中的id
		for i in range(len(self.concept_heap)):
			new_history=[]
			for id in self.concept_heap[i].concept_module.concept_history_queue:
				if id not in delete_id_list:
					new_history.append(New_ID_Dict[id])
			self.concept_heap[i].concept_module.concept_history_queue=new_history

	def addParent(self,concept_id,parent_id_list):
		concept=self.data[1][concept_id]
			
		for parent_id in List_Difference(parent_id_list,concept["parent"]):
			
			# 禁止自生
			if parent_id==concept_id:
				DTFrame.DTMessageBox(self,"Information","Are you kidding?",DTIcon.Holo01())
				continue

			# 禁止隔一辈的乱伦，隔数辈的允许组成有向图
			if parent_id in concept["child"]:
				DTFrame.DTMessageBox(self,"Information","%s is already %s's child."%(self.data[1][parent_id]["name"],self.data[1][concept_id]["name"]),DTIcon.Information())
				continue
			
			concept["parent"].append(parent_id)
			if concept_id not in self.data[1][parent_id]["child"]:
				self.data[1][parent_id]["child"].append(concept_id)
			else:
				# 数据错误
				DTFrame.DTMessageBox(self,"Error","Error occured during adding parent!\n\n%s is already %s's child."%(concept_id,parent_id),DTIcon.Error())
	
	def addChild(self,concept_id,child_id_list):
		concept=self.data[1][concept_id]
			
		for child_id in List_Difference(child_id_list,concept["child"]):
			
			# 禁止自生
			if child_id==concept_id:
				DTFrame.DTMessageBox(self,"Information","Are you kidding?",DTIcon.Holo01())
				continue

			# 禁止隔一辈的乱伦，隔数辈的允许组成有向图
			if child_id in concept["parent"]:
				DTFrame.DTMessageBox(self,"Information","%s is already %s's parent."%(self.data[1][child_id]["name"],self.data[1][concept_id]["name"]),DTIcon.Information())
				continue
			
			concept["child"].append(child_id)
			if concept_id not in self.data[1][child_id]["parent"]:
				self.data[1][child_id]["parent"].append(concept_id)
			else:
				# 数据错误
				DTFrame.DTMessageBox(self,"Error","Error occured during adding child!\n\n%s is already %s's parent."%(concept_id,child_id),DTIcon.Error())

	def addRelative(self,concept_id,relative_id_list):
		concept=self.data[1][concept_id]
		
		for relative_id in List_Difference(relative_id_list,concept["relative"]):
			
			# 禁止自交
			if relative_id==concept_id:
				DTFrame.DTMessageBox(self,"Information","That's not a good idea.",DTIcon.Holo01())
				continue

			concept["relative"].append(relative_id)
			if concept_id not in self.data[1][relative_id]["relative"]:
				self.data[1][relative_id]["relative"].append(concept_id)
			else:
				# 数据错误
				DTFrame.DTMessageBox(self,"Error","Error occured during adding relative!\n\n%s is already %s's relative."%(concept_id,relative_id),DTIcon.Error())
	
	def deleteParent(self,concept_id,delete_id_list):
		concept=self.getConcept(concept_id)
		concept["parent"]=List_Difference(concept["parent"],delete_id_list)
		
		for id in delete_id_list:
			self.getConcept(id)["child"].remove(concept_id)
	
	def deleteChild(self,concept_id,delete_id_list):
		concept=self.getConcept(concept_id)
		concept["child"]=List_Difference(concept["child"],delete_id_list)
		
		for id in delete_id_list:
			self.getConcept(id)["parent"].remove(concept_id)

	def deleteRelative(self,concept_id,delete_id_list):
		concept=self.getConcept(concept_id)
		concept["relative"]=List_Difference(concept["relative"],delete_id_list)
		
		for id in delete_id_list:
			self.getConcept(id)["relative"].remove(concept_id)

	#################################################################

	def getLibraryData(self):
		return self.data[2]

	def getLibraryFile(self,date:QDate,name):
		year, month, day= map(str, QDate_to_Tuple(date))
		try:
			return self.data[2][year][month][day][name]
		except:
			return None
	
	def getLibraryFileTooltip(self,date:QDate,name):
		file=self.getLibraryFile(date,name)
		backslash_char = "\\"
		tooltip=f"""{os.path.join(self.library_base, file["url"]).replace(backslash_char,"/") if file["type"]!=2 else file["url"]}
Type: {file["type"]}
Concept: {", ".join([self.getConcept(i)["name"] for i in file["concept"]])}"""
		return tooltip

	def getLibraryFileList(self,name_list=[],date_range_list=[],concept_name_list=[],TYPE=None):
		
		def add_all_files():
			for y in self.data[2]:
				for m in self.data[2][y]:
					for d in self.data[2][y][m]:
						for file_name,file in self.data[2][y][m][d].items():
							file_list.append({
								"y":int(y),
								"m":int(m),
								"d":int(d),
								"type":file["type"],
								"name":file_name,
								"url":file["url"],
								"concept":file["concept"]
							})
							

		def add_file_in_dates(begin:QDate,end:QDate=None):
			if end==None:
				end=QDate(begin)

			# 因为Library Data的dict是排好序的，就可以最直接遍历了
			for y in self.data[2]:
				for m in self.data[2][y]:
					for d in self.data[2][y][m]:
						current_date=QDate(int(y),int(m),int(d))
						if begin<=current_date<=end:
							for file_name,file in self.data[2][str(y)][str(m)][str(d)].items():
								file_list.append({
									"y":int(y),
									"m":int(m),
									"d":int(d),
									"type":file["type"],
									"name":file_name,
									"url":file["url"],
									"concept":file["concept"]
								})
		
		def namelist_in_filename(file_name):
			# 判断文件名是否包含搜索name列表中的所有元素，如果全部包含则返回非零值（True），否则返回0（False）
			return not len([i for i in name_list if i not in file_name.lower() and i not in Str_to_AZ(file_name)])
		
		file_list=[]
		if date_range_list==[]:
			add_all_files()
		else:
			for date_range in date_range_list:
				if type(date_range)==tuple:
					add_file_in_dates(*date_range)
				else:
					add_file_in_dates(date_range)

		if TYPE!=None:
			file_list=[file for file in file_list if file["type"]==TYPE ]
		
		if concept_name_list==None:
			# 搜索没有链接concept的内容
			file_list=[file for file in file_list if file["concept"]==[] ]
		elif concept_name_list!=[]:			
			file_list=[file for file in file_list if List_Difference(concept_name_list,[self.data[1][id]["name"].lower() for id in file["concept"]])==[] ]
		
		if name_list!=[]:
			file_list=[file for file in file_list if namelist_in_filename(file["name"])]

		return file_list

	def addLibraryFile(self, date:QDate, url:str, concept:list, move_from_outside=True):
		# 他奶奶的，这里concept本来写成了默认参数, concept:list=[]，
		# 然后又在Library的addFile的循环中调用的时候在这个参数的空什么都没写（其他几个地方如果为空倒是写了）
		# 然后在addFile的循环中，这个[]的地址就一直没变，
		# 就算你多次拖、改日期改年份拖，进来的时候，这里的[]的地址一直都是最初def这个函数时创建的那个地址，
		# 然后就他妈的，对一个文件的concept进行操作，其他几个都他妈"瞬间"同化，
		# （试了上一版本的程序也出错，可以明明记得之前测试的时候，这么基本的操作没有bug的）。
		# 两个多小时摸不着头脑，还以为灵异事件见鬼了电脑坏掉了，结果是你丫Python的狗屎特性
		"如果是file类型，url为原始地址；如果是link类型，url为网站地址"
		y, m, d= map(str, QDate_to_Tuple(date))
		
		# BookmarkParser来的标准型filedict，就不用去获取网页title了，ymd也不是当日，而是收藏夹中的日期
		if type(url)==dict:
			file=url
			y=str(file["y"])
			m=str(file["m"])
			d=str(file["d"])
			TYPE=2
			name=file["name"]
			url=file["url"]
			try:
				self.data[2][y][m][d][name]
				already_have=True
			except:
				already_have=False

			if already_have:
				warning="Already have web page or file named %s in %s.%s.%s,\n\nwhich url is %s\n\nYou want to add still?"%(name,y,m,d,self.data[2][y][m][d].get(name)["url"])
				dlg=DTFrame.DTConfirmBox(self,"Warning",warning,DTIcon.Warning())
				if dlg.exec_():
					name=name+str(time.time_ns())
				else:
					return None

		elif url[:8]=="file:///":
			if os.path.isdir(url[8:]):
				TYPE=0 # folder=0
			else:
				TYPE=1 # file=1
			old_dir=url[8:]
			name=os.path.basename(old_dir)

			try:
				# link名字和文件夹名相同
				if self.data[2][y][m][d].get(name)!=None:
					DTFrame.DTMessageBox(self,"Warning","Already exsist %s in %s.%s.%s"%(name,y,m,d),DTIcon.Warning())
					return None
			except:
				pass

			# 禁止从library_base层添加文件
			if self.library_base in os.path.dirname(old_dir) and move_from_outside:
				if self.extractFileURL(os.path.dirname(old_dir)).count("/")<=2:
					DTFrame.DTMessageBox(self,"Error","Do not add file from library_base",DTIcon.Warning())
					return None

			url="%s/%s/%s/%s"%(y,m,d,name)
			new_dir=os.path.join(self.library_base,url)
			try:
				new_base=os.path.dirname(new_dir) # 日期文件夹路径
				
				# 创建日期文件夹
				if not os.path.exists(new_base):
					os.makedirs(new_base)
				
				# 检查日期文件夹中是否已存在同名文件
				if name in os.listdir(new_base) and move_from_outside:
					DTFrame.DTMessageBox(self,"Error","%s already exsit in %s!"%(name,new_base),DTIcon.Warning())
					return None
				
				# 移动
				if move_from_outside:
					Win32_Shellmove(old_dir,new_dir)
			
			except Exception as e:
				# 出错
				DTFrame.DTMessageBox(self,"Error",str(e),DTIcon.Warning())
				return None
		else:
			TYPE=2 # link=2
			res=GetWebPageResponse(url)
			if res!=None:
				
				# 浏览器拖图片
				# Yandex浏览器的图片拖出来，附带的url不是临时文件地址，这里就手动下载好了
				if "image" in res.headers["Content-Type"]:
					try:
						TYPE=res.headers["Content-Type"].split("/")[1]
						img=res.content
						# 在根目录生成临时文件
						temp_file_url=os.path.join(os.getcwd(),"%s.%s"%(time.time_ns(),TYPE))
						with open(temp_file_url,"wb") as f:
							f.write(img)
						return self.addLibraryFile(date,"file:///"+temp_file_url,concept)
					except Exception as e:
						DTFrame.DTMessageBox(self,"Error",str(e),DTIcon.Warning())
						return None
				
				# 普通网页
				else:
					html=res.text
					try:
						tree=etree.HTML(html)
						title=tree.xpath(".//title/text()")[0]
						title=urllib.parse.unquote(title,'utf-8')
						name=str(title)

						try:
							self.data[2][y][m][d][name]
							already_have=True
						except:
							already_have=False

						if already_have:
							warning="Already have web page or file named %s in %s.%s.%s,\n\nwhich url is %s\n\nYou want to add still?"%(name,y,m,d,self.data[2][y][m][d].get(name)["url"])
							dlg=DTFrame.DTConfirmBox(self,"Warning",warning,DTIcon.Warning())
							if dlg.exec_():
								name=name+str(time.time_ns())
							else:
								return None
					except:
						DTFrame.DTMessageBox(self,"Warning",str(res),DTIcon.Warning())
						name="Unknow%s"%time.time_ns()
			else:
				DTFrame.DTMessageBox(self,"Warning","Failed to fetch %s"%url,DTIcon.Warning())
				name="Unknow%s"%time.time_ns()

		if self.data[2].get(y)==None:
			self.data[2][y]={}
			self.data[2]=dict(sorted(self.data[2].items(),key=lambda x:int(x[0])))
		
		if self.data[2][y].get(m)==None:
			self.data[2][y][m]={}
			self.data[2][y]=dict(sorted(self.data[2][y].items(),key=lambda x:int(x[0])))
		
		if self.data[2][y][m].get(d)==None:
			self.data[2][y][m][d]={}

		self.data[2][y][m][d][name]={
			"type": TYPE,
			"concept": concept,
			"url": url
		}
		
		self.data[2][y][m]=dict(sorted(self.data[2][y][m].items(),key=lambda x:int(x[0])))

		return name,self.data[2][y][m][d][name]
	
	def renameLibraryFile(self,date:QDate,old_name,new_name,rename_operation=True,new_file_type=None,new_date=None):
		y, m, d= map(str, QDate_to_Tuple(date))
		if old_name==new_name and new_date==None:
			return False
		
		if new_date==None:
			new_y, new_m, new_d= map(str, QDate_to_Tuple(date))
		else:
			new_y, new_m, new_d= map(str, QDate_to_Tuple(new_date))
		
		try:
			if self.data[2][new_y][new_m][new_d].get(new_name)!=None:
				DTFrame.DTMessageBox(self,"Warning","Alreay have file in %s.%s.%s named %s"%(new_y,new_m,new_d,new_name))
				return False
		except:
			pass

		old_file=self.data[2][y][m][d][old_name]
		old_file_type=old_file["type"]

		old_url=old_file["url"]
		if old_file["type"]!=2:
			new_url="%s/%s/%s/%s"%(new_y,new_m,new_d,new_name)
		else:
			new_url=old_url

		if old_file["type"]!=2 and rename_operation==True and old_name!=new_name:
			try:
				os.rename(os.path.join(self.library_base,old_url),os.path.join(self.library_base,new_url))
			except Exception as e:
				DTFrame.DTMessageBox(self,"Error",str(e),DTIcon.Error())
				return False
		
		old_cache_name=date.toString("yyyyMMdd")+old_name
		if new_date==None:
			new_cache_name=date.toString("yyyyMMdd")+new_name
		else:
			new_cache_name=new_date.toString("yyyyMMdd")+new_name
		if self.cache.get(old_cache_name)!=None:
			cache=self.cache[old_cache_name]
			del self.cache[old_cache_name]
			self.cache[new_cache_name]=cache

		new_file=old_file
		new_file["url"]=new_url
		if new_file_type!=None:
			new_file["type"]=new_file_type
		del self.data[2][y][m][d][old_name]

		# 臭狗屎
		if new_date!=None:
			if self.data[2].get(new_y)==None:
				self.data[2][new_y]={}
				self.data[2]=dict(sorted(self.data[2].items(),key=lambda x:int(x[0])))
			
			if self.data[2][new_y].get(new_m)==None:
				self.data[2][new_y][new_m]={}
				self.data[2][new_y]=dict(sorted(self.data[2][new_y].items(),key=lambda x:int(x[0])))
			
			if self.data[2][new_y][new_m].get(new_d)==None:
				self.data[2][new_y][new_m][new_d]={}

			self.data[2][new_y][new_m][new_d][new_name]=new_file

			self.data[2][new_y][new_m]=dict(sorted(self.data[2][new_y][new_m].items(),key=lambda x:int(x[0])))
		else:
			self.data[2][new_y][new_m][new_d][new_name]=new_file
		
		old_file={
			"y":int(y),
			"m":int(m),
			"d":int(d),
			"type":old_file_type,
			"name":old_name,
			"url":old_url
		}

		# 重命名diary line链接的file
		for year in self.data[0]:
			for month in self.data[0][year]:
				for day in self.data[0][year][month]:
					for line in self.data[0][year][month][day]:
						if old_file in line["file"]:
							file=line["file"][line["file"].index(old_file)]
							file["y"]=int(new_y)
							file["m"]=int(new_m)
							file["d"]=int(new_d)
							file["name"]=new_name
							file["url"]=new_url
							if new_file_type!=None:
								file["type"]=new_file_type
		
		# 重命名Concept链接的file
		for concept in self.data[1]:
			if old_file in concept["file"]:
				file=concept["file"][concept["file"].index(old_file)]
				file["y"]=int(new_y)
				file["m"]=int(new_m)
				file["d"]=int(new_d)
				file["name"]=new_name
				file["url"]=new_url
				if new_file_type!=None:
					file["type"]=new_file_type
	
	def deleteLibraryFile(self, delete_file_list, delete_operation=True):
		"""删除多个LibraryFile

		Args:
			delete_file_list (list): 元素为diary line["file"]和concept["file"]的字典标准型（包含y,m,d,type,name,url）
		"""
		success_deleted_file=[]
		for file in delete_file_list:
			year=str(file["y"])
			month=str(file["m"])
			day=str(file["d"])
			name=file["name"]
			url=file["url"]

			if file["type"]!=2 and delete_operation==True:
				try:
					res=Delete_to_Recyclebin(os.path.join(self.library_base,url))
					if res==False:
						DTFrame.DTMessageBox(self,"Error","Failed to delete %s"%name,DTIcon.Warning())
						continue
					else:
						success_deleted_file.append(file)
						del self.data[2][year][month][day][name]
						cache_name=QDate(int(year),int(month),int(day)).toString("yyyyMMdd")+name
						if self.cache.get(cache_name)!=None:
							del self.cache[cache_name]

				except Exception as e:
					# 出错
					DTFrame.DTMessageBox(self,"Error",str(e),DTIcon.Warning())
					continue
			else:
				del self.data[2][year][month][day][name]
				cache_name=QDate(int(year),int(month),int(day)).toString("yyyyMMdd")+name
				if self.cache.get(cache_name)!=None:
					del self.cache[cache_name]
				success_deleted_file.append(file)

		# 删除Diary链接的file
		for year in self.data[0]:
			for month in self.data[0][year]:
				for day in self.data[0][year][month]:
					for line in self.data[0][year][month][day]:
						line["file"]=List_Difference_Full(line["file"],success_deleted_file)
		
		# 删除Concept链接的file
		for concept in self.data[1]:
			concept["file"]=List_Difference_Full(concept["file"],success_deleted_file)
	
	def generateDiaryConceptFileDict(self,date:QDate,type:int,name:str,url:str):
		
		y,m,d=QDate_to_Tuple(date)
		file={
			"y":y,
			"m":m,
			"d":d,
			"type":type,
			"name":name,
			"url":url
		}
		return file
	
	def generateLibraryFileDict(self,date:QDate,type:int,name:str,url:str):
		y,m,d=map(str,QDate_to_Tuple(date))
		concept_list=self.data[2][y][m][d][name]["concept"]
		file={
			"y":int(y),
			"m":int(m),
			"d":int(d),
			"type":type,
			"name":name,
			"url":url,
			"concept":concept_list
		}
		return file
	
	######################################################################

	def parseSearchText(self,search:str):
		"""
		name1
		name1 name2 [ConceptA]
		name (2021.7.4) [ConceptA] name2
		(2021.7.4) [ConceptA] name
		(2021.7.4-2021.7.21) [ConceptA] [Concept B] name
		"""
		
		def parseDateOne(i):

			# (2021)==(2021.1.1-2021.12.31)
			if i.count(".")==0 and i.isdigit():
				begin=QDate(int(i),1,1)
				end=QDate(int(i),12,31)
				if begin.isValid():
					return (begin,end)
			
			# (2021.7)==(2021.7.1-2021.7.31)
			elif i.count(".")==1:
				try:
					y,m=map(int,i.split("."))
					begin=QDate(y,m,1)
					if begin.isValid():
						end=begin.daysInMonth()
						end=QDate(y,m,end)
						return (begin,end)
				except:
					return None
			# (2021.7.20)
			elif i.count(".")==2:
				try:
					y,m,d=map(int,i.split("."))
					date=QDate(y,m,d)
					if date.isValid():
						return (date)
				except:
					return None
			
			return None
		
		def parseDateTwo(i):
			# (2021)==(2021.1.1)
			if i.count(".")==0 and i.isdigit():
				date=QDate(int(i),1,1)
				if date.isValid():
					return date
			
			# (2021.7)==(2021.7.1)
			elif i.count(".")==1:
				try:
					y,m=map(int,i.split("."))
					date=QDate(y,m,1)
					if date.isValid():
						return date
				except:
					return None
			# (2021.7.20)
			elif i.count(".")==2:
				try:
					y,m,d=map(int,i.split("."))
					date=QDate(y,m,d)
					if date.isValid():
						return date
				except:
					return None
			
			return None
		
		search=search.lower()
		if search.strip()!="":
			search=" "+search+" "
			
			TYPE=re.findall("(?<= \{).*?(?=\} )",search)
			search=re.sub("\{.*?\}","",search)
			if TYPE!=[]:
				if str.isdigit(TYPE[0]):
					TYPE=int(TYPE[0])
				else:
					TYPE=None
			else:
				TYPE=None
			
			concept_list=re.findall("(?<= \[).*?(?=\] )",search)
			search=re.sub("\[.*?\]","",search)
			# []表示搜索没有链接concept的内容
			if concept_list==[""]:
				concept_list=None
			
			date_str_list=re.findall("(?<= \().*?(?=\) )",search)
			date_range_list=[]
			search=re.sub("\(.*?\)","",search)
			for i in date_str_list:
				if i.count("-")==0:
					# (2021) \ (2021.7) \ (2021.7.1)
					res=parseDateOne(i)
					if res!=None:
						date_range_list.append(res)
				
				elif i.count("-")==1:
					# (2021-2021.7) \ (2021.1.1-2021.12.31) \ ...
					try:
						begin,end=i.split("-")
						begin=parseDateTwo(begin)
						end=parseDateTwo(end)
						if begin!=None and end!=None:
							date_range_list.append((begin,end))
					except:
						pass
				else:
					pass

			name_list=search.split()

			return name_list,date_range_list,concept_list,TYPE
		else:
			return [],[],[],None
	
	def extractFileURL(self, url:str):
		if url[:4]=="http":
			pass
		else:
			url=os.path.abspath(url).replace("\\","/").replace(os.path.abspath(self.library_base+"/").replace("\\","/"),"")
			if len(url)>1 and url[0]=="/":
				url=url[1:]
		return url