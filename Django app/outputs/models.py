from django.db import models
from django import forms  
# from django.core.files.uploadedfile import SimpleUploadedFile
# from PIL import Image

# Create your models here.

class ImagesModel(models.Model):
    image = models.FileField(upload_to='images/')

class ImagesForm(forms.ModelForm):
    class Meta:
        model = ImagesModel
        fields = ('image', )


class InputClass(forms.Form):
	Brain_Tumor = forms.CharField(label='Brain_Tumor', max_length=100)
	# Image_Captions = forms.FileField(upload_to='images/')
	# Voice_Recognition = forms.FileField(upload_to='images/')
	# Banana_Clasification = forms.FileField(upload_to='images/')
	Stocks_price_prediction = forms.CharField(label='stock', max_length=100)
	Sarcasm_Detection = forms.CharField(label='sarcasm', max_length=100)
	# Leaf_Identification = forms.FileField(upload_to='images/')
	# captions = forms.ImageField(upload_to='images/')
	# voice = forms.CharField(label='voice', max_length=100)
	# banana = forms.ImageField(upload_to='images/')
	name = forms.CharField(label='name', max_length=100)
	# stock = forms.CharField(label='stock', max_length=100)
	# sarcasm = forms.CharField(label='sarcasm', max_length=100)
	# leaf = forms.ImageField(upload_to='images/')


