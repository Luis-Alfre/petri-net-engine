from lib2to3.pgen2 import token
from flask import Flask, jsonify, render_template, request, url_for
from flask_restful import Api
from flask_cors import CORS
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
import json

from api import include_urls
from api.app.petriNets.utils import Analytics

app = Flask(__name__)


api = Api(app)
include_urls(api)


@app.route('/', methods=["GET", "POST"]) 
def home():
    return render_template('index.html')




@app.route('/petry', methods=["POST"]) 
def process():
    places = ','+str(request.form.get("places"))+','
    tokens = ','+str(request.form.get("tokens"))+','
    transitions = ','+ str(request.form.get("transitions"))+','
    input =  ','+str(request.form.get("input"))+','
    output =  ','+str(request.form.get("output"))+','
    shooting =  ','+str(request.form.get("shooting"))+','
    print("##############3333333")
    Analytics(places,tokens,transitions,input,output,shooting)
    return render_template('result.html')



Bootstrap(app)

if __name__ == '__main__':
    app.run(debug=True)