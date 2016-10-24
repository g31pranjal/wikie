import threading
import logging
import sqlite3 as sql
import random

class FileOperations(object) :
	def __init__(self) :
		self.lock = threading.Lock()

	def resolveURL(self) :
		logging.debug("# trying to acquire the lock for Control Files IO Operations");
	 	self.lock.acquire()

	 	ret = {}

	 	conn = sql.connect('cntrl/test.db')
	 
		cursor = conn.cursor()

	 	#cursor.execute("SELECT * from pages WHERE done = 0 AND processing = 0")
	 	cursor.execute("SELECT * from pages WHERE done = 3 AND `processing` = 0")
	 	
	 	r = cursor.fetchone()

	 	if r is not None :
	 		cursor.execute("UPDATE pages SET processing = 1 WHERE docid = '" + r[1] +"'")
	 		conn.commit()
	 		ret = { 'url' : r[0] , 'docid' : r[1] }
	 	else :
	 		ret = None

	 	self.lock.release()

	 	return ret



	def getDocIDforHTMLRemoval(self) :
		logging.debug("# trying to acquire the lock");
	 	self.lock.acquire()

	 	ret = {}

	 	conn = sql.connect('cntrl/test.db')
	 	cursor = conn.cursor()

	 	cursor.execute("SELECT * from pages WHERE done = 1 AND html_freed = 0 AND scrap_d = 0")
	 	r = cursor.fetchone()

	 	if r is not None :
	 		cursor.execute("UPDATE pages SET html_freed = 1 WHERE docid = '" + r[1] +"'")
	 		conn.commit()
	 		ret = r[1]
	 	else :
	 		ret = None

	 	self.lock.release()

	 	return ret




	def crawlResult(self, status, docid) :

		self.lock.acquire()

		conn = sql.connect('cntrl/test.db')
	 	
		cursor = conn.cursor()

		logging.debug("# Setting crawl result to " + docid +" , status : " + str(status) + "!... ")

		if status == 1 :
			cursor.execute("UPDATE pages SET done = 1, processing = 0 where docid = '" + docid + "'")
		else :
			cursor.execute("UPDATE pages SET done = 0, processing = 0 where docid = '" + docid + "'")

		conn.commit()

		self.lock.release()
		

	def cleaningResult(self, status, docid) :

		self.lock.acquire()

		conn = sql.connect('cntrl/test.db')
	 	
		cursor = conn.cursor()

		logging.debug("# Setting crawl result to " + docid +" , status : " + str(status) + "!... ")

		if status == 1 :
			cursor.execute("UPDATE pages SET scrap_d = 1, html_freed = 0 where docid = '" + docid + "'")
		else :
			cursor.execute("UPDATE pages SET scrap_d = 2, html_freed = 0 where docid = '" + docid + "'")

		conn.commit()

		self.lock.release()

	def addPages(self, parent, childList) :

		self.lock.acquire()

		conn = sql.connect('cntrl/test.db')
	 	
		cursor = conn.cursor()

		logging.debug("# Adding the child nodes ! : number of children : " + str(len(childList)))

		s = set()

		for entry in childList :
			# logging.debug("# Processing child : " + entry + ".")
			cursor.execute("SELECT * from pages where url = '" + entry + "'")

			r = cursor.fetchone()

			if r is None :
				# logging.debug("# The child is not in the scrapping queue. Arranging to add ... ")

				docid = generateDocID()
				cursor.execute("SELECT * from pages WHERE docid = '" + docid + "'")
				r = cursor.fetchone()
				
				while r is not None : 
					docid = generateDocID()
					cursor.execute("SELECT * from pages WHERE docid = '" + docid + "'")
					r = cursor.fetchone()

				cursor.execute("INSERT into pages VALUES ('"+entry+"', '"+docid+"', 0, 0, 0, 0)")
			else :
				# logging.debug("# The child already there !")
				docid = r[1]

			tmp = ( parent, docid )
			s.add(tmp)

		while len(s) is not 0 :
			tmp = s.pop()
			cursor.execute("INSERT INTO edges VALUES ('"+tmp[0]+"', '"+tmp[1]+"')")





		conn.commit()

		self.lock.release()



def generateDocID() :
	return chr(int(random.uniform(0,25.99)) + 97) + chr(int(random.uniform(0,25.99)) + 97) + chr(int(random.uniform(0,25.99)) + 97) + chr(int(random.uniform(0,9.99)) + 48) + chr(int(random.uniform(0,9.99)) + 48) + chr(int(random.uniform(0,9.99)) + 48) + chr(int(random.uniform(0,25.99)) + 97)	



						






