# # --
from DTPySide import *

class FileTable(DTWidget.DTHorizontalTabel):

	fileDropped=Signal(list,list)
	
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

			if type!=2:
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

				type=int(self.item(row,0).text())
				y,m,d=map(int,self.item(row,1).text().split("."))
				name=self.item(row,3).text()
				url=self.item(row,4).text().replace(self.Headquarter.library_base+"/","")
				file=self.Headquarter.generateDiaryConceptFileDict(QDate(y,m,d),type,name,url)
				
				from widget.FileTab import LoadThumbnailThread
				loading_thread=LoadThumbnailThread(self,self.Headquarter,file,row,force=True)
				loading_thread.finished.connect(loading_thread.deleteLater)
				loading_thread.start()
		
		def slot2():
			row=self.currentRow()
			y,m,d=map(int,self.item(row,1).text().split("."))
			date=QDate(y,m,d)
			type=int(self.item(row,0).text())
			old_name=self.item(row,3).text()

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
					self.item(row,3).setText(new_name)
					if type!=2:
						url=self.Headquarter.getLibraryFile(date,new_name)["url"]
						url=os.path.join(self.Headquarter.library_base,url).replace("\\","/")
						self.item(row,4).setText(url)

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
		self.setColumn(["Type","Date","Ext","File","Url"])
		self.setColumnHidden(4,True)

		self.setIconSize(QSize(32,32))

		self.lock=QMutex(QMutex.NonRecursive) # 更新icon时防止多线程在刷新完列表之前就去更新
		self.thread_list=[]

	def Clear(self):
		self.lock.lock()
		super().Clear()
		self.lock.unlock()