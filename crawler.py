import threading
import logging
from lxml import html
import requests


class CrawlingThread(threading.Thread) :

	def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None) :
		threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)
		self.args = args
		self.fIO = kwargs['fileIO']
		return 

	def run(self) :
		# initializing thread statement
		
		logging.debug("# initiating ...");	
		
		URL = self.fIO.resolveURL()

		print URL

		if(URL is not None) :
			#scrap content from the URL
			logging.debug('# Downloading the source : ' + URL['tup'][0] )
			page = requests.get('https://en.wikipedia.org/wiki/India')
			raw_text = page.text.encode('utf-8')

			print raw_text

		
		logging.debug("... end ...")
		return

