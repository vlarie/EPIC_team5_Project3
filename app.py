#######################################################
################  Flask Application  #################
##################  Dependencies  ###################
####################################################

# @TODO check dependencies
import os
import io
import models

from flask import Flask, request, redirect, url_for, jsonify, render_template

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'Uploads'


#######################################################
###################  App Routes  #####################
#####################################################

###  LANDING PAGE  ###
@app.route("/")
def index():
    print("Return the homepage")
    return render_template("index.html")


###  FACIAL KEYPOINT DETECTION  ###
@app.route("/keypoints/", methods=["GET", "POST"])
def tierone():
    print()
    models.load_model_keypoints
    # if request.method == "POST":
    #     print(request)
    #     if request.files.get("file"):
    #         file = request.files["file"]
    #         filename = file.filename
    #         filepath = os.path.join(app.config["UPLOAD_Folder"], filename)
    #         file.save(filepath)
    #         image_size = (96, 96)
    #         im = image.load_img(filepath, target_size=image_size, grayscale=True)
    #         image_array = prepare_image(im)
    #         print(image_array)
    #         global graph
    #         with graph.as_default():
    #             predicted_keypoints = model.predict_classes(image_array)[0]
    #             data["prediction"] = str(predicted_keypoints)
    #             data["success"] = True
    #         return jasonify(data)
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