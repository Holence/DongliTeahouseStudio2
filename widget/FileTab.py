# # --
from DTPySide import *
from filetype import image_extension
from web_func import *

ICONWIDTH=128

class LoadThumbnailThread(QThread):

	def __init__(self, parent, Headquarter, file, row, force=False):
		super().__init__(parent=parent)
		self.Headquarter=Headquarter
		self.file=file
		self.row=row
		self.force=force
	
	def run(self):
		
		y=self.file["y"]
		m=self.file["m"]
		d=self.file["d"]
		type=self.file["type"]
		name=self.file["name"]
		url=self.file["url"]
		ext=os.path.splitext(url)[1].lower()[1:]
		cache_name=QDate(y,m,d).toString("yyyyMMdd")+name

		redirect_dict={
			"bilibili":"https://www.bilibili.com/favicon.ico",
			"douban":"https://img3.doubanio.com/favicon.ico",
			"mail.google":"https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
			"gmail":"https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico"
		}

		if self.file["type"]==2:
			for key,value in redirect_dict.items():
				if key in url:

					data=self.Headquarter.cache.get(key)
					if data==None or self.force==True:
						data=GetWebPagePic(value)
						if data!=None:
							data=base64.b64encode(data)

							self.Headquarter.qlock.lock()
							self.Headquarter.cache[key]=data
							self.Headquarter.qlock.unlock()
							
							pixmap=QPixmap()
							pixmap.loadFromData(base64.b64decode(data))
							pixmap=pixmap.scaled(ICONWIDTH,ICONWIDTH,Qt.KeepAspectRatio,Qt.FastTransformation)
							icon=QIcon(pixmap)
						else:
							self.Headquarter.qlock.lock()
							self.Headquarter.cache[key]=-1
							self.Headquarter.qlock.unlock()
							icon=IconFromCurrentTheme("globe.svg")
					elif data==-1:
						icon=IconFromCurrentTheme("globe.svg")
					else:
						pixmap=QPixmap()
						pixmap.loadFromData(base64.b64decode(data))
						pixmap=pixmap.scaled(ICONWIDTH,ICONWIDTH,Qt.KeepAspectRatio,Qt.FastTransformation)
						icon=QIcon(pixmap)
					
					self.parent().lock.lock()
					if "Table" in self.parent().objectName():
						try:
							item_list=self.parent().findItems(url,Qt.MatchExactly)
							self.parent().item(item_list[0].row(),3).setIcon(icon)
						except:
							pass
					elif "List" in self.parent().objectName():
						try:
							if url==self.parent().item(self.row).toolTip().split("\n")[0]:
								self.parent().item(self.row).setIcon(icon)
						except:
							pass
					self.parent().lock.unlock()
					return

		data=self.Headquarter.cache.get(cache_name)
		
		# cache中没有，或者要刷新
		if data==None or self.force==True:
			# 文件
			if self.file["type"]!=2:
				url=os.path.join(self.Headquarter.library_base,url).replace("\\","/")
				
				if self.file["type"]==0 or ext not in image_extension:
					# folder或者其他类型文件
					file_info=QFileInfo(url)
					icon=QFileIconProvider().icon(file_info)
				else:
					if os.path.exists(url):
						if os.path.getsize(url)/1024/1024>50 or ext=="gif":
							# 图片大于50mb就算了
							file_info=QFileInfo(url)
							icon=QFileIconProvider().icon(file_info)
						else:
							# 图片
							pixmap=QPixmap()
							pixmap.load(url)
							pixmap=pixmap.scaled(ICONWIDTH,ICONWIDTH,Qt.KeepAspectRatio,Qt.FastTransformation)

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
					else:
						icon=QIcon()
			
			# link
			elif self.file["type"]==2:
				data=GetWebFavIcon(url)
				if data!=None:
					data=base64.b64encode(data)

					self.Headquarter.qlock.lock()
					self.Headquarter.cache[cache_name]=data
					self.Headquarter.qlock.unlock()
					
					pixmap=QPixmap()
					pixmap.loadFromData(base64.b64decode(data))
					pixmap=pixmap.scaled(ICONWIDTH,ICONWIDTH,Qt.KeepAspectRatio,Qt.FastTransformation)
					icon=QIcon(pixmap)
				else:
					#一些防爬的就算了，标记-1，制定icon的时候给globe就行了
					self.Headquarter.qlock.lock()
					self.Headquarter.cache[cache_name]=-1
					self.Headquarter.qlock.unlock()
					
					icon=IconFromCurrentTheme("globe.svg")
			
			self.parent().lock.lock()
			if "Table" in self.parent().objectName():
				try:
					item_list=self.parent().findItems(url,Qt.MatchExactly)
					self.parent().item(item_list[0].row(),3).setIcon(icon)
				except:
					pass
			elif "List" in self.parent().objectName():
				try:
					if url==self.parent().item(self.row).toolTip().split("\n")[0]:
						self.parent().item(self.row).setIcon(icon)
				except:
					pass
			self.parent().lock.unlock()
			return
		
		# cache中有
		else:
			if data==-1: #一些防爬的就算了，标记-1，制定icon的时候给globe就行了
				icon=IconFromCurrentTheme("globe.svg")
			else:
				if type!=2:
					url=os.path.join(self.Headquarter.library_base,url).replace("\\","/")
					# convert bytes to QPixmap
					pixmap=QPixmap()
					ba = QByteArray(data)
					pixmap.loadFromData(ba, ext)
					pixmap=pixmap.scaled(ICONWIDTH,ICONWIDTH,Qt.KeepAspectRatio,Qt.FastTransformation)
					icon=QIcon(pixmap)
				else:
					# convert bytes to QPixmap
					pixmap=QPixmap()
					pixmap.loadFromData(base64.b64decode(data))
					pixmap=pixmap.scaled(ICONWIDTH,ICONWIDTH,Qt.KeepAspectRatio,Qt.FastTransformation)
					icon=QIcon(pixmap)
			
			self.parent().lock.lock()
			if "Table" in self.parent().objectName():
				try:
					item_list=self.parent().findItems(url,Qt.MatchExactly)
					self.parent().item(item_list[0].row(),3).setIcon(icon)
				except:
					pass
			elif "List" in self.parent().objectName():
				try:
					if url==self.parent().item(self.row).toolTip().split("\n")[0]:
						self.parent().item(self.row).setIcon(icon)
				except:
					pass
			self.parent().lock.unlock()
			return


