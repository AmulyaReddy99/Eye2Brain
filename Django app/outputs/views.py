from django.shortcuts import render, render
from django.http import HttpResponse
import json

input_content = {
	'Brain Tumor':'''Please input mri scanned image
					<form action='/brain'><input type='file'><input type='submit'></form>''',
	
	'Image Captions':'''Please input an image
					<form action='/captions'><input type='file'><input type='submit'></form>''',
	
	'Voice Recognition':'''Input mp3 or wav file of Sharhukh/Amitab/Kajol and watch the classification
					<form action='/captions'><input type='file'><input type='submit'></form>''',
	
	'Banana Clasification':'''Please input an image of banana
							<form action='/banana'><input type='file'><input type='submit'></form>''',

	'Stocks price prediction':'''Enter the Security Id (Eg. MSFT)
							<form action='/stock'><input type='text'><input type='submit'></form>''',
	
	'Sarcasm Detection':'''Enter a sentence in the input box below
						<form action='/sarcasm'><input type='text'><input type='submit'></form>''',
	
	'Leaf Identification':'''Please input an image of leaf
					<form action='/brain'><input type='file'><input type='submit'></form>''',
	

}

output_content = {
	'Brain Tumor':''
}

def brain(request):
	print("-------> brain")
	image = request.files['image']
	# brain_model.predict(image)
	return render(request,'pages/index.html',{'image':image})

# Create your views here.
def index(request):
	return render(request,'pages/index.html',{'input_content':input_content})

def about(request):
	return render(request,'pages/speaker-details.html',{'n' : range(1,6)})