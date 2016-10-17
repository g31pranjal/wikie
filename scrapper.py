import threading
import logging
import requests


# class ScrappingThread(threading.Thread) :

# 	def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None) :
# 		threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)
# 		self.args = args
# 		self.fIO = kwargs['fileIO']
# 		return 

# 	def run(self) :
# 		# initializing thread statement
		
# 		logging.debug("# initiating ...");	
		
# 		inf = self.fIO.resolveURL()

# 		logging.debug("# Resolved URL entry : " + str(inf))

# 		if(inf is not None) :
# 			#scrap content from the URL
# 			logging.debug('# Downloading the source : https://en.wikipedia.org' + inf['url'] )
# 			page = requests.get('https://en.wikipedia.org' + inf['url'])
# 			raw_text = page.text.encode('utf-8')

# 			fhandle = open('repo/'+inf['docid']+'.raw', 'w')
# 			fhandle.write(raw_text)
# 			fhandle.close()

# 			self.fIO.crawlResult(1 ,inf['docid'])

# 			# create a list of all the (not unique) URLS that can be reached from the current page

# 			lst = ['/wiki/China','/wiki/Peru','/wiki/Argentina','/wiki/Brazil','/wiki/Mexico','/wiki/Canada','/wiki/new_york','/wiki/Bhutan','/wiki/Amazon','/wiki/Google','/wiki/San_fransisco','/wiki/London','/wiki/Antarctica','/wiki/Australia','/wiki/Japan','/wiki/Russia']
# 			self.fIO.addPages(inf['docid'], lst)

		
# 		logging.debug("... end ...")
# 		return



