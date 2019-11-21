from django.db import models
from django import forms  

# Create your models here.
class EditProfile(forms.ModelForm):
	def __init__(self, brain, *args, **kwargs):
		self.profile = profile
		super(EditProfile, self).__init__(*args, **kwargs)
		self.fields['name'] = forms.CharField(label='Name:', initial= profile.name,required=False)

class Meta:
	fields = ("name", "phoneNumber","streetAddress", "profilePic")