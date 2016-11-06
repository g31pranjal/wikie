from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse, JsonResponse
from search.models import *


def index(request) :
	return render(request, "search/land.html")


def fetchResults(request) :
	return render(request, "search/results.html")

