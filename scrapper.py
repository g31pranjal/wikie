import threading
import logging
import requests
from bs4 import BeautifulSoup as bs
from HTMLParser import HTMLParser

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-20s) %(message)s',)

class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.strict = False
		self.convert_charrefs= True
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def strip_tags(html):
	s = MLStripper()
	s.feed(html)
	return s.get_data()


class ScrappingThread(threading.Thread) :

	def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None) :
		threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)
		self.args = args
		self.fIO = kwargs['fileIO']
		return 

	def run(self) :
		# initializing thread statement
		
		logging.debug("# initiating ...");	
		doc = self.fIO.getDocIDforHTMLRemoval()

		try :
			
			logging.debug("# DOCID : " + str(doc))

			if(doc is not None) :
				#scrap content from the URL
				logging.debug('# Fetching raw page : ' + doc )
				
				fhandle = open('repo/'+doc+'.raw', 'r')
				a = fhandle.read()

				soup = bs(a, 'html.parser')
				x = soup.find("div", {'id' : 'mw-content-text'}, { 'class' : 'mw-content-ltr' })

				# remove all hatnotes
				for child in x.find_all("div", class_="hatnote") :
					child.extract()

				# remove infobox
				for child in x.find_all("table", class_="infobox") :
					child.extract()

				# remove infobox
				for child in x.find_all("table", class_="plainlinks") :
					child.extract()

				# remove table of contents
				for child in x.find_all("div", {'id' : 'toc'}) :
					child.extract()

				# remove all image placeholders
				for child in x.find_all("div", class_="thumb") :
					child.extract()

				# remove all references
				for child in x.find_all("div", class_="reflist") :
					child.extract()

				# remove all references
				for child in x.find_all("ol", class_="references") :
					child.extract()

				# remove all references
				for child in x.find_all("script") :
					child.extract()

				# remove all references
				for child in x.find_all("noscript") :
					child.extract()



				logging.debug('# Writing the new file !' )

				fw = open('cleaned/'+doc+'.txt', 'w')
				fw.write(  strip_tags(str(x))  )

				logging.debug('# Written the new file' )

				self.fIO.cleaningResult(1 ,doc)
			
		except Exception, e :

			print e
			
			self.fIO.cleaningResult(0 ,doc)

		
		logging.debug("... end ...")


		return



