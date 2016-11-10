import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
import collections
import sqlite3 as sql
import math
from scipy import stats


def getTokens(sentence) :
	stop = set(stopwords.words('english'))
	tokens =  [i for i in sentence.lower().split() if i not in stop]

	stemmer = PorterStemmer()

	tokens = [str(stemmer.stem(token)) for token in tokens]

	return tokens


def queryTokenVector(sentence) :

	tokens = getTokens(sentence)

	connect = sql.connect('cntrl/weights.db')
	cursor = connect.cursor()
	
	a =  dict(collections.Counter(tokens))

	norm = 0.

	for key, value in a.iteritems() :
		tmp =  key[0].upper()
		cursor.execute("SELECT `idf` from `idf_"+tmp+"` WHERE `name` = '"+key+"'")
		r = cursor.fetchone()

		if r is None :
			a[key] = -1
		else :
			a[key] = r[0]*(1 + (math.log10(value)))
			norm += a[key] ** 2

	norm = math.sqrt(norm)

	for key, value in a.iteritems() :
		a[key] = a[key]/norm

	return a


def getRelevance(query, qVector) :

	connect = sql.connect('cntrl/weights.db')
	cursor = connect.cursor()

	tokens = getTokens(query)

	# list of all docids which have atleast 1 occurence of word
	lst = []
	for token in tokens :
		tmp = posting(token)
		lst += tmp

	# combine multiple entries and convert to dictionary 
	c = dict(collections.Counter(lst))

	lst = None 
	dc = {}
	for key in c.keys() :
		dc[key] = 0.

	c = None
	cnt = 0
	ind = {}

	# find norm 
	norm = {}
	cursor.execute("select * from `wts`");
	r = cursor.fetchone()

	while r is not None :
		norm[r[0]] = r[1]
		r = cursor.fetchone()

	# index in memory	
	for token in qVector.keys() :
		ind = {}
		print "flushed index"
		alpha = token[0].upper()
		cursor.execute("SELECT * from `tf-idf_"+alpha+"`")
		r = cursor.fetchone()
		while r is not None :
			tmp = (r[0], r[1])
			ind[tmp] = r[2]
			r = cursor.fetchone()

		print "indexed" + alpha

		for doc in dc.keys() :

			try :
				dc[doc] += (ind[(token, int(doc))] * qVector[token])  
				# print( str( norm[int(doc)]) +" : "+ str(ind[(token, int(doc))]) +" : "+ str(qVector[token])+" : "+str(ind[(token, int(doc))]*qVector[token]))
			except Exception :
				dc[doc] += 0.

	ind = None

	# convert to list of tuples 
	ftup = []

	for key, value in dc.iteritems() :
		tmp = (key, value)
		ftup.append(tmp)

	ftup = sorted(ftup, key = lambda x : x[1], reverse = True)
	
	mp = {}

	connect = sql.connect('cntrl/map.db')
	cursor = connect.execute("SELECT * from `map`")

	r = cursor.fetchone()

	while r is not None :
		mp[r[0]] = r[1]
		r = cursor.fetchone()

	tps = []

	for i in range(0,min(80, len(ftup))) :
		t1 = int(ftup[i][0])
		t2 = str(mp[t1])
		tps.append(t2)
	
	return tps


def posting(word):

	a = word[0]
	a = a.upper()
	st = "final_stuff/posting/posting/TFmts"+a+".txt"
	f = open(st,'r')

	post = []
	post = f.readlines()	
	i=0
	j=0
	list = []
	while i <len(post):
		temp = post[i].split()
		if temp[0] == word:
			temp1 = temp[1].split(",")
			while j<len(temp1)-1:
				list.append(temp1[j])
				j+=1

		i+=1

	return list


def calcWeightage(Elo_count) :
	Rrel = 0.4
	Rran = 1. - Rrel

	hm = stats.hmean(Elo_count) - 10

	elo_confidence = 0.4 * (1 - math.exp(-hm / 2) )

	elo_contri = Rran * (elo_confidence)
	pr_contri  = Rran - elo_contri

	return (Rrel, pr_contri, elo_contri) 



def rank_merge(lst_D, pr_D, elo_D, wl, wp, we) :

	dct = []

	for key, value in pr_D.iteritems() :
		try :
			dct.append( (  key ,  (wl / (1 + lst_D[key])) + (wp / (1 + value)) + (we / (1 + elo_D[key])) ) )  
		except Exception :
			pass

	s = sorted( dct , key = lambda x : x[1], reverse = True)

	return s
