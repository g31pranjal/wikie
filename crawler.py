import threading
import logging
import requests
from bs4 import BeautifulSoup as bs

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-20s) %(message)s',)

class CrawlingThread(threading.Thread) :

	def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None) :
		threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)
		self.args = args
		self.fIO = kwargs['fileIO']
		return 

	def run(self) :
		# initializing thread statement
		
		logging.debug("# initiating ...");	
		
		inf = self.fIO.resolveURL()

		logging.debug("# Resolved URL entry : " + str(inf))

		if(inf is not None) :
			#scrap content from the URL
			logging.debug('# Downloading the source : https://en.wikipedia.org' + inf['url'] )
			page = requests.get('https://en.wikipedia.org' + inf['url'])
			
			if page.status_code is 200 :
				raw_text = page.text.encode('utf-8')

				fhandle = open('repo/'+inf['docid']+'.raw', 'w')
				fhandle.write(raw_text)
				fhandle.close()

				self.fIO.crawlResult(1 ,inf['docid'])
			
				soup = bs(raw_text, 'html.parser')
				x = soup.find("div", {'id' : 'mw-content-text'}, { 'class' : 'mw-content-ltr' })

				lst = []

				for a_tags in x('a') :
					lst.append(str(a_tags.get('href')))

				# must be an internal link only
				lst = [x for x in lst if x.startswith("/wiki")]

				# remove words which are not to be parsed
				bad_words = ['list', 'List', 'svg', 'png', 'disambiguation', 'file', 'File', ':', '#']
				for word in bad_words :
					lst = [x for x in lst if word not in x]

				self.fIO.addPages(inf['docid'], lst)

			else :
				self.fIO.crawlResult(0 ,inf['docid'])

		
		logging.debug("... end ...")
		return



