from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^results$', views.fetchResults, name='fetchResults'),
	url(r'^goto/$', views.goto, name='goto'),

]
