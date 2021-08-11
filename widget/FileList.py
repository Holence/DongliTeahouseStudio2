# # --
from DTPySide import *

class FileList(QListWidget):

	fileDropped=Signal(list,list)

	def eventFilter(self, watched: QObject, event:QEvent) -> bool:
		if event.type()==QEvent.KeyPress:
			if event.key()==Qt.Key_Control:
				self.__ctrlPressed=True
		if event.type()==QEvent.KeyRelease:
			if event.key()==Qt.Key_Control:
				self.__ctrlPressed=False
		return False # 这里是让继续延续event的处理，不要被filter掉了

	def wheelEvent(self, event: QWheelEvent):
		if self.__ctrlPressed==True:
			xscrolls = event.angleDelta().x()
			yscrolls = event.angleDelta().y()
			
			#放大
			if xscrolls>0 or yscrolls>0:
				icon_size=self.iconSize()+QSize(self.step,self.step)
				grid_size=self.gridSize()+QSize(self.step,self.step)
			#缩小
			elif xscrolls<0 or yscrolls<0 and self.iconSize().width()-self.step>32:
				icon_size=self.iconSize()-QSize(self.step,self.step)
				grid_size=self.gridSize()-QSize(self.step,self.step)
			else:
				return False
			
			self.setIconSize(icon_size)
			self.setGridSize(grid_size)
		else:
			super().wheelEvent(event)
		
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
			
			url=self.item(row).toolTip().replace(self.Headquarter.library_base+"/","")
			if url[:4]=="http":
				name=self.item(row).text()
				date=Str_To_QDate(name[name.rfind("|")+1:][1:-1],".")
				name=name[:name.rfind("|")]
			else:
				y,m,d=url.split("/")[:3]
				date=QDate(int(y),int(m),int(d))
				name=self.item(row).text()

			type=self.Headquarter.getLibraryFile(date,name)["type"]
			file_list.append(self.Headquarter.generateDiaryConceptFileDict(date,type,name,url))

			if type!=2:
				url="file:///"+self.item(row).toolTip()
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
		elif event.mimeData().objectName()!="" and (self.objectName()=="LibraryFileTable" or self.objectName()=="LibraryFileList"):
			# 内部不允许拖到LibraryFileTable\LibraryFileList
			event.ignore()
		elif event.mimeData().hasUrls():
			event.acceptProposedAction()
		elif event.mimeData().hasText():
			if [False for url in event.mimeData().text().split() if "http" not in url].count(False)==0:
				event.acceptProposedAction()
	
	def dragMoveEvent(self, event: QDragMoveEvent):
		# 淦！为什么接受资源管理器拖进来的文件，还得implement这个event。
		# 找这个Bug花了我将近一个小时的时间？！茶屋工作室1.0里就不用的？！！
		event.acceptProposedAction()

	def dropEvent(self, event:QDropEvent):

		if event.mimeData().hasUrls():
			url_list=[url.toString() for url in event.mimeData().urls()]
		elif event.mimeData().hasText():
			url_list=[url.strip() for url in event.mimeData().text().split()]
		
		try:
			file_list=json.loads((event.mimeData().data("FileList").data().decode("utf-8")))
		except:
			file_list=[]
		self.fileDropped.emit(url_list,file_list)
	
	def mousePressEvent(self, event: QMouseEvent):
		def slot():

			for model_index in self.selectionModel().selectedRows():
				row=model_index.row()

				url=self.item(row).toolTip().replace(self.Headquarter.library_base+"/","")
				if url[:4]=="http":
					name=self.item(row).text()
					date=Str_To_QDate(name[name.rfind("|")+1:][1:-1],".")
					name=name[:name.rfind("|")]
				else:
					y,m,d=url.split("/")[:3]
					date=QDate(int(y),int(m),int(d))
					name=self.item(row).text()

				type=self.Headquarter.getLibraryFile(date,name)["type"]
				file=self.Headquarter.generateDiaryConceptFileDict(date,type,name,url)
				
				from widget.FileTab import LoadThumbnailThread
				loading_thread=LoadThumbnailThread(self,self.Headquarter,file,row,force=True)
				loading_thread.finished.connect(loading_thread.deleteLater)
				loading_thread.start()
		
		def slot2():
			url=self.currentItem().toolTip().replace(self.Headquarter.library_base+"/","")
			if url[:4]=="http":
				name=self.currentItem().text()
				date=Str_To_QDate(name[name.rfind("|")+1:][1:-1],".")
				old_name=name[:name.rfind("|")]
				type=2
			else:
				y,m,d=url.split("/")[:3]
				date=QDate(int(y),int(m),int(d))
				old_name=self.currentItem().text()
				type=0

			dlg=DTFrame.DTDialog(self.window(),"Rename")
			w=QWidget()
			l=QVBoxLayout(w)
			
			lable1=QLabel("Old Name")
			l.addWidget(lable1)

			line_edit1=QLineEdit(old_name)
			line_edit1.setReadOnly(True)
			l.addWidget(line_edit1)

			lable2=QLabel("New Name")
			l.addWidget(lable2)
			line_edit2=QLineEdit(old_name)
			l.addWidget(line_edit2)

			w.setLayout(l)

			dlg.setCentralWidget(w)
			dlg.setMinimumSize(600,300)

			if dlg.exec_():
				new_name=line_edit2.text()
				res=self.Headquarter.renameLibraryFile(date,old_name,new_name)
				if res!=False:
					if type==2:
						# link的特殊格式
						self.currentItem().setText(new_name+"|[%s]"%QDate_to_Str(date,"."))
					else:
						self.currentItem().setText(new_name)
						url=self.Headquarter.getLibraryFile(date,new_name)["url"]
						url=os.path.join(self.Headquarter.library_base,url).replace("\\","/")
						self.currentItem().setToolTip(url)

		pos=event.pos()
		if event.button()==Qt.RightButton:
			
			if len(self.selectionModel().selectedRows())>0:
				menu=QMenu()
				action1=QAction("Refresh Icon")
				action1.triggered.connect(slot)
				menu.addAction(action1)

				if len(self.selectionModel().selectedRows())==1 and "Library" not in self.objectName():
					action2=QAction("Rename")
					action2.triggered.connect(slot2)
					menu.addAction(action2)
				
				pos=self.mapToGlobal(pos)
				menu.exec_(pos)
			
		else:
			super().mousePressEvent(event)
	
	def __init__(self, parent):
		super().__init__(parent=parent)
		self.setMinimumHeight(150)
		
		self.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.setDragEnabled(True)
		self.setDragDropMode(QAbstractItemView.DragDrop)
		self.setViewMode(QListView.IconMode)

		self.setStyleSheet("""
		QListWidget::item:!selected{
			background:transparent;
			border:none;
		}
		""")
		
		self.step=4
		self.setIconSize(QSize(self.step*10,self.step*10))
		self.setGridSize(QSize(self.step*15,self.step*20))
		self.setWordWrap(True)
		
		self.setResizeMode(QListView.Adjust)
		self.__ctrlPressed=False
		self.installEventFilter(self)

		self.lock=QMutex(QMutex.NonRecursive) # 更新icon时防止多线程在刷新完列表之前就去更新
		self.thread_list=[]
	
	def Clear(self):
		self.lock.lock()
		super().clear()
		self.lock.unlock()