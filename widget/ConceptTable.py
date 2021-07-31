# # --
from DTPySide import *

from session.LobbySession import LobbySession
class ConceptTable(DTWidget.DTHorizontalTabel):
	
	conceptClicked=Signal(int)
	conceptDoubleClicked=Signal(int)
	conceptDropped=Signal(list)

	def startDrag(self, actions:Qt.DropActions):
		######################################################################
		# MIME通信规则：
		# 
		# data/Key: bytes("DTC","utf-8")
		# 作为钥匙，在dragEnterEvent中检验，防止其他类型的drop进来
		# 
		# text/id_list: 495 9961 1
		# 其实不用这个，drop进来也完全可以和表格fit，只是这样方便处理数据，不用我再去一个个识别加进来的item了
		######################################################################
		
		indexes = self.selectedIndexes()
		mime = self.model().mimeData(indexes)
		
		id_list = ""
		for model_index in self.selectionModel().selectedRows():
			row=model_index.row()
			id=str(int(self.item(row,0).text()))
			id_list += id+" "
		
		#防止拖到自己的里面
		mime.setObjectName(self.objectName())
		mime.setData("Key",bytes("DTC","utf-8"))
		mime.setText(id_list)
		
		drag = QDrag(self)
		drag.setPixmap(QIcon(":/icon/white/white_hash.svg").pixmap(32,32))
		drag.setMimeData(mime)
		drag.exec_(actions)
	
	def dragEnterEvent(self, event:QDragEnterEvent):
		if event.mimeData().objectName()!=self.objectName():
			if event.mimeData().data("Key")==bytes("DTC","utf-8"):
					event.acceptProposedAction()
	
	def dragMoveEvent(self, event: QDragMoveEvent):
		# 统一一下
		event.acceptProposedAction()
	
	def dropEvent(self, event:QDropEvent):
		id_list=list(map(int,event.mimeData().text().split()))
		self.conceptDropped.emit(id_list)

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.setMinimumHeight(150)
		self.setColumn(["ID","Name"])

		self.itemClicked.connect(self.itemClickedSlot)
		self.itemDoubleClicked.connect(self.itemDoubleClickedSlot)
	
	def setHeadquarter(self,Headquarter: LobbySession):
		self.Headquarter=Headquarter
		self.setStyleSheet("font-family: %s"%self.Headquarter.app.Font().family())
	
	def itemClickedSlot(self):
		"""双击table中的元素，emit附带concept id的conceptClicked信号（用于出去跳转展示concept）
		"""
		id=int(self.item(self.currentRow(),0).text())
		self.conceptClicked.emit(id)

	def itemDoubleClickedSlot(self):
		"""双击table中的元素，emit附带concept id的conceptClicked信号（用于出去跳转展示concept）
		"""
		id=int(self.item(self.currentRow(),0).text())
		self.conceptDoubleClicked.emit(id)

	def appendConcept(self, id:int, name:str):

		self.StoreTableStatus()

		id=f"%{len(str(self.rowCount()))}s"%id
		self.addRow(self.rowCount(),[QTableWidgetItem(id),QTableWidgetItem(name)])

		self.RestoreTableStatus()
		self.clearSelection()
		self.selectRow(self.rowCount()-1)
	
	def setConceptIDList(self, concept_id_list):
		"""设置concepttable为concept_id_list对应的concept_list，适用于diary、file的concept链接列表，以及concept的parent、relative的concept链接列表

		Args:
			concept_id_list (list): 是concept id的列表
		"""		
		self.StoreTableStatus()
		self.Clear()

		id_str_width=len(str(len(concept_id_list)))
		row=0
		for concept_id in concept_id_list:
			concept=self.Headquarter.getConcept(concept_id)
			id=f"%{id_str_width}s"%concept["id"]
			name=concept["name"]
			self.addRow(row,[QTableWidgetItem(id),QTableWidgetItem(name)])
			row+=1

		self.RestoreTableStatus()