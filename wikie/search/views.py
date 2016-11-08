from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse, JsonResponse
from search.models import *
import collections
import sqlite3 as sql
from mods import pagerank, elo, utility, indx
from scipy import stats
import math


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

	
	


	
	return render(request, "search/results.html")


def goto(request) :
	data = request.POST 

	# served = str(data[unicode('served')])
	clicked = str(data[unicode('clicked')])

	connect = sql.connect('cntrl/worker.db')
	cursor = connect.cursor()




