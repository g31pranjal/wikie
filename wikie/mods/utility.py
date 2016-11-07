import sqlite3 as sql
from os import listdir
from os.path import isfile, join


# return the set of docs that has been crawled from database
def crawled_docs() :
	connect = sql.connect('cntrl/production.db')
	cursor  = connect.cursor()

	cursor.execute('SELECT * from `pages` where `done` = 1')

	r = cursor.fetchone()

	s = set()

	while r is not None :
		s.add(r[1])
		r = cursor.fetchone()

	return s

# return the set of docs in the repo folder
def repoFilelist() :
	mypath = 'repo/'
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	
	onlyfiles = [f[0:-4] for f in onlyfiles ]

	s = set(onlyfiles)

	return s

# return the set of docs in the cleaned folder
def cleanedFilelist() :
	mypath = 'cleaned/'
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	
	onlyfiles = [f[0:-4] for f in onlyfiles ]

	s = set(onlyfiles)

	return s

# return the set of docs with 0 bytes in the cleaned folder
def nullFilelist() :
	mypath = 'null/'
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	
	onlyfiles = [f[0:-4] for f in onlyfiles ]

	s = set(onlyfiles)

	return s

# return all the edges
def edges() :

	connect = sql.connect('cntrl/production.db')
	cursor = connect.cursor()

	cursor.execute('SELECT * from edges')

	r = cursor.fetchone()

	lst = []
	while r is not None :
		lst.append(r)
		r = cursor.fetchone()

	s = set(lst)

	return s

# 
def failedScrapping() :
	connect = sql.connect('cntrl/production.db')
	cursor  = connect.cursor()

	cursor.execute('SELECT * from `pages` where `scrap_d` = 2')

	r = cursor.fetchone()

	s = set()

	while r is not None :
		s.add(r[1])
		r = cursor.fetchone()

	return s


def wP() :
	conn = sql.connect('cntrl/production.db')
	cursor = conn.cursor()

	cursor.execute('SELECT * from `pages` WHERE `done` = 1 AND `scrap_d` = 1')

	r = cursor.fetchone()

	lst = []

	while r is not None :
		lst.append(r)
		r = cursor.fetchone()

	connT = sql.connect('cntrl/worker.db')
	cursorT = connT.cursor()

	while len(lst) is not 0 :
		r = lst.pop()
		cursorT.execute("INSERT INTO `pages` values('"+ r[0] +"','"+ r[1] +"')")

	connT.commit()


# return the set of docs that has been crawled from database
def correctDocs() :
	connect = sql.connect('cntrl/worker.db')
	cursor  = connect.cursor()

	cursor.execute('SELECT * from `pages`')

	r = cursor.fetchone()

	s = set()

	while r is not None :
		s.add(r)
		r = cursor.fetchone()

	return s

# return the set of docs that has been crawled from database
def correctEdges() :
	connect = sql.connect('cntrl/worker.db')
	cursor  = connect.cursor()

	cursor.execute('SELECT * from `edges`')

	r = cursor.fetchone()

	s = set()

	while r is not None :
		s.add(r)
		r = cursor.fetchone()

	return s


def wE() :

	print "init.."

	edg = edges()
	print "edges loaded"
	docs = correctDocs()

	edg = [ x for x in edg if x[0] in docs and x[1] in docs ]

	print type(edg)
	
	print "num  : " + str(len(edg))

	connT = sql.connect('cntrl/worker.db')
	cursorT = connT.cursor()

	cnt = 0 

	while len(edg) is not 0 :
		r = lst.pop()
		cursorrsorT.execute("INSERT INTO `edges` values('"+ r[0] +"','"+ r[1] +"')")
		cnt += 1
		print cnt

	connT.commit()


def wO() :
	connect = sql.connect('cntrl/worker.db')
	cursor = connect.cursor()

	docs = correctDocs()
	edges = correctEdges()

	tally = 0
	cnt = 0


	for doc in docs :
		pass



	for doc in docs :
		num = cursor.fetchone()[0]
		tally += num


		cursor.execute("UPDATE `pages` SET `outlinks` = "+str(num)+" WHERE `docid` = '"+doc+"' ")

		connect.commit()
		cnt += 1
		print str(cnt) +" : " + str(tally)


def pagerank_init() :
	
	connect = sql.connect('cntrl/worker.db')
	cursor = connect.cursor()


	docs = correctDocs()

	init = 1./len(docs)

	sm = 0

	for doc in docs :
		cursor.execute("insert into `pagerank-score` (`docid`, `rank0`, `score`) values ( '" + doc[1] + "', "+str(init)+", 0.0 ) ")
		sm += init

	print sm

	connect.commit()



def elo_rating() :
	connect = sql.connect('cntrl/worker.db')
	cursor = connect.cursor()

	docs = correctDocs()


	for doc in docs :
		cursor.execute("insert into `elo-rating` (`docid`, `rating`, `count`) values ( '" + doc[1] + "', 7000.0, 0 ) ")

	connect.commit()

