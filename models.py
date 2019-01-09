#### Dependencies  ####
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

load_model_keypoints()

def prepare_image(img):
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

####  Age & Gender  ####
# @TODO get model route 
def load_model_agegender():
    global model
    global graph
    model = keras.models.load_model("./facialKeypoints/colabFiles/EPICProjectThree/tKeypointModel1227.h5")
    graph = K.get_session().graph