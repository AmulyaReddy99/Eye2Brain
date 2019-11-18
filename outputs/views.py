from django.shortcuts import render, render
from django.http import HttpResponse

# Create your views here.
def index(request):
	l = ['Brain Tumor','Image Captions','Voice Recognition','Banana Clasification','Stocks price prediction','Sarcasm Detection','Leaf Identification', 'Handwritten Text recognition','Traffic detection']
	return render(request,'pages/index.html',{'n2': l})

def about(request):
	return render(request,'pages/speaker-details.html',{'n' : range(1,6)})