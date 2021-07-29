# # --
from DTPySide import *

class LoadThumbnailThread(QThread):

	def __init__(self, parent, Headquarter, file, row, ROWHEIGHT, force=False):
		super().__init__(parent=parent)
		self.Headquarter=Headquarter
		self.file=file
		self.row=row
		self.ROWHEIGHT=ROWHEIGHT
		self.force=force
	
	def run(self):
		
		y=self.file["y"]
		m=self.file["m"]
		d=self.file["d"]
		type=self.file["type"]
		name=self.file["name"]
		url=self.file["url"]
		ext=url.split(".")[-1].lower()
		cache_name=QDate_to_Str(QDate(y,m,d),"0")+name

		if self.file["type"]==2 and "bilibili" in url:
			data=self.Headquarter.cache.get("bilibili就你多事")
			if data==None or self.force==True:
				status,data=GetWebFavIcon("https://www.bilibili.com/")
				if status==True:

					self.Headquarter.qlock.lock()
					self.Headquarter.cache["bilibili就你多事"]=data
					self.Headquarter.qlock.unlock()
					
					pixmap=QPixmap()
					ba = QByteArray(data)
					pixmap.loadFromData(ba, "ico")
					icon=QIcon(pixmap)
				else:
					self.Headquarter.qlock.lock()
					self.Headquarter.cache["bilibili就你多事"]=-1
					self.Headquarter.qlock.unlock()
					icon=QIcon(":/icon/white/white_globe.svg")
			elif data==-1:
				icon=QIcon(":/icon/white/white_globe.svg")
			else:
				pixmap=QPixmap()
				ba = QByteArray(data)
				pixmap.loadFromData(ba, ext)
				icon=QIcon(pixmap)
			
			self.parent().lock.lock()
			self.parent().item(self.row,3).setIcon(icon)
			self.parent().lock.unlock()
			return


		data=self.Headquarter.cache.get(cache_name)
		# cache中有
		if data!=None or self.force==True:
			if data==-1: #一些防爬的就算了，标记-1，制定icon的时候给globe就行了
				icon=QIcon(":/icon/white/white_globe.svg")
			else:
				if type!=2:
					# convert bytes to QPixmap
					pixmap=QPixmap()
					ba = QByteArray(data)
					pixmap.loadFromData(ba, ext)
					icon=QIcon(pixmap)
				else:
					# convert bytes to QPixmap
					pixmap=QPixmap()
					ba = QByteArray(data)
					if not pixmap.loadFromData(ba, "ico"):
						if not pixmap.loadFromData(ba, "png"): # 有的favicon竟然是png……
								pixmap.loadFromData(ba, "svg") # 有的favicon竟然是svg……
					icon=QIcon(pixmap)
			
			self.parent().lock.lock()
			self.parent().item(self.row,3).setIcon(icon)
			self.parent().lock.unlock()
			return
		
		# cache中没有
		# 文件
		if self.file["type"]!=2:
			url=os.path.join(self.Headquarter.library_base,url).replace("\\","/")
			
			if self.file["type"]==0 or ext not in image_extension:
				# folder或者其他类型文件
				file_info=QFileInfo(url)
				icon=QFileIconProvider().icon(file_info)
			else:
				# 图片
				pixmap=QPixmap()
				pixmap.load(url)
				pixmap=pixmap.scaled(self.ROWHEIGHT,self.ROWHEIGHT,Qt.KeepAspectRatio,Qt.FastTransformation)

				# convert QPixmap to bytes
				ba = QByteArray()
				buff = QBuffer(ba)
				buff.open(QIODevice.WriteOnly)
				pixmap.save(buff, ext)
				pixmap_bytes = ba.data()
				
				self.Headquarter.qlock.lock()
				self.Headquarter.cache[cache_name]=pixmap_bytes
				self.Headquarter.qlock.unlock()

				icon=QIcon(pixmap)
		
		# link
		elif self.file["type"]==2:
			status,data=GetWebFavIcon(url)
			if status==True:

				self.Headquarter.qlock.lock()
				self.Headquarter.cache[cache_name]=data
				self.Headquarter.qlock.unlock()
				
				pixmap=QPixmap()
				ba = QByteArray(data)
				if not pixmap.loadFromData(ba, "ico"):
					if not pixmap.loadFromData(ba, "png"): # 有的favicon竟然是png……
							pixmap.loadFromData(ba, "svg") # 有的favicon竟然是svg……
				icon=QIcon(pixmap)
			else:
				#一些防爬的就算了，标记-1，制定icon的时候给globe就行了
				self.Headquarter.qlock.lock()
				self.Headquarter.cache[cache_name]=-1
				self.Headquarter.qlock.unlock()
				
				icon=QIcon(":/icon/white/white_globe.svg")
		
		self.parent().lock.lock()
		self.parent().item(self.row,3).setIcon(icon)
		self.parent().lock.unlock()
		return


