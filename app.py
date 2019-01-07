#######################################################
################  Flask Application  #################
##################  Dependencies  ###################
####################################################

# @TODO check dependencies
# import os

# import pandas as pd
# import numpy as np
# import json

from flask import Flask, render_template

app = Flask(__name__)



#######################################################
###################  App Routes  #####################
#####################################################

###  LANDING PAGE  ###
@app.route("/")
def index():
    print("Return the homepage")
    return render_template("index.html")

###  FACIAL KEYPOINT DETECTION  ###
@app.route("/keypoints/")
def tierone():
    print()
    return render_template("keypoints.html")

###  AGE & GENDER CLASSIFIER  ###
@app.route('/agegender/')
def tiertwo():
    print()
    return render_template("agegender.html")

###  FACE GENERATOR  ###
@app.route("/generator/")
def tierthree():
    print()
    return render_template("generator.html")

###  ABOUT THE TEAM  ###
@app.route("/aboutus/")
def about():
    print()
    return render_template("aboutus.html")


if __name__ == "__main__":
    app.run(debug=True)