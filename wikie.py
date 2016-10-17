import os
import time
import dbOps
import crawler as ct
import scrapper as st
import logging
import threading

pid = os.getpid()
drc = os.getcwd()

os.system('cls' if os.name == 'nt' else 'clear')
print "\n\n"
print "wikie 1.o"
print "-------------------------------------------------------------------------"
print "process id : " + str(pid) + ", cwd : "  + str(drc) 
print "\n\n"

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-20s) %(message)s',)




logging.debug("Main thread started. Starting child thread !..\n")

fIO = dbOps.FileOperations()
while(True) :
	time.sleep(1)
	if(len(threading.enumerate()) <= 4 ) :
		t = ct.CrawlingThread(kwargs = {'fileIO' : fIO})
		t.start()
		#u = st.ScrappingThread(kwargs = {'fileIO' : fIO})
		#u.start()
			
	