from filetype import image_extension
from session.LobbySession import LobbySession
class FileTable(DTWidget.DTHorizontalTabel):

	fileDropped=Signal(list,list)
	
	def eventFilter(self, watched: QObject, event:QKeyEvent) -> bool:
		if event.type()==QEvent.KeyPress or event.type()==QEvent.KeyRelease:
			if event.key()==Qt.Key_Alt:
				self.__altPressed=True
			else:
				self.__altPressed=False
		return False # 这里是让继续延续event的处理，不要被filter掉了
	
	def startDrag(self, actions:Qt.DropActions):
		######################################################################
		# MIME通信规则：
		# 
		# text/url_list: 来自内部，["file:///E:/dlcw/2021/7/21/a.txt","https://www.google.com"]；
		#                来自外部，则为windows explorer的drag event自带的url_list
		# FileList: 来自内部，[{
		# 	"y":y,
		# 	"m":m,
		# 	"d":d,
		# 	"type":type,
		# 	"name":name,
		# 	"url":url
		# }]
		#                来自外部，为[]
		######################################################################
		
		indexes = self.selectedIndexes()
		mime = self.model().mimeData(indexes)
		
		url_list = []
		file_list=[]
		for model_index in self.selectionModel().selectedRows():
			row=model_index.row()
			
			type=int(self.item(row,0).text())
			y,m,d=map(int,self.item(row,1).text().split("."))
			name=self.item(row,3).text()
			url=self.item(row,4).text().replace(self.Headquarter.library_base+"/","")
			file_list.append(self.Headquarter.generateDiaryConceptFileDict(QDate(y,m,d),type,name,url))

			if self.item(row,0).text()=="0":
				url="file:///"+self.item(row,4).text()
			url_list.append(QUrl(url))
		
		#防止拖到自己的里面
		mime.setObjectName(self.objectName())
		mime.setUrls(url_list)
		mime.setData("FileList",bytes(json.dumps(file_list),encoding="utf-8"))
		
		drag = QDrag(self)
		drag.setPixmap(QIcon(":/icon/white/white_inbox.svg").pixmap(32,32))
		drag.setMimeData(mime)
		drag.exec_(actions)
	
	def dragEnterEvent(self, event:QDragEnterEvent):
		if event.mimeData().objectName()==self.objectName():
			# 拖到自己
			event.ignore()
		elif event.mimeData().objectName()!="" and self.objectName()=="LibraryFileTable":
			# 内部不允许拖到LibraryFileTable
			event.ignore()
		elif event.mimeData().hasUrls():
			event.acceptProposedAction()
	
	def dragMoveEvent(self, event: QDragMoveEvent):
		# 淦！为什么接受资源管理器拖进来的文件，还得implement这个event。
		# 找这个Bug花了我将近一个小时的时间？！茶屋工作室1.0里就不用的？！！
		event.acceptProposedAction()

	def dropEvent(self, event:QDropEvent):
		url_list=[url.toString() for url in event.mimeData().urls()]
		
		try:
			file_list=json.loads((event.mimeData().data("FileList").data().decode("utf-8")))
		except:
			file_list=[]
		
		self.fileDropped.emit(url_list,file_list)
	
	def mousePressEvent(self, event: QMouseEvent):
		def slot():

			for model_index in self.selectionModel().selectedRows():
				row=model_index.row()

				type=int(self.item(row,0).text())
				y,m,d=map(int,self.item(row,1).text().split("."))
				name=self.item(row,3).text()
				url=self.item(row,4).text().replace(self.Headquarter.library_base+"/","")
				file=self.Headquarter.generateDiaryConceptFileDict(QDate(y,m,d),type,name,url)

				loading_thread=LoadThumbnailThread(self,self.Headquarter,file,row,self.ROWHEIGHT,force=True)
				loading_thread.finished.connect(loading_thread.deleteLater)
				loading_thread.start()
		
		pos=event.pos()
		if event.button()==Qt.RightButton:
			
			menu=QMenu()
			action=QAction("Refresh Icon")
			action.triggered.connect(slot)
			menu.addAction(action)
			pos=self.mapToGlobal(pos)
			menu.exec_(pos)
			
			
		else:
			super().mousePressEvent(event)

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.setMinimumHeight(150)
		self.setColumn(["Type","Date","Ext","File","Url"])
		self.setColumnHidden(4,True)
		self.itemDoubleClicked.connect(self.openFile)

		self.ROWHEIGHT=32
		self.setIconSize(QSize(self.ROWHEIGHT,self.ROWHEIGHT))

		self.lock=QMutex(QMutex.NonRecursive) # 更新icon时防止多线程在刷新完列表之前就去更新

		self.__altPressed=False
		self.installEventFilter(self)
	
	def setHeadquarter(self,Headquarter: LobbySession):
		self.Headquarter=Headquarter
	
	def setFileList(self, file_list):
		"""设置filetable为file_list

		Args:
			file_list (list): 元素具有y,m,d,name,type,url属性
		"""

		self.StoreTableStatus()
		self.Clear()

		row=0
		# 更新icon时防止多线程在刷新完列表之前就去更新
		self.lock.lock()
		for file in file_list:

			y=file["y"]
			m=file["m"]
			d=file["d"]
			type=file["type"]
			name=file["name"]
			url=file["url"]
			
			if type==0:
				ext="folder"
			elif type==1:
				url=os.path.join(self.Headquarter.library_base,url).replace("\\","/")
				ext=url.split(".")[-1].lower()
			elif type==2:
				ext="link"

			loading_thread=LoadThumbnailThread(self,self.Headquarter,file,row,self.ROWHEIGHT)
			loading_thread.finished.connect(loading_thread.deleteLater)
			loading_thread.start()
			
			self.addRow(row,[QTableWidgetItem(str(type)),QTableWidgetItem("%s.%s.%s"%(y,m,d)),QTableWidgetItem(ext),QTableWidgetItem(name),QTableWidgetItem(url)])
			self.setRowHeight(row,self.ROWHEIGHT)
			row+=1
		
		self.RestoreTableStatus()
		self.lock.unlock()

	def openFile(self):
			
		url=self.item(self.currentRow(),4).text()
		type=self.item(self.currentRow(),0).text()
		ext=self.item(self.currentRow(),2).text()

		if type!="2":
			# alt打开根目录
			if self.__altPressed==True:
				url=os.path.dirname(url)
				self.__altPressed=False
				try:
					os.startfile(url)
				except Exception as e:
					DTFrame.DTMessageBox(self,"Warning","Could not open file! Try running Check Library.\n\n%s"%e,DTIcon.Warning())
			
			# 打开图片，自动附加上fileTable中其他的图片
			elif ext.lower() in image_extension:
				if os.path.exists(url):
					pic_list=[self.item(row,4).text() for row in range(self.rowCount()) if self.item(row,2).text().lower() in image_extension]
					index=pic_list.index(url)

					from session import ImageViewerSession
					self.imageviewer=ImageViewerSession(self.Headquarter.app,pic_list,index)
					self.imageviewer.initialize()
					self.imageviewer.show()
				else:
					DTFrame.DTMessageBox(self,"Warning","Could not open file! Try running Check Library.",DTIcon.Warning())
			else:
				try:
					os.startfile(url)
				except Exception as e:
					DTFrame.DTMessageBox(self,"Warning","Could not open file! Try running Check Library.\n\n%s"%e,DTIcon.Warning())
		else:
			os.system("start explorer \"%s\""%url)