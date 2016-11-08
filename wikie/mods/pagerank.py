import utility
import sqlite3 as sql
import time
import math



def pagerank_rec() :


	connect = sql.connect('cntrl/worker.db')
	cursor = connect.cursor()

	# dictionary of outdegrees
	t = utility.correctDocs()
	t = list(t)

	N = 1./len(t)

	dct = {}
	for entry in t :
		dct[str(entry[1])] = entry[2]

	print "outlink dictionary created. dct"

	# old pagerank and a column for new
	cursor.execute('select * from `pagerank-score`')
	r= cursor.fetchone()
	lst = {}
	while r is not None :
		lst[str(r[0])] = (r[1], 0.0)
		r = cursor.fetchone()

	print "old and new pagerank tuple created. lst"


	# list of edge tuples
	edg = utility.correctEdges()

	print "edges fetched..."

	util = {}
	for doc in t :
		util[str(doc[1])] = []

	print "blank util created..."

	cnt = 0

	for edge in edg :
		util[str(edge[1])].append(str(edge[0]))
		cnt += 1
		print cnt

	print "data structures created"

	s = 0
	error = 0

	for i in range(0,50) :
		s = 0

		print "iteration :: " + str(i) + ". Resuming in 5(secs)"
		time.sleep(5)


		for key, value in lst.iteritems() :
			
			tmp = util[str(key)]
			tmp1 = 0.

			print "ins completed"

			if len(tmp) != 0 :
				for x in tmp :
					tmp1 += lst[x][0]/dct[x]
				tmp1 = 0.85*tmp1 + 0.15*N
			
			s += tmp1
			tp = (lst[key][0], tmp1)
			lst[key] = tp

			print str(key) +" : "+str(tmp1)	

		val = (1-s)/len(t)

		s = 0
		error = 0

		for key in lst.keys() :
			s += (lst[key][1] + val)
			error += abs(lst[key][1] + val - lst[key][0])

			tp = (lst[key][1] + val, 0.0)
			lst[key] = tp

			print " : " + str(s)

		print error

	cnt = 0

	for key in lst.keys() :
		cursor.execute("update `pagerank-score` set `rank0` = " +str(lst[key][0] + val)+ " where `docid` = '"+str(key)+"' ")
		cnt += 1
		print cnt


	connect.commit()




def pagerank_scale() :


	connect = sql.connect('cntrl/worker.db')
	cursor = connect.cursor()

	cursor.execute('select * from `pagerank-score`')
	r= cursor.fetchone()
	lst = {}
	while r is not None :
		lst[str(r[0])] = (r[1], ( (( r[1] - 1.e-9)/(5e-3 - 1.e-9)) ** (1./3)  )  )
		print(lst[str(r[0])][1])
		r = cursor.fetchone()


	print "done"

	cnt = 0
	for key in lst.keys() :
		cursor.execute("update `pagerank-score` set `score` = " +str(lst[key][1])+ " where `docid` = '"+str(key)+"' ")
		cnt += 1

		print cnt


	connect.commit()


def get_pagerank(lst = [ "wru896w", "ecr403h", "zre991n", "emo769w", "hri743h", "edu280f", "ywr043h", "ajo035x", "hcm341s", "yng119x" ]) :


	connect = sql.connect('cntrl/worker.db')
	cursor = connect.cursor()

	rst = []

	for doc in lst :
		cursor.execute("SELECT * from `pagerank-score` where `docid` = '"+str(doc)+"'")
		r = cursor.fetchone()
		try :
			rst.append(  (str(doc), r[2]) )
		except Exception :
			pass

	s = sorted(rst, key = lambda x : x[1], reverse = True)
	s = [x[0] for x in s ]

	return s


#pagerank_scale()