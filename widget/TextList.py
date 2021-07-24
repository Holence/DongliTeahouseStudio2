# # --
from DTPySide import *

from session.LobbySession import LobbySession
class TextList(QListWidget):

	textDropped=Signal(list)

	def startDrag(self, actions:Qt.DropActions):
		######################################################################
		# MIME通信规则：
		# 
		# data/Key: bytes("DTT","utf-8")
		# 作为钥匙，在dragEnterEvent中检验，防止其他类型的drop进来
		# 
		# text_list: []
		# 
		######################################################################
		
		indexes = self.selectedIndexes()
		mime = self.model().mimeData(indexes)

		text_list=[]
		for model_index in self.selectionModel().selectedRows():
			row=model_index.row()
			text_list.append(self.text_list[row])
		
		#防止拖到自己的里面
		mime.setObjectName(self.objectName())
		mime.setData("Key",bytes("DTT","utf-8"))
		mime.setData("TextList",bytes(json.dumps(text_list),encoding="utf-8"))
		
		drag = QDrag(self)
		drag.setPixmap(QIcon(":/icon/white/white_align-left.svg").pixmap(32,32))
		drag.setMimeData(mime)
		drag.exec_(actions)
	
	def dragEnterEvent(self, event:QDragEnterEvent):
		if "DiaryTextList" in self.objectName() and "DiaryTextList" in event.mimeData().objectName():
			if self.objectName()==event.mimeData().objectName():
				# DiaryTextList类的允许拖到自己
				event.acceptProposedAction()
			else:
				# 不允许DiaryTextList之间互相拖
				event.ignore()
		elif "DiaryTextList" in self.objectName() and "DiaryTextList" not in event.mimeData().objectName():
			# 不允许其他地方拖到DiaryTextList
			event.ignore()
		elif event.mimeData().objectName()!=self.objectName():
			if event.mimeData().data("Key")==bytes("DTT","utf-8"):
					# 其他地方随便拖
					event.acceptProposedAction()
	
	def dragMoveEvent(self, event: QDragMoveEvent):
		# 统一一下
		super().dragMoveEvent(event) # 拖放排序时侦测扔到哪里时的事件
		event.acceptProposedAction()
	
	def dropEvent(self, event:QDropEvent):
		super().dropEvent(event) # 拖放排序扔下时的事件
		if "DiaryTextList" in self.objectName():
			self.textDropped.emit([])
		else:
			text_list=json.loads((event.mimeData().data("TextList").data().decode("utf-8")))
			self.textDropped.emit(text_list)
	
	def __init__(self, parent):
		super().__init__(parent=parent)
		self.setStyleSheet("QListWidget{ font-size: 18pt; } QListWidget::item{ border: 2px solid #8C6BBB; border-radius: 10px;}")
		self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
		self.verticalScrollBar().setSingleStep(18)
	
		self.setAutoScroll(False)
		self.setEditTriggers(QAbstractItemView.NoEditTriggers)
		
		self.setDragEnabled(True)
		self.setDragDropMode(QAbstractItemView.DragDrop)

		self.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.setMovement(QListView.Free)
		self.setResizeMode(QListView.Adjust)
		self.setSpacing(15)
		self.setWordWrap(True)
	
	def setHeadquarter(self,Headquarter: LobbySession):
		self.Headquarter=Headquarter
	
	def setTextList(self,Type,*args):
		self.clear()
		self.text_list=[]

		if Type=="Diary":
			date=args[0]
			index=0
			for line in self.Headquarter.getDiaryDay(date):
				have_concept=int(line["concept"]!=[])
				have_file=int(line["file"]!=[])
				item=QListWidgetItem(line["text"])
				item.setIcon(QIcon("./icon/line_%s%s.png"%(have_concept,have_file)))
				self.addItem(item)
				
				self.text_list.append({
					"y":date.year(),
					"m":date.month(),
					"d":date.day(),
					"index":index
				})
				index+=1
			
		elif Type=="Concept":
			id_list=args[0]

			day_list=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
			diary_data=self.Headquarter.getDiaryData()
			for year in diary_data:
				for month in diary_data[year]:
					for day in diary_data[year][month]:
						index=0
						for line in diary_data[year][month][day]:
							if List_Intersection(line["concept"],id_list)!=[]:
								text="%s.%s.%s %s\n\n"%(year,month,day,day_list[QDate(int(year),int(month),int(day)).dayOfWeek()-1])+line["text"]
								item=QListWidgetItem(text)
								self.addItem(item)
								self.text_list.append({
									"y":int(year),
									"m":int(month),
									"d":int(day),
									"index":index
								})
							index+=1
			
		elif Type=="Library":
			file_dict=args[0]
			day_list=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
			diary_data=self.Headquarter.getDiaryData()
			for year in diary_data:
				for month in diary_data[year]:
					for day in diary_data[year][month]:
						index=0
						for line in diary_data[year][month][day]:
							if List_Intersection_Full(line["file"],[file_dict])!=[]:
								text="%s.%s.%s %s\n\n"%(year,month,day,day_list[QDate(int(year),int(month),int(day)).dayOfWeek()-1])+line["text"]
								item=QListWidgetItem(text)
								self.addItem(item)
								self.text_list.append({
									"y":int(year),
									"m":int(month),
									"d":int(day),
									"index":index
								})
							index+=1