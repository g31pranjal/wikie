import os
import time
import threading
import logging
import crawler as ct
import re

pid = os.getpid()
drc = os.getcwd()

os.system('cls' if os.name == 'nt' else 'clear')
print "\n\n"
print "crawler 0.0.1"
print "-------------------------------------------------------------------------"
print "process id : " + str(pid) + ", cwd : "  + str(drc) 
print "\n\n"

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-12s) %(message)s',)




class FileOperations(object) :
	def __init__(self) :
		self.lock = threading.Lock()

	def resolveURL(self) :
		logging.debug("# trying to acquire the lock for Control Files IO Operations");
		self.lock.acquire()

		ret = None
		try : 
			ePointer = -1

			# reading the main stats file
			fhandle = open('./cntrl/main.stats', 'r')
			stats = eval(fhandle.read());
			logging.debug('# file status : ' + str(stats));

			if len(stats['fatality']) > 0 :
				logging.debug('# fatal entry found in main.stats')
				ongoing = stats['fatality'][0]
				stats['fatality'].remove(ongoing)
				fhandle = open('./cntrl/main.stats', 'w')
				fhandle.write(str(stats))

			else :
				ongoing = stats['ongoing']

			if(ongoing <= stats['files'] ) :
				
				fid = ongoing
				f = 'repo.' + ongoing + '.stats'

				logging.debug("# opening stat file : " + './cntrl/' + f)
				fhandle = open('./cntrl/' + f, 'r')
				repostats = eval(fhandle.read());
		 		logging.debug('# ' + str(len(repostats['fatality'])) + ' fatality(s) found.. ')
				
				# clear fatalaties first, in case of any
				if(len(repostats['fatality']) > 0) :
					arr = repostats['fatality']
					ePointer = arr[0]
					repostats['fatality'].remove(ePointer)

					fhandle = open('./cntrl/' + f, 'w')
					fhandle.write(str(repostats))
					
					logging.debug('# Fatal entry : '+ str(ePointer))
					
					if(ePointer > repostats['entries']) :
						logging.debug('CORRECTED ERROR :: Invalid fatality entry in file ' + './cntrl/' + f)
						ePointer = -1
					else :
						logging.debug('# Setting Effective pointer to ' + str(ePointer) + ' in file ' + './cntrl/' + f)

				# take the pointer and increment by 1
				else :
					if(repostats['pointer'] > repostats['entries']) :
						logging.debug('# pointer ended, updating main.stats !') 	
						
						fhandle = open('./cntrl/main.stats', 'w')
						
						num = 0
						for i in range(0,4) :
							num = num*26 + (ord(fid[i:i+1]) - 97)
						num += 1

						code = ''
						for i in range(3, -1, -1) :
							code = code + chr(num/(26**i) + 97)
							num %= (26**i)

						stats['ongoing'] = code
						fhandle.write(str(stats))

					else :
						ePointer = repostats['pointer']
						repostats['pointer'] += 1
						logging.debug('# Setting Effective pointer to ' + str(ePointer) + ' in file ' + './cntrl/' + f)

				if(ePointer == -1) :
					logging.debug('# No URL left to crawl. Exiting ... ')
					
				else :
					# fetch the URL pointed by ePointer from the file
					repoFile = 'url.repo.' + fid

					logging.debug('Fetching URL and docID from ' + repoFile)

					fRepo = open('./cntrl/' + repoFile, 'r')
					tup = eval((fRepo.readlines()[ePointer - 1: ePointer][0]).split('\n')[0])

					fhandle = open('./cntrl/' + f, 'w')
					fhandle.write(str(repostats))

					logging.debug(tup)

					ret = {'fid' : fid, 'tup' : tup, 'ep' : ePointer}
					

		except Exception :
			logging.debug('# Error in fetching URL. Exiting ...')
		
		finally :
			self.lock.release()
			return ret






logging.debug("Main thread started. Starting child thread !..\n")

fIO = FileOperations()

while(True) :
	time.sleep(1)
	if(len(threading.enumerate()) <= 1 ) :
		t = ct.CrawlingThread(kwargs = {'fileIO' : fIO})
		t.start()
	



