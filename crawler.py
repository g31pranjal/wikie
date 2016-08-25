import threading
import logging



class CrawlingThread(threading.Thread) :

	def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None) :
		threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)
		self.args = args
		self.fIO = kwargs['fileIO']
		return 

	def run(self) :
		# initializing thread statement
		
		logging.debug("# initiating ...");	
		URL = self.fIO.returnURL()
		
		logging.debug("... end ...")
		return

