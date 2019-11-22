from django.shortcuts import render, render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json
import numpy as np
from bs4 import BeautifulSoup  
from outputs.models import InputClass

input_content = {
	'Brain Tumor':'''Please input mri scanned image
					<form action='/brain' method="post"><input type='file' name="brain">''',
	
	'Image Captions':'''Please input an image
					<form action='/captions' method="post"><input type='file' name="captions">''',
	
	'Voice Recognition':'''Input mp3 or wav file of Sharhukh/Amitab/Kajol and watch the classification
					<form action='/voice' method="post"><input type='file' name="voice">''',
	
	'Banana Clasification':'''Please input an image of banana
							<form action='/banana' method="post"><input type='file' name="banana">''',

	'Stocks price prediction':'''Enter the Security Id (Eg. MSFT)
							<form action='/models' method="post"><input type='text' name="stock">''',
	
	'Sarcasm Detection':'''Enter a sentence in the input box below
						<form action='/sarcasm' method="post"><input type='text' name="sarcasm">''',
	
	'Leaf Identification':'''Please input an image of leaf
					<form action='/brain' method="post"><input type='file' name="leaf">''',
	

}

output_content = {
	'Brain Tumor':''
}

def models(request):
	import outputs.load_saved_models as m
	form = InputClass(request.POST)
	text = form['stock']

	soup = BeautifulSoup(str(text))
	value = soup.find('input').get('value')
	
	# this is only for stocks.. Generalize this to others as well
	test = np.array([[[0.05474711],[0.05526832],[0.05245382],[0.04859692],[0.04703332],[0.04734604],[0.04515699],[0.04296794],[0.0433849 ],[0.04290539],[0.04067464],[0.03869407],[0.03942376],[0.03243964],[0.02910395],[0.02910395],[0.02378768],[0.02503857],[0.02243256],[0.02222408],[0.02159863],[0.02180711],[0.02326648],[0.0181587 ],[0.01742901],[0.01940958],[0.0197223 ],[0.01555268],[0.01742901],[0.01763749],[0.01930534],[0.02034566],[0.0192011 ],[0.02316224],[0.02649794],[0.03014635],[0.03223116],[0.02910395],[0.02681066],[0.02660218],[0.0269149 ],[0.02597673],[0.02785306],[0.03108452],[0.03389901],[0.03410749],[0.03671351],[0.03702623],[0.03858983],[0.03879832],[0.03963224],[0.03963224],[0.04150857],[0.04296794],[0.04422091],[0.04578243],[0.04755452],[0.04536547],[0.04421882],[0.04161281]]])
	result = m.stock(test)
	print("++++++++>",result)
	
	return HttpResponse("Prediction is "+str(result[0][0]))

# Create your views here.
def index(request):
	return render(request,'pages/index.html',{'input_content':input_content})

def about(request):
	return render(request,'pages/speaker-details.html',{'n' : range(1,6)})