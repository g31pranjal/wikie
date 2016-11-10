from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render, redirect
from django.template import Context
from django.http import HttpResponse, JsonResponse
from search.models import *
import collections
import sqlite3 as sql
from mods import pagerank, elo, utility, indx
from scipy import stats
import math
import random


def index(request) :
	return render(request, "search/land.html")


def fetchResults(request) :

	connect = sql.connect('cntrl/weights.db')
	cursor = connect.cursor()

	data = request.GET
	query = str(data[unicode('q')])

	qVector = indx.queryTokenVector(query)
	lst = indx.getRelevance(query, qVector)
	rel_D = {}

	for i in range(0, len(lst)) :
		rel_D[lst[i]] = i+1

	pagerank_scores = pagerank.get_pagerank(lst)
	pr_D = {}

	for i in range(0, len(pagerank_scores)) :
		pr_D[pagerank_scores[i]] = i+1

	elo_rating, count_lst = elo.get_elo(lst)
	elo_D = {}

	for i in range(0, len(elo_rating)) :
		elo_D[elo_rating[i]] = i+1

	Rrel, pr_contri, elo_contri = indx.calcWeightage(count_lst)

	fR = indx.rank_merge(rel_D, pr_D, elo_D, Rrel, pr_contri, elo_contri)

	connect = sql.connect('cntrl/worker.db')
	cursor = connect.cursor()

	#r9p = 0.8 + 0.2*random.random()
	#rat = float(r9p)/fR[0][1]

	ff = []
	st = ''

	for rec in fR :
		cursor.execute("SELECT `url`, `title` from `pages` where `docid` = '"+rec[0]+"'")
		r = cursor.fetchone()
		url = r[0]
		#score = "{0:.2f}".format(10*rat*rec[1])
		score = "{0:.2f}".format(10*rec[1])

		ff.append(( rec[0], url, score, r[1] ))
		st += '"'+rec[0]+'", '

	st = st[:-1]
	st = '[' + st + ']'

	
	return render(request, "search/results.html", { "lst" : ff , "query" : query, "string" : st} )


def goto(request) :
	data = request.GET 

	served = eval(data[unicode('served')])
	clicked = str(data[unicode('clicked')])
	url = unicode(data[unicode('url')])

	print type(served)
	print served

	elo.set_elo(served, clicked)

	return redirect(url)





