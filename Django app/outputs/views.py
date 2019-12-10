from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json, cv2, os
import numpy as np
from bs4 import BeautifulSoup  
from outputs.models import InputClass, ImagesForm


input_content = {
	'Brain Tumor':'''Please input mri scanned image
					<input type='file' id="Brain Tumor" name="Brain_Tumor">''',
	
	'Image Captions':'''Please input an image
					<input type='file' id="Image Captions" name="Image_Captions">''',
	
	'Voice Recognition':'''Input flac or mp3 or wav file of Sharhukh/Amitab/Kajol and watch the classification
					<input type='file' id="Voice Recognition" name="Voice_Recognition">''',
	
	'Banana Clasification':'''Please input an image of banana
					<input type='file' id="Banana Clasification" name="Banana_Clasification">''',

	'Stocks price prediction':'''Enter the Security Id (Eg. MSFT)
					<input type='text' id="Stocks price prediction" name="Stocks_price_prediction">''',
	
	'Sarcasm Detection':'''Enter a sentence in the input box below
					<input type='text' id="Sarcasm Detection" name="Sarcasm_Detection">''',
	
	'Leaf Identification':'''Please input an image of leaf
					<input type='file' id="Leaf Identification" name="Leaf_Identification">''',
}

import outputs.load_saved_model as m

# @Todo
test_input = '' #@Todo: Change this variable to np.array which stores input data like image, text, numericals etc which is passed to respective functions.


def simple_upload(request,myfile):
    global test_input
    if request.method == 'POST' and request.FILES[myfile]:
        myfile = request.FILES[myfile]
        # @Todo:
        """Assign file data to test_input. """
        fs = FileSystemStorage()
        extention = myfile.name.split('.')[-1]
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        test_input = uploaded_file_url
        print("Done uploading.....")



def models(request):
	global test_input
	form = InputClass(request.POST)
	text = form['name']
	soup = BeautifulSoup(str(text))
	value = soup.find('input').get('value')
	temp = value.replace(' ','_')
	output_content = dict()
	try:
		if request.method == 'POST' and request.FILES[temp]:
			image_form = ImagesForm(request.POST, request.FILES)
			simple_upload(request,temp)
			test_input = test_input[1:]
			output_content = {
				'Brain Tumor': m.brain(test_input),
				'Image Captions': m.captions(test_input),
				'Voice Recognition': m.voice(test_input),
				'Banana Clasification': m.banana(test_input),
				'Stocks price prediction': m.stock(test_input),
				'Sarcasm Detection': m.sarcasm(test_input),
				'Leaf Identification': m.leaf(test_input)
			}
	except Exception as e:
		print("-------> ", e)

	test_input = str(test_input)
	print("+++++++++",test_input)
	test_output = output_content[value]

	# @Todo: Change this to redirect to same page without reloading.
	print('-----------------------------')
	return HttpResponse('<h2>Input</h2><img width="193" height="130" src='+test_input+'/><hr><h2>Output</h2>'+str(test_output))
	# return JsonResponse({"img":'<h2>Input</h2><img src='+test_input+'/>',"output":'<hr><h2>Output</h2>'+test_output})

# Create your views here.
def index(request):
	return render(request,'pages/index.html',{'input_content':input_content})

def about(request):
	return render(request,'pages/speaker-details.html',{'n' : range(1,6)})

