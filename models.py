#### Dependencies  ####
import pandas as pd
import numpy as np

# From Troy's notebook
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import BatchNormalization, Conv2D, Activation, MaxPooling2D, Dense, GlobalAveragePooling2D
from keras import optimizers
from keras.layers import Dropout, Flatten
from keras.models import load_model
from PIL import Image
import cv2

# From Class Activity
import keras
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from keras.applications.xception import (
    Xception, preprocess_input, decode_predictions)
from keras import backend as K

####  Facial Keypoints Model  ####
def load_model_keypoints():
    global model
    global graph
    model = keras.models.load_model("./facialKeypoints/colabFiles/EPICProjectThree/tKeypointModel1227.h5")
    graph = K.get_session().graph

def prep_img_keypoints(img):
    # Class Activity img processing code
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    
    # Troy's img processing code
    img = cv2.imread(img)
    originalDimX=img.shape[0]
    originalDimY=img.shape[1]
    face_cascade = cv2.CascadeClassifier('./facialKeypoints/colabFiles/EPICProjectThree/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    imgCropped = gray[y:y+h, x:x+w]
    croppedDimX=imgCropped.shape[0]
    croppedDimY=imgCropped.shape[1]
    # Check math on all the following - may need adjusting to accurately scale up
    cropOffsetX = (originalDimX - croppedDimX)/2
    cropOffsetY = (originalDimY - croppedDimY)/2
    imgCropped96 = cv2.resize(imgCropped, (96, 96))
    ratioTo96x = 96/croppedDimX
    ratioTo96y = 96/croppedDimY
    imgCropped96 = imgCropped96 / 255
    df = pd.read_csv('./facialKeypoints/data/training.csv')
    twoKGoodFaces = df.dropna()
    y = np.vstack(twoKGoodFaces[twoKGoodFaces.columns[:-1]].values)

    return img, imgCropped96

def predict_keypoints(imgCropped96):
    # Import dataset
    df = pd.read_csv('./facialKeypoints/data/training.csv')
    twoKGoodFaces = df.dropna()
    y = np.vstack(twoKGoodFaces[twoKGoodFaces.columns[:-1]].values)
    y.shape, y.dtype

    load_model_keypoints()

    # Creating pipeline
    output_pipe = make_pipeline(
        MinMaxScaler(feature_range=(-1, 1))
    )
    y_train = output_pipe.fit_transform(y)

    predictions = model.predict(imgCropped96[np.newaxis, :, :, np.newaxis])

    xy_predictions = output_pipe.inverse_transform(predictions).reshape(15, 2)




####  Age & Gender  ####
# @TODO get model route 
def load_model_agegender():
    global model
    global graph
    model = keras.models.load_model("./facialKeypoints/colabFiles/EPICProjectThree/tKeypointModel1227.h5")
    graph = K.get_session().graph