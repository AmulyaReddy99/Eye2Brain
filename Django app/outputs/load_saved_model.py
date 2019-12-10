import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2,os

from imageai.Detection import VideoObjectDetection

# @Todo
''' Remove unnecessary imports'''
import glob, os, re, random, csv
from keras.applications import VGG16
from keras.applications.vgg16 import VGG16, preprocess_input
from keras import models
from keras.models import Sequential, Model 
from keras.layers import Dense, LSTM, Dropout, Conv2D, Flatten, AveragePooling2D, MaxPooling2D, Lambda
from keras.optimizers import Adam, RMSprop

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.utils import np_utils, to_categorical

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix

from keras.models import load_model
# heroku run bash -a eye2brain 
# import soundfile as sf # flac file 

def stock(test):
	model = load_model('outputs/saved_models/stocks.h5')
	# @ Todo
	"""Input: array of list of 60 decimal numbers as shown below. Tpycally everything is in np.array form. Check this once."""
	test = np.array([[[0.05474711],[0.05526832],[0.05245382],[0.04859692],[0.04703332],[0.04734604],[0.04515699],[0.04296794],[0.0433849 ],[0.04290539],[0.04067464],[0.03869407],[0.03942376],[0.03243964],[0.02910395],[0.02910395],[0.02378768],[0.02503857],[0.02243256],[0.02222408],[0.02159863],[0.02180711],[0.02326648],[0.0181587 ],[0.01742901],[0.01940958],[0.0197223 ],[0.01555268],[0.01742901],[0.01763749],[0.01930534],[0.02034566],[0.0192011 ],[0.02316224],[0.02649794],[0.03014635],[0.03223116],[0.02910395],[0.02681066],[0.02660218],[0.0269149 ],[0.02597673],[0.02785306],[0.03108452],[0.03389901],[0.03410749],[0.03671351],[0.03702623],[0.03858983],[0.03879832],[0.03963224],[0.03963224],[0.04150857],[0.04296794],[0.04422091],[0.04578243],[0.04755452],[0.04536547],[0.04421882],[0.04161281]]])
	return model.predict(test)

def brain(test):
	model = load_model('outputs/saved_models/tumour.h5')
	test = np.array([cv2.resize(cv2.imread(test),(100,100))])
	return model.predict(test)


def banana(test):
	model = load_model('outputs/saved_models/banana.h5')
	# testimage = 'outputs/images/banana.jpeg'
	img = cv2.resize(cv2.imread(test), (100, 100))
	img = np.array([cv2.cvtColor(img, cv2.COLOR_BGR2RGB)])
	return np.array(model.predict(img))

def captions(test):
	# @Todo
	"""Comment this return statement below once done with below task mentioned."""
	return "----------> CAPTIONS"
	# @Todo
	"""Please go to respective .ipynb in main project folder (cd ../..) after downloading the dataset.
	Run the model and save it using model.save('Django app/outputs/saved_models/filename.h5').
	Input parameter: Image. Tpycally everything is in np.array form. Check this once."""
	model = load_model('outputs/saved_models/captions.h5')
	modelvgg.compile(loss='categorical_crossentropy', optimizer='adam')
	return model.predict(test)

def voice(test):
	return "----------> CAPTIONS" #@Todo: comment this
	# @Todo
	"""Please go to respective .ipynb in main project folder (cd ../..) after downloading the dataset.
	Run the model and save it using model.save('Django app/outputs/saved_models/filename.h5').
	Input parameter: flac file"""
	model = load_model('outputs/saved_models/voice.h5')
	model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
	return model.predict(test)


# not yet done
def sarcasm(test):
	return "----------> SARCASM" #@Todo: comment this
	# @Todo
	""" save model. Input: Text. Check if test is received properly."""
	model = load_model('outputs/saved_models/sarcasm.h5')
	return model.predict(test)

def leaf(test):
	return "----------> LEAF" #@Todo: comment this
	# @Todo
	""" save model. check input is image"""
	model = load_model('outputs/saved_models/leaf.h5')
	model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
	return model.predict(test)

def handwritten(test):
	return "----------> HANDWRITTEN" #@Todo: comment this
	# @Todo
	""" save model. check input is image"""
	model = load_model('outputs/saved_models/handwritten.h5')
	model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
	return model.predict(test)

