import os
from flask import Flask, request, redirect, url_for, jsonify, make_response
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import json
import sys
import imageservice
from imageservice import myImage

UPLOAD_FOLDER = os.path.abspath("images")
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

cors = CORS(app, resources={r"/*": {"origins": "*"}})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        imageservice.imagelink = file.filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',filename=filename))
    # Import the model script
    import model
    # Process the detection
    preprocessed_image = model.prepare_image(imageservice.myImage())
    predictions = model.mobile.predict(preprocessed_image)
    # Store the results
    results = model.imagenet_utils.decode_predictions(predictions)
    # Create an object for each result
    first_result = [x[0] for x in results]
    second_result = [x[1] for x in results]
    third_result = [x[2] for x in results]
    fourth_result = [x[3] for x in results]
    fifth_result = [x[4] for x in results]
    analysis_res = {
        "first_prob" : {str(first_result[0][1]) : str(int(first_result[0][2] * 100))+'%'},
        "second_prob" : {str(second_result[0][1]) : str(int(second_result[0][2] * 100))+'%'},
        "third_prob" : {str(third_result[0][1]) : str(int(third_result[0][2] * 100))+'%'},
        "fourth_prob" : {str(fourth_result[0][1]) : str(int(fourth_result[0][2] * 100))+'%'},
        "fifth_prob" : {str(fifth_result[0][1]) : str(int(fifth_result[0][2] * 100))+'%'}
    }
    # Send results to client
    os.remove(os.path.abspath("images")+'/'+imageservice.myImage())
    return json.dumps(analysis_res)

if __name__ == '__main__':
    app.run()
