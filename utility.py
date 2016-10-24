import sqlite3 as sql
from os import listdir
from os.path import isfile, join


def crawled_docs() :
	connect = sql.connect('cntrl/test.db')
	cursor  = connect.cursor()

	cursor.execute('SELECT * from `pages` where `done` = 1')

	r = cursor.fetchone()

	s = set()

	while r is not None :
		s.add(r[1])
		r = cursor.fetchone()

	return s


def repoFilelist() :
	mypath = 'repo/'
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	
	onlyfiles = [f[0:-4] for f in onlyfiles ]

	s = set(onlyfiles)

	return s

def cleanedFilelist() :
	mypath = 'cleaned/'
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	
	onlyfiles = [f[0:-4] for f in onlyfiles ]

	s = set(onlyfiles)

	return s


def edges() :

	connect = sql.connect('cntrl/test_final.db')
	cursor = connect.cursor()

	cursor.execute('SELECT * from edges')

	r = cursor.fetchone()

	lst = []
	while r is not None :
		lst.append(r)
		r = cursor.fetchone()

	s = set(lst)

	return s


def recrawl() :

	fhandle = open('recrawl', 'r')
	dat = eval(fhandle.read())

	connect = sql.connect('cntrl/test_final.db')
	cursor = connect.cursor()

	for entry in dat :
		cursor.execute("UPDATE pages SET `done` = 3 WHERE `docid` = '" + entry + "'")
	
	connect.commit()





