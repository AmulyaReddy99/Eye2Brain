# DNN

## Django - app
Our aim is to build a web interface for the models.

## Setup
- Clone this repo
- `cd DNN-master`
- Start jupyter noterbook to view the ipynb files
- To run the app goto `cd Django app`
- Run the app by `python3 manage.py runserver`

## Brain Tumor
- Download `vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5`
- Run `Tumor.ipynb`
- Model saved in `VGG16-transferlearning.model`

## Image Captions
- Data from `Kaggle Flikr image dataset`
- Pretrained model `vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5`
- Run `Image Captions.ipynb`

## Voice Recognition
- Data from `https://www.openslr.org/12`
- Run `Voice Recognition.ipynb`

## Banana
- No need for large dataset since transfer learning is used.
- Manually labeled data (255 images of green, ripe and overripe bananas) got from [here](github.com/giovannipcarvalho/banana-ripeness-classificationtree/master/data)
- Run `Banana.ipynb`

## Stocks
- Data is taken from Alphavantage, no need to download. Code has direct link to dataset
- `Stocks.ipynb`

## Sarcasm Detection
- Used tf-idf, LinearSVC, GaussianNB, LogisticRegression and RandomForest algorithms
- Run `Sarcasm Detection.ipynb`

## Leaf
- Leaf snap dataset
- Flavia dataset
- `Leaf.ipynb`

## Handwritten Text recognition
- iam handwriting dataset
- `Handwritten.ipynb`

## Traffic
- Requires Yolopretrained model
- Run `object_detection.py`

## Mnist 
- First program
