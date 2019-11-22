from django.urls import path

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('stocks',views.stocks,name='stocks'),
	path('about',views.about,name='about')
]