from django.urls import path

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('brain',views.index,name='brain'),
	path('about',views.about,name='about')
]