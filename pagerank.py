import utility
import sqlite3 as sql
import time


connect = sql.connect('cntrl/worker.db')
cursor = connect.cursor()

# dictionary of outdegrees
t = utility.correctDocs()
t = list(t)

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

for i in range(0,6) :
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
			tmp1 = 0.85*tmp1
		
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




