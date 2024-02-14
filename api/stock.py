from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random
import http.client

from model.stocks import *

stock_api = Blueprint('stock_api', __name__,
                   url_prefix='/api/stock')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(stock_api)

class StockAPI:
    # not implemented
    
    # getWeather()
    class _Read(Resource):
        def get(self):
            body = request.get_json()
            stock = body.get('stock')
            return jsonify(getStockAPIData(stock))
        
        
    api.add_resource(_Read, '/')

#if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
 #   server = 'https://flask.nighthawkcodingsociety.com' # run from web
 #   url = server + "/api/stock"
 #   responses = []  # responses list
    
