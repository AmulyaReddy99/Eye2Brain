from django.db import models
from django import forms  

# Create your models here.
class InputClass(forms.Form):
	# brain = forms.ImageField(upload_to='images/')
	# captions = forms.ImageField(upload_to='images/')
	# voice = forms.CharField(label='voice', max_length=100)
	# banana = forms.ImageField(upload_to='images/')
	stock = forms.CharField(label='stock', max_length=100)
	sarcasm = forms.CharField(label='sarcasm', max_length=100)
	# leaf = forms.ImageField(upload_to='images/')


