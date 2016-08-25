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

	def returnURL(self) :
		logging.debug("# trying to acquire the lock for Control Files IO Operations");
		self.lock.acquire()

		statFiles = os.listdir('./cntrl/');
		statFiles = [x for x in statFiles if re.match('repo\.[0-9]+\.stats', x)]
		statFiles.sort(reverse = True)

		ePointer = -1
		repo = ''

		for f in statFiles :
			repo = f
			logging.debug("# opening stat file : " + './cntrl/' + f)
			fhandle = open('./cntrl/' + f, 'r')
			stats = eval(fhandle.read());
			# print stats
			logging.debug('# ' + str(len(stats['fatality'])) + ' fatality(s) found.. ')
			
			if(len(stats['fatality']) > 0) :
				ePointer = stats['fatality'][0]
				stats['fatality'].remove(ePointer)
				
				if(ePointer > stats['entries']) :
					logging.debug('CORRECTED ERROR :: Invalid fatality entry in file ' + './cntrl/' + f)
					ePointer = -1
				else :
					logging.debug('# Setting Effective pointer to ' + str(ePointer) + ' in file ' + './cntrl/' + f)

			else :
				if(stats['pointer'] > stats['entries']) : 	
					pass
				else :
					ePointer = stats['pointer']
					stats['pointer'] += 1
					logging.debug('# Setting Effective pointer to ' + str(ePointer) + ' in file ' + './cntrl/' + f)

			fcor = open('./cntrl/' + f, 'w')
			fcor.write(str(stats))
			fcor.close()

			if(ePointer != -1) : 
				break

		if(ePointer == -1) :
			logging.debug('# No URL left to crawl. Exiting ... ')
		else :
			logging.debug('')
			pass

		try : 
			pass
		
		finally :
			self.lock.release()



logging.debug("Main thread started. Starting child thread !..\n")

fIO = FileOperations()

while(True) :
	time.sleep(1)
	if(len(threading.enumerate()) < 5 ) :
		t = ct.CrawlingThread(kwargs = {'fileIO' : fIO})
		t.start()
	



