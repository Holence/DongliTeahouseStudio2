# # --
from DTPySide import *
from DTPySide.DTFrame.DTMainWindow import DTMainWindow


class LobbySession(DTSession.DTMainSession):
	
	def eventFilter(self, watched: QObject, event:QMouseEvent) -> bool:
		# 为了实现重新focusIn窗体的时候刷新界面，虽然手动把一堆子控件installEventFilter一遍，但也只能这样了
		# focusInEvent和mousePressEvent都试了，都不可能捕获子控件的事件，所以只有点击到TitleBar或者window的空白区域，才可能被触发
		if (event.type()==QEvent.MouseButtonPress and event.button()==Qt.LeftButton) or event.type()==QEvent.FocusIn:
			# print(watched)
			if self.WindowFocusing()!=self:
				self.setWindowFocusing(self)
				# print("Now focused in",self.WindowFocusing())
		return False # 这里是让继续延续event的处理，不要被filter掉了

	def __init__(self, app):
		super().__init__(app)
		self.__WindowFocusing=None #记录点击的window，如果focus的window改变，对应被focusIn的window就要刷新画面
		
	
	def WindowFocusing(self):
		return self.__WindowFocusing
	
	def setWindowFocusing(self,which:DTMainWindow):
		self.__WindowFocusing=which
	
	def loadData(self):
		if os.path.exists("Diary_Data.dlcw"):
			self.diary_data=Fernet_Decrypt_Load(self.password(),"Diary_Data.dlcw")
			if self.diary_data==False:
				DTFrame.DTMessageBox(self,"Error","Diary data error!")
				self.app.quit()
		else:
			self.diary_data={}
			Fernet_Encrypt_Save(self.password(),self.diary_data,"Diary_Data.dlcw")
		
		if os.path.exists("Concept_Data.dlcw"):
			self.concept_data=Fernet_Decrypt_Load(self.password(),"Concept_Data.dlcw")
			if self.concept_data==False:
				DTFrame.DTMessageBox(self,"Error","Concept data error!")
				self.app.quit()
		else:
			self.concept_data=[]
			Fernet_Encrypt_Save(self.password(),self.concept_data,"Diary_Data.dlcw")
		
		if os.path.exists("Library_Data.dlcw"):
			self.library_data=Fernet_Decrypt_Load(self.password(),"Library_Data.dlcw")
			if self.library_data==False:
				DTFrame.DTMessageBox(self,"Error","Library data error!")
				self.app.quit()
		else:
			self.library_data={}
			Fernet_Encrypt_Save(self.password(),self.library_data,"Library_Data.dlcw")

		self.library_base=Fernet_Decrypt(self.password(),self.UserSetting().value("LibraryBase"))
		if self.library_base==False:
			dlg=QFileDialog(self)
			while not self.library_base:
				DTFrame.DTMessageBox(self,"Information","You need to set Library Base first!")
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
		self.diary_dump=[]
		diary=DiarySession(self.app,self)
		diary.initialize()
		self.diary_dump.append(diary)

		from session.ConceptSession import ConceptSession
		self.concept_dump=[]
		concept=ConceptSession(self.app,self)
		concept.initialize()
		self.concept_dump.append(concept)


		from session.LibrarySession import LibrarySession
		self.library_dump=[]
		library=LibrarySession(self.app,self)
		library.initialize()
		self.library_dump.append(library)

	def restoreWindowStatus(self):
		try:
			self.resize(self.UserSetting().value("WindowStatus/LobbySize"))
			self.move(self.UserSetting().value("WindowStatus/LobbyPos"))
		except:
			pass

	def initializeSignal(self):
		super().initializeSignal()
		self.installEventFilter(self)
		self.refreshModuleSingal()

	
	def refreshModuleSingal(self):
		def slot(id):
			for concept in self.concept_dump:
				concept.show()
				concept.setFocus()
				concept.concept_module.showConcept(id)
		
		for diary in self.diary_dump:
			diary.diary_module.conceptTable.conceptClicked.connect(slot)
		
		for library in self.library_dump:
			library.library_module.conceptTable.conceptClicked.connect(slot)

	def saveWindowStatus(self):
		self.UserSetting().setValue("WindowStatus/LobbySize",self.size())
		self.UserSetting().setValue("WindowStatus/LobbyPos",self.pos())
		self.UserSetting().setValue("WindowStatus/DiarySize",self.diary_dump[0].size())
		self.UserSetting().setValue("WindowStatus/DiaryPos",self.diary_dump[0].pos())
		self.UserSetting().setValue("WindowStatus/ConceptSize",self.concept_dump[0].size())
		self.UserSetting().setValue("WindowStatus/ConceptPos",self.concept_dump[0].pos())
		self.UserSetting().setValue("WindowStatus/LibrarySize",self.library_dump[0].size())
		self.UserSetting().setValue("WindowStatus/LibraryPos",self.library_dump[0].pos())

	def saveData(self):
		Fernet_Encrypt_Save(self.password(),self.diary_data,"Diary_Data.dlcw")
		Fernet_Encrypt_Save(self.password(),self.concept_data,"Concept_Data.dlcw")
		Fernet_Encrypt_Save(self.password(),self.library_data,"Library_Data.dlcw")

	def saveAllEncryptData(self):
		super().saveAllEncryptData()
		self.saveData()
		self.UserSetting().setValue("LibraryBase",Fernet_Encrypt(self.password(),self.library_base))
	
	def setting(self):
		from session.SettingSession import SettingSession
		dlg=SettingSession(self,self.app)
		dlg.exec_()

	#################################################################

	def getDiaryData(self):
		return self.diary_data

	def getDiaryDay(self, date:QDate):
		"""获取一日的diary_data，若存在则返回该日字典，若不存在则返回None

		Args:
			date (QDate): 要读取的日期

		Returns:
			[type]: 该日的diary_data字典
		"""

		year, month, day= map(str, QDate_to_Tuple(date))
		try:
			return self.diary_data[year][month][day]
		except:
			return None
	
	def getDiaryDayLine(self, date:QDate, index:int):
		year, month, day= map(str, QDate_to_Tuple(date))
		try:
			return self.diary_data[year][month][day][index]
		except:
			return None

	def addDiaryDay(self, date:QDate):
		"""在diary_data中创建对应date的列表容器，并返回该列表容器

		Args:
			date (QDate): 要创建的日期

		Returns:
			[type]: 返回该列表容器
		"""	

		year, month, day= map(str, QDate_to_Tuple(date))
		
		if self.diary_data.get(year)==None:
			self.diary_data[year]={}
			self.diary_data=dict(sorted(self.diary_data.items(),key=lambda x:int(x[0])))
		
		if self.diary_data[year].get(month)==None:
			self.diary_data[year][month]={}
			self.diary_data[year]=dict(sorted(self.diary_data[year].items(),key=lambda x:int(x[0])))
		
		if self.diary_data[year][month].get(day)==None:
			self.diary_data[year][month][day]=[]
			self.diary_data[year][month]=dict(sorted(self.diary_data[year][month].items(),key=lambda x:int(x[0])))
		
		return self.diary_data[year][month][day]
	
	#################################################################

	def getConceptData(self):
		return self.concept_data

	def getConcept(self, id:int):
		"""获取指定的concept，若存在则返回该concept字典，若不存在则返回None

		Args:
			id (int): 要读取的concept

		Returns:
			[type]: 该concept的字典
		"""
		try:
			return self.concept_data[id]
		except:
			return None
	
	def appendConcept(self):
		"""在concept_data中append concept字典容器，返回该字典容器

		Returns:
			[type]: 返回该字典容器
		"""
		self.concept_data.append({
			"id": len(self.concept_data),
			"name": "",
			"detail": "", 
			"parent": [],
			"child": [],
			"relative": [],
			"az": "",
			"file": [],
		})
		return self.concept_data[-1]
	
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
		for i in range(len(self.concept_data)):
			New_ID_Dict[i]=CalcNewID(i)
		
		# Diary链接的concept中，剔除delete_id_list中的id，并且改需要前移的id
		for year in self.diary_data:
			for month in self.diary_data[year]:
				for day in self.diary_data[year][month]:
					for line in self.diary_data[year][month][day]:
						line["concept"]=Bake_ID_List(line["concept"])

		# Library链接的concept中，剔除delete_id_list中的id，并且改需要前移的id
		for year in self.library_data:
			for month in self.library_data[year]:
				for day in self.library_data[year][month]:
					for file in self.library_data[year][month][day]:
						file=self.library_data[year][month][day][file]
						file["concept"]=Bake_ID_List(file["concept"])

		# 还是别在for循环中用remove或者pop了，太麻烦了，这样一句话就完事，运算效率还高
		self.concept_data=[concept for concept in self.concept_data if concept["id"] not in delete_id_list]

		# Concept中改需要前移的id
		for concept in self.concept_data:
			concept["id"]=New_ID_Dict[concept["id"]]
			concept["parent"]=Bake_ID_List(concept["parent"])
			concept["child"]=Bake_ID_List(concept["child"])
			concept["relative"]=Bake_ID_List(concept["relative"])

	def addParent(self,concept_id,parent_id_list):
		concept=self.concept_data[concept_id]
			
		for parent_id in List_Difference(parent_id_list,concept["parent"]):
			
			# 禁止自生
			if parent_id==concept_id:
				DTFrame.DTMessageBox(self,"Information","Are you kidding?",DTIcon.Holo01())
				continue

			# 禁止隔一辈的乱伦，隔数辈的允许组成有向图
			if parent_id in concept["child"]:
				DTFrame.DTMessageBox(self,"Information","%s is already %s's child."%(self.concept_data[parent_id]["name"],self.concept_data[concept_id]["name"]),DTIcon.Information())
				continue
			
			concept["parent"].append(parent_id)
			if concept_id not in self.concept_data[parent_id]["child"]:
				self.concept_data[parent_id]["child"].append(concept_id)
			else:
				# 数据错误
				DTFrame.DTMessageBox(self,"Error","Error occured during adding parent!\n\n%s is already %s's child."%(concept_id,parent_id),DTIcon.Error())
	
	def addChild(self,concept_id,child_id_list):
		concept=self.concept_data[concept_id]
			
		for child_id in List_Difference(child_id_list,concept["child"]):
			
			# 禁止自生
			if child_id==concept_id:
				DTFrame.DTMessageBox(self,"Information","Are you kidding?",DTIcon.Holo01())
				continue

			# 禁止隔一辈的乱伦，隔数辈的允许组成有向图
			if child_id in concept["parent"]:
				DTFrame.DTMessageBox(self,"Information","%s is already %s's parent."%(self.concept_data[child_id]["name"],self.concept_data[concept_id]["name"]),DTIcon.Information())
				continue
			
			concept["child"].append(child_id)
			if concept_id not in self.concept_data[child_id]["parent"]:
				self.concept_data[child_id]["parent"].append(concept_id)
			else:
				# 数据错误
				DTFrame.DTMessageBox(self,"Error","Error occured during adding child!\n\n%s is already %s's parent."%(concept_id,child_id),DTIcon.Error())

	def addRelative(self,concept_id,relative_id_list):
		concept=self.concept_data[concept_id]
		
		for relative_id in List_Difference(relative_id_list,concept["relative"]):
			
			# 禁止自交
			if relative_id==concept_id:
				DTFrame.DTMessageBox(self,"Information","That's not a good idea.",DTIcon.Holo01())
				continue

			concept["relative"].append(relative_id)
			if concept_id not in self.concept_data[relative_id]["relative"]:
				self.concept_data[relative_id]["relative"].append(concept_id)
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

	def getLibraryFile(self,date:QDate,name):
		year, month, day= map(str, QDate_to_Tuple(date))
		try:
			return self.library_data[year][month][day][name]
		except:
			return None

	def getLibraryFileList(self,name_list=[],date_range_list=[],concept_name_list=[]):
		
		def add_all_files():
			for y in self.library_data:
				for m in self.library_data[y]:
					for d in self.library_data[y][m]:
						for file_name,file in self.library_data[y][m][d].items():
							file_list.append({
								"y":y,
								"m":m,
								"d":d,
								"type":file["type"],
								"name":file_name,
								"url":file["url"],
								"concept":file["concept"],
								"concept_az":[self.concept_data[id]["az"] for id in file["concept"]]
							})

		def add_file_in_dates(begin:QDate,end:QDate=None):
			if end==None:
				end=QDate(begin)

			while begin<=end:
				y,m,d=map(str,QDate_to_Tuple(begin))
				try:
					for file_name,file in self.library_data[y][m][d].items():
						file_list.append({
							"y":y,
							"m":m,
							"d":d,
							"type":file["type"],
							"name":file_name,
							"url":file["url"],
							"concept":file["concept"],
							"concept_az":[self.concept_data[id]["az"] for id in file["concept"]]
						})
				except:
					pass
				begin=begin.addDays(1)
		
		def namelist_in_filename(file_name):
			# 判断文件名是否包含搜索name列表中的所有元素，如果全部包含则返回非零值（True），否则返回0（False）
			return not len([i for i in name_list if i.lower() not in file_name.lower() and i.lower() not in Str_to_AZ(file_name)])
		
		file_list=[]
		if date_range_list==[]:
			add_all_files()
		else:
			for date_range in date_range_list:
				if type(date_range)==tuple:
					add_file_in_dates(*date_range)
				else:
					add_file_in_dates(date_range)
		
		if concept_name_list!=[]:
			concept_name_list=[ Str_to_AZ(concept_name) for concept_name in concept_name_list]
			file_list=[file for file in file_list if List_Difference(concept_name_list,file["concept_az"])==[] ]
		
		if name_list!=[]:
			file_list=[file for file in file_list if namelist_in_filename(file["name"])]

		return file_list

	def addLibraryFile(self, date:QDate, url:str, concept:list=[]):
		"如果是file类型，url为原始地址；如果是link类型，url为网站地址"
		y, m, d= map(str, QDate_to_Tuple(date))
		
		if url[:8]=="file:///":
			type=0
			old_dir=url[8:]
			name=os.path.basename(old_dir)

			# 禁止从library_base层添加文件
			if self.library_base in os.path.dirname(old_dir):
				if os.path.dirname(old_dir).replace(self.library_base+"/","").count("/")<=2:
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
				if name in os.listdir(new_base):
					DTFrame.DTMessageBox(self,"Error","%s already exsit in %s!"%(name,new_base),DTIcon.Warning())
					return None
				
				# 移动
				shutil.move(old_dir,new_dir)
			
			except Exception as e:
				# 出错
				DTFrame.DTMessageBox(self,"Error",str(e),DTIcon.Warning())
				return None
		else:
			type=1
			status,res=GetWebPageResponse(url)
			if status==True:
				
				# 浏览器拖图片
				# Yandex浏览器的图片拖出来，附带的url不是临时文件地址，这里就手动下载好了
				if "image" in res.raw.info()["Content-Type"]:
					try:
						type=res.raw.info()["Content-Type"].split("/")[1]
						status,res=GetWebPagePic(response=res)
						if status==True:
							# 在根目录生成临时文件
							temp_file_url=os.path.join(os.getcwd(),"%s.%s"%(time.time_ns(),type))
							with open(temp_file_url,"wb") as f:
								f.write(res)
							return self.addLibraryFile(date,"file:///"+temp_file_url,concept)
						else:
							DTFrame.DTMessageBox(self,"Warning",str(res),DTIcon.Warning())
							return None
						
					except Exception as e:
						DTFrame.DTMessageBox(self,"Warning",str(e),DTIcon.Warning())
						return None
				
				# 普通网页
				else:
					status,res=GetWebPageTitle(response=res)
					if status==True:
						name=res
					else:
						DTFrame.DTMessageBox(self,"Warning",str(res),DTIcon.Warning())
						return None

		if self.library_data.get(y)==None:
			self.library_data[y]={}
		
		if self.library_data[y].get(m)==None:
			self.library_data[y][m]={}
		
		if self.library_data[y][m].get(d)==None:
			self.library_data[y][m][d]={}
		
		self.library_data[y][m][d][name]={
			"type": type,
			"concept": concept,
			"url": url
		}
		
		return name,self.library_data[y][m][d][name]
	
	def renameLibraryFile(self,date:QDate,old_name,new_name):
		y, m, d= map(str, QDate_to_Tuple(date))


		file=self.library_data[y][m][d][old_name]
		old_url=file["url"]
		new_url=file["url"].replace(old_name,new_name)
		
		if file["type"]==0:
			try:
				os.rename(os.path.join(self.library_base,old_url),os.path.join(self.library_base,new_url))
			except Exception as e:
				DTFrame.DTMessageBox(self,"Error",str(e),DTIcon.Error())
				return
		
		file["url"]=new_url
		del self.library_data[y][m][d][old_name]
		self.library_data[y][m][d][new_name]=file
		
		old_file={
			"y":int(y),
			"m":int(m),
			"d":int(d),
			"type":file["type"],
			"name":old_name,
			"url":old_url
		}

		# 重命名diary line链接的file
		for year in self.diary_data:
			for month in self.diary_data[year]:
				for day in self.diary_data[year][month]:
					for line in self.diary_data[year][month][day]:
						if old_file in line["file"]:
							file=line["file"][line["file"].index(old_file)]
							file["name"]=new_name
							file["url"]=new_url
		
		# 重命名Concept链接的file
		for concept in self.concept_data:
			if old_file in concept["file"]:
				file=concept["file"][concept["file"].index(old_file)]
				file["name"]=new_name
				file["url"]=new_url
		

	def deleteLibraryFile(self, delete_file_list):
		"""删除多个LibraryFile

		Args:
			delete_file_list (list): 元素为diary line["file"]和concept["file"]的字典标准型（包含y,m,d,type,name,url）
		"""
		for file in delete_file_list:
			year=str(file["y"])
			month=str(file["m"])
			day=str(file["d"])
			name=file["name"]
			url=file["url"]

			if file["type"]==0:
				try:
					res=Delete_to_Recyclebin(os.path.join(self.library_base,url))
					if res==False:
						DTFrame.DTMessageBox(self,"Error","Failed to delete %s"%name,DTIcon.Warning())
				except Exception as e:
					# 出错
					DTFrame.DTMessageBox(self,"Error",str(e),DTIcon.Warning())
			
			del self.library_data[year][month][day][name]

		# 删除Diary链接的file
		for year in self.diary_data:
			for month in self.diary_data[year]:
				for day in self.diary_data[year][month]:
					for line in self.diary_data[year][month][day]:
						line["file"]=List_Difference_Full(line["file"],delete_file_list)
		
		# 删除Concept链接的file
		for concept in self.concept_data:
			concept["file"]=List_Difference_Full(concept["file"],delete_file_list)