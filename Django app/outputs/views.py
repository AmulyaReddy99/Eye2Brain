from django.shortcuts import render, render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,'pages/index.html')

def about(request):
	return render(request,'pages/speaker-details.html',{'n' : range(1,6)})