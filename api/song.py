from flask import Flask, jsonify, request
import requests
import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required



app = Flask(__name__)

@app.route('/search')
def search_songs():
    search_term = request.args.get('term')
    if not search_term:
        return jsonify({'error': 'Search term is required'}), 400
    
    itunes_api_url = f'https://itunes.apple.com/search?term={search_term}&entity=song&limit=10'
    response = requests.get(itunes_api_url)
    
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data from iTunes API'}), response.status_code
    
    data = response.json()
    return jsonify(data)
