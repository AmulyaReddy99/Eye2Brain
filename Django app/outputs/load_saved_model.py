import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

from keras.models import Sequential  
from keras.layers import Dense, LSTM, Dropout 

from keras.models import load_model

def brain(test):
	return "---------> BRAIN"
	model = load_model('outputs/saved_models/brain.h5')
	model.compile(loss='binary_crossentropy',optimizer=RMSprop(lr=1e-4),metrics=['accuracy'])
	return model.predict(test)

def captions(test):
	return "----------> CAPTIONS"
	model = load_model('outputs/saved_models/captions.h5')
	modelvgg.compile(loss='categorical_crossentropy', optimizer='adam')
	return model.predict(test)

def voice(test):
	return "----------> CAPTIONS"
	model = load_model('outputs/saved_models/voice.h5')
	model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
	return model.predict(test)

def banana(test):
	return "----------> BANANA"
	model = load_model('outputs/saved_models/banana.h5')
	model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
	return model.predict(test)

def stock(test):
	return "----------> STOCK"
	model = load_model('outputs/saved_models/stocks.h5')
	model.compile(optimizer = 'adam', loss = 'mean_squared_error')
	# test = np.array([[[0.05474711],[0.05526832],[0.05245382],[0.04859692],[0.04703332],[0.04734604],[0.04515699],[0.04296794],[0.0433849 ],[0.04290539],[0.04067464],[0.03869407],[0.03942376],[0.03243964],[0.02910395],[0.02910395],[0.02378768],[0.02503857],[0.02243256],[0.02222408],[0.02159863],[0.02180711],[0.02326648],[0.0181587 ],[0.01742901],[0.01940958],[0.0197223 ],[0.01555268],[0.01742901],[0.01763749],[0.01930534],[0.02034566],[0.0192011 ],[0.02316224],[0.02649794],[0.03014635],[0.03223116],[0.02910395],[0.02681066],[0.02660218],[0.0269149 ],[0.02597673],[0.02785306],[0.03108452],[0.03389901],[0.03410749],[0.03671351],[0.03702623],[0.03858983],[0.03879832],[0.03963224],[0.03963224],[0.04150857],[0.04296794],[0.04422091],[0.04578243],[0.04755452],[0.04536547],[0.04421882],[0.04161281]]])
	predict_ = model.predict(test)
	print("============>",predict_)
	return predict_

# not yet done
def sarcasm(test):
	return "----------> SARCASM"
	model = load_model('outputs/saved_models/sarcasm.h5')
	return model.predict(test)

def leaf(test):
	return "----------> LEAF"
	model = load_model('outputs/saved_models/leaf.h5')
	model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
	return model.predict(test)

def handwritten(test):
	return "----------> HANDWRITTEN"
	model = load_model('outputs/saved_models/handwritten.h5')
	model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
	return model.predict(test)

