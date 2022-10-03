# # --
from DTPySide import *

from session.LobbySession import LobbySession
class ConceptSearch(QLineEdit):

	conceptAdd=Signal(list)

	def __init__(self, parent):
		super().__init__(parent=parent)
		
		self.textEdited.connect(self.showDropList)

		self.search_list=QStringListModel(self)
		self.Completer=QCompleter(self.search_list,self)
		self.Completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
		self.setCompleter(self.Completer)

		def slot(s):
			id=int(s.split("|")[0])
			self.conceptAdd.emit([id])
			
			#记录选concept的频度
			if self.Headquarter.concept_frequency.get(id)==None:
				self.Headquarter.concept_frequency[id]=1
			else:
				self.Headquarter.concept_frequency[id]+=1
			
			QTimer.singleShot(0, self.clear)
		
		self.Completer.activated.connect(slot)

	
	def setHeadquarter(self,Headquarter: LobbySession):
		self.Headquarter=Headquarter

	def showDropList(self,search):
		id_list=self.Headquarter.getConceptIDList(search,rank=True)
		self.search_list.setStringList([str(id)+" | "+self.Headquarter.getConcept(id)["name"] for id in id_list])