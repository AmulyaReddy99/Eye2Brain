from django.shortcuts import render, render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json
from bs4 import BeautifulSoup  
from outputs.models import InputClass

input_content = {
	'Brain Tumor':'''Please input mri scanned image
					<form action='/brain' method="post"><input type='file' name="brain" class="custom-file-input"><input type='submit' class="btn btn-submit"></form>''',
	
	'Image Captions':'''Please input an image
					<form action='/captions' method="post"><input type='file' name="captions" class="custom-file-input"><input type='submit' class="btn btn-submit"></form>''',
	
	'Voice Recognition':'''Input mp3 or wav file of Sharhukh/Amitab/Kajol and watch the classification
					<form action='/voice' method="post"><input type='file' name="voice" class="custom-file-input"><input type='submit' class="btn btn-submit"></form>''',
	
	'Banana Clasification':'''Please input an image of banana
							<form action='/banana' method="post"><input type='file' name="banana" class="custom-file-input"><input type='submit' class="btn btn-submit"></form>''',

	'Stocks price prediction':'''Enter the Security Id (Eg. MSFT)
							<input type='text' name="stock">''',
	
	'Sarcasm Detection':'''Enter a sentence in the input box below
						<form action='/sarcasm' method="post"><input type='text' name="sarcasm" class="form-control"><input type='submit' class="btn btn-submit"></form>''',
	
	'Leaf Identification':'''Please input an image of leaf
					<form action='/brain' method="post"><input type='file' name="leaf" class="custom-file-input"><input type='submit' class="btn btn-submit"></form>''',
	

}

output_content = {
	'Brain Tumor':''
}

def stocks(request):
	form = InputClass(request.POST)
	text = form['stock']

	soup = BeautifulSoup(str(text))
	value = soup.find('input').get('value')
	# brain_model.predict(image)
	return HttpResponse("Your response is "+value)

# Create your views here.
def index(request):
	return render(request,'pages/index.html',{'input_content':input_content})

def about(request):
	return render(request,'pages/speaker-details.html',{'n' : range(1,6)})