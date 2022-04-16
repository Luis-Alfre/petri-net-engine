#model
# flask
from flask import Response, request
from flask_wtf import FlaskForm
from flask_restful import Resource
from api.app.petriNets.utils import construction
import json

class PetriNets(Resource):
    
    def post(self):
        body = request.get_json()
        newState=construction(body) 
        return {"New State":newState.tolist()}, 200