from session.LobbySession import LobbySession
from widget.Ui_FileTab import Ui_FileTab
class FileTab(Ui_FileTab,QWidget):

	fileClicked=Signal()
	fileDropped=Signal(list,list)
	fileDelete=Signal()

	def eventFilter(self, watched: QObject, event:QKeyEvent) -> bool:
		if event.type()==QEvent.KeyPress:
			if event.key()==Qt.Key_Return:
				self.openFile()
		return False # 这里是让继续延续event的处理，不要被filter掉了
	
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.setMinimumHeight(150)

		self.file_list=[]

		def slot1(url_list,file_list):
			self.fileDropped.emit(url_list,file_list)
		
		self.fileTable.fileDropped.connect(slot1)
		self.fileList.fileDropped.connect(slot1)
		
		def slot2():
			self.fileClicked.emit()
		
		self.fileTable.itemClicked.connect(slot2)
		self.fileList.itemClicked.connect(slot2)

		def slot3(o):
			count=len(o.selectionModel().selectedRows())
			if count>0:
				self.label_info.setText("%s item selected"%count)
			else:
				self.label_info.clear()

		self.fileTable.selectionModel().selectionChanged.connect(lambda:slot3(self.fileTable))
		self.fileList.selectionModel().selectionChanged.connect(lambda:slot3(self.fileList))

		def slot4():
			self.fileDelete.emit()
		self.fileTable.fileDelete.connect(slot4)
		self.fileList.fileDelete.connect(slot4)

		self.setStyleSheet("""
		QPushButton{
			border: none;
			background:transparent;
			max-height: 24px;
			min-height: 24px;
			min-width: 24px;
			max-width: 24px;
		}

		QLabel{
			font-size: 12pt;
		}
		""")

		self.fileTable.itemDoubleClicked.connect(self.openFile)
		self.fileList.itemDoubleClicked.connect(self.openFile)

		self.pushButton_table.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
		self.pushButton_table.clicked.connect(lambda:self.setFileList(self.file_list))
		self.pushButton_table.setIcon(IconFromCurrentTheme("list.svg"))
		self.pushButton_list.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
		self.pushButton_list.clicked.connect(lambda:self.setFileList(self.file_list))
		self.pushButton_list.setIcon(IconFromCurrentTheme("image.svg"))

		# sort取消，手动重新赋值
		self.fileTable.sortReset.connect(lambda:self.setFileList(self.file_list))

		self.installEventFilter(self)
	
	def setHeadquarter(self,Headquarter: LobbySession):
		self.Headquarter=Headquarter
		self.fileTable.Headquarter=Headquarter
		self.fileList.Headquarter=Headquarter
	
	def currentRow(self):
		if self.stackedWidget.currentIndex()==0:
			row=self.fileTable.currentRow()
		else:
			row=self.fileList.currentRow()
		return row
	
	def selectRow(self,row):
		if self.stackedWidget.currentIndex()==0:
			self.fileTable.selectRow(row)
		else:
			self.fileList.setCurrentRow(row)
	
	def currentFile(self):
		row=self.currentRow()
		if row==-1:
			return None
		
		if self.stackedWidget.currentIndex()==0:
			date=QDate().fromString(self.fileTable.item(row,1).text(),"yyyy.M.d")
			name=self.fileTable.item(row,3).text()
		else:
			if self.fileList.item(row).toolTip().split("\n")[0][:4]=="http":
				name=self.fileList.item(row).text()
				date=QDate().fromString(name[name.rfind("|")+1:][1:-1],"yyyy.M.d")
				name=name[:name.rfind("|")]
			else:
				y,m,d=self.Headquarter.extractFileURL(self.fileList.item(row).toolTip().split("\n")[0]).split("/")[:3]
				date=QDate(int(y),int(m),int(d))
				name=self.fileList.item(row).text()

		return date,name

	def setFileList(self,file_list):
		
		def FileTableSetFileList(file_list):
			"""设置filetable为file_list

			Args:
				file_list (list): 元素具有y,m,d,name,type,url属性
			"""
			
			self.fileTable.StoreTableStatus()
			self.fileTable.Clear()

			self.fileTable.lock.lock()

			self.fileTable.thread_list=[]

			row=0
			# 更新icon时防止多线程在刷新完列表之前就去更新
			for file in file_list:

				y=file["y"]
				m=file["m"]
				d=file["d"]
				type=file["type"]
				name=file["name"]
				url=file["url"]
				
				if type==0:
					ext="folder"
					url=os.path.join(self.Headquarter.library_base,url).replace("\\","/")
				elif type==1:
					url=os.path.join(self.Headquarter.library_base,url).replace("\\","/")
					ext=os.path.splitext(url)[1].lower()[1:]
				elif type==2:
					ext="link"

				loading_thread=LoadThumbnailThread(self.fileTable,self.Headquarter,file,row)
				self.fileTable.thread_list.append(loading_thread)
				loading_thread.finished.connect(loading_thread.deleteLater)
				loading_thread.start()
				
				name_item=QTableWidgetItem(name)
				name_item.setToolTip(self.Headquarter.getLibraryFileTooltip(QDate(y,m,d), name))
				self.fileTable.addRow(row,[QTableWidgetItem(str(type)),QTableWidgetItem("%02d.%02d.%02d"%(y,m,d)),QTableWidgetItem(ext),name_item,QTableWidgetItem(url)])
				self.fileTable.setRowHeight(row,32)
				row+=1
			
			self.label_count.setText("%s item  |  "%row)
			
			self.fileTable.lock.unlock()
			self.fileTable.RestoreTableStatus()

		def FileListSetFileList(file_list):
			"""设置filetable为file_list

			Args:
				file_list (list): 元素具有y,m,d,name,type,url属性
			"""
			
			selected_index=self.fileList.selectedIndexes()

			self.fileList.clear()

			self.fileList.lock.lock()

			self.fileList.thread_list=[]

			row=0
			# 更新icon时防止多线程在刷新完列表之前就去更新
			for file in file_list:

				y=file["y"]
				m=file["m"]
				d=file["d"]
				type=file["type"]
				name=file["name"]

				loading_thread=LoadThumbnailThread(self.fileList,self.Headquarter,file,row)
				self.fileList.thread_list.append(loading_thread)
				loading_thread.finished.connect(loading_thread.deleteLater)
				loading_thread.start()
				
				if type==2:
					item=QListWidgetItem(name+"|[%s.%s.%s]"%(y,m,d))
				else:
					item=QListWidgetItem(name)

				item.setToolTip(self.Headquarter.getLibraryFileTooltip(QDate(y,m,d), name))
				self.fileList.addItem(item)
				row+=1
			
			self.label_count.setText("%s item  |  "%row)
			
			self.fileList.lock.unlock()
			
			for index in selected_index:
				self.fileList.selectionModel().select(index,QItemSelectionModel.Select | QItemSelectionModel.Rows)
		
		self.label_info.clear()
		self.file_list=file_list
		
		if self.stackedWidget.currentIndex()==0:
			FileTableSetFileList(file_list)
		else:
			FileListSetFileList(file_list)
		
	def setFocus(self):
		super().setFocus()
		if self.stackedWidget.currentIndex()==0:
			self.fileTable.setFocus()
		else:
			self.fileList.setFocus()


	def openFile(self):

		if self.fileTable.currentRow()==-1 and self.fileList.currentRow()==-1:
			return

		if self.stackedWidget.currentIndex()==0:
			url=self.fileTable.item(self.fileTable.currentRow(),4).text()
		else:
			url=self.fileList.item(self.fileList.currentRow()).toolTip().split("\n")[0]

		if url[:4]!="http":
			try:
				Open_Explorer(url, False)
			except Exception as e:
				DTFrame.DTMessageBox(self.window(),"Warning","Could not open file! Try running Check Library.\n\n%s"%e,DTIcon.Warning())
		else:
			Open_Website(url)
	
	def Clear(self):
		if self.stackedWidget.currentIndex()==0:
			self.fileTable.Clear()
		else:
			self.fileList.Clear()
	
	def clearSelection(self):
		if self.stackedWidget.currentIndex()==0:
			self.fileTable.clearSelection()
		else:
			self.fileList.clearSelection()