import sqlite3 as sql
import math





def get_elo(lst = [ "wru896w", "ecr403h", "zre991n", "emo769w", "hri743h", "edu280f", "ywr043h", "ajo035x", "hcm341s", "yng119x" ]) :

	connect = sql.connect('cntrl/worker.db')
	cursor = connect.cursor()

	# list of tuple to store rankings 
	rst = []

	for doc in lst :
		try :
			cursor.execute("SELECT * from `elo-rating` where `docid` = '"+str(doc)+"'")
			r = cursor.fetchone()

			tmp = (doc, r[1], r[2])
			rst.append(tmp)
		except Exception :
			pass


	cursor.execute("select `rating` from `elo-rating` order by `rating` DESC limit 1")
	tmp = cursor.fetchone()
	high = float(tmp[0])

	cursor.execute("select `rating` from `elo-rating` order by `rating` ASC limit 1")
	tmp = cursor.fetchone()
	low = float(tmp[0])

	diff = high - low 

	dct = []


	for entry in rst :
		if diff != 0 :
			dct.append(   (  entry[0] ,   "{0:.4f}".format(  ((entry[1] - low)/diff ) )    ,   entry[2] )  )
		else :
			dct.append( ( entry[0]  ,  0    ,   entry[2] ) )

	s = sorted(dct, key = lambda x : x[1], reverse = True)

	lst = [x[0] for x in s]
	cnt = [x[2] for x in s]

	return (lst, cnt)



# limit elo to 25
def set_elo(lst, selected = "rwb641g") :

	lst = ["fng105e", "qjv742d", "ymi617z", "rwb641g", "uck812y", "fcj482b", "jjh305d", "lih081o", "klq010c", "wnt749r", "elh075w", "ymb767w", "zoe107r", "dfg824i", "iwq376q", "yng119x" ,"hcm341s", "ajo035x", "ywr043h", "edu280f", "hri743h", "emo769w", "zre991n", "ecr403h", "wru896w"]

	connect = sql.connect('cntrl/worker.db')
	cursor = connect.cursor()

	# retrieve current ratings 
	rst = []
	for doc in lst :
		cursor.execute("SELECT * from `elo-rating` where `docid` = '"+str(doc)+"'")
		r = cursor.fetchone()
		tmp = (doc, r[1], float(r[1])/400, r[2])
		
		#print tmp

		rst.append(tmp)



	# calculate expected winning S^exp and damp it 
	fst = [] 
	dampF = 0.
	sm = 0
	for tup1 in rst :
		den = 0
		for tup2 in rst :
			if tup1[0] == tup2[0] :
				v = 1
			else :
				v = (2 ** -(tup1[2]-tup2[2]) )
			den += v

		#print den

		t = (1./den)*math.exp(-dampF)
		dampF += 0.05
		print(" : "+str(1./den) + " : "+ str(t))

		sm += t
		tmp = (tup1[0], tup1[1], t, tup1[3])
		fst.append(tmp)	

	# scale damped expected and calculate based on the selection
	val = sm
	gst = []
	for entry in fst :
		if entry[0] == selected :
			tmp = (entry[0], entry[1], entry[1] +  100*(1 - entry[2]/val)  , entry[3] + 1 )
		else :
			tmp = (entry[0], entry[1], entry[1] +  200*(0 - entry[2]/val)  , entry[3] + 1 )

		print tmp

		gst.append(tmp)


	for doc in gst : 
		cursor.execute("update `elo-rating` set `rating` = "+ str(int(doc[2])) +", `count` = "+str(doc[3])+" where `docid` = '" + doc[0] + "' ")

	connect.commit()


