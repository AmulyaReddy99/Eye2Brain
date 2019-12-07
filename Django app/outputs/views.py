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
					<input type='file' id="id" name="Brain_Tumor">''',
	
	'Image Captions':'''Please input an image
					<input type='file' id="id" name="Image_Captions">''',
	
	'Voice Recognition':'''Input flac or mp3 or wav file of Sharhukh/Amitab/Kajol and watch the classification
					<input type='file' id="id" name="Voice_Recognition">''',
	
	'Banana Clasification':'''Please input an image of banana
					<input type='file' id="id" name="Banana_Clasification">''',

	'Stocks price prediction':'''Enter the Security Id (Eg. MSFT)
					<input type='text' id="id" name="Stocks_price_prediction">''',
	
	'Sarcasm Detection':'''Enter a sentence in the input box below
					<input type='text' id="id" name="Sarcasm_Detection">''',
	
	'Leaf Identification':'''Please input an image of leaf
					<input type='file' id="id" name="Leaf_Identification">''',
	

}

import outputs.load_saved_model as m

# @Todo
test_input = 1 #@Todo: Change this variable to np.array which stores input data like image, text, numericals etc which is passed to respective functions.

output_content = {
	'Brain Tumor': m.brain(test_input),
	'Image Captions': m.captions(test_input),
	'Voice Recognition': m.voice(test_input),
	'Banana Clasification': m.banana(test_input),
	'Stocks price prediction': m.stock(test_input),
	'Sarcasm Detection': m.sarcasm(test_input),
	'Leaf Identification': m.leaf(test_input)
}

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
	try:
		if request.method == 'POST' and request.FILES[temp]:
			image_form = ImagesForm(request.POST, request.FILES)
			simple_upload(request,temp)
	except Exception as e:
		print("-------> ", e)

	test_output = output_content[value]

	# @Todo: Change this to redirect to same page without reloading.
	print(str(test_input))
	print('-----------------------------')
	return HttpResponse('<h2>Input</h2><img width="193" height="130" src='+test_input+'/><hr><h2>Output</h2>'+test_output)
	# return JsonResponse({"img":'<h2>Input</h2><img src='+test_input+'/>',"output":'<hr><h2>Output</h2>'+test_output})

	"""Donot uncomment the below"""
	# return redirect('index')
	# import outputs.load_saved_models as m
	# form = InputClass(request.POST)
	# text = form['stock']

	# soup = BeautifulSoup(str(text))
	# value = soup.find('input').get('value')
	
	# # this is only for stocks.. Generalize this to others as well
	# test = np.array([[[0.05474711],[0.05526832],[0.05245382],[0.04859692],[0.04703332],[0.04734604],[0.04515699],[0.04296794],[0.0433849 ],[0.04290539],[0.04067464],[0.03869407],[0.03942376],[0.03243964],[0.02910395],[0.02910395],[0.02378768],[0.02503857],[0.02243256],[0.02222408],[0.02159863],[0.02180711],[0.02326648],[0.0181587 ],[0.01742901],[0.01940958],[0.0197223 ],[0.01555268],[0.01742901],[0.01763749],[0.01930534],[0.02034566],[0.0192011 ],[0.02316224],[0.02649794],[0.03014635],[0.03223116],[0.02910395],[0.02681066],[0.02660218],[0.0269149 ],[0.02597673],[0.02785306],[0.03108452],[0.03389901],[0.03410749],[0.03671351],[0.03702623],[0.03858983],[0.03879832],[0.03963224],[0.03963224],[0.04150857],[0.04296794],[0.04422091],[0.04578243],[0.04755452],[0.04536547],[0.04421882],[0.04161281]]])
	# result = m.stock(test)
	# print("++++++++>",result)
	
	# return HttpResponse("Prediction is "+str(result[0][0]))


# Create your views here.
def index(request):
	return render(request,'pages/index.html',{'input_content':input_content})

def about(request):
	return render(request,'pages/speaker-details.html',{'n' : range(1,6)})

