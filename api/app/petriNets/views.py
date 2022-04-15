#model
# flask
from flask import Response, request
from flask_restful import Resource
from api.app.petriNets.utils import construction

class PetriNets(Resource):
    
    def post(self):
        body = request.get_json()
        construction(body) 
        

        return {"message": "El usuario no tiene permisos para realizar esta operación.",
                    "status": 403}, 403