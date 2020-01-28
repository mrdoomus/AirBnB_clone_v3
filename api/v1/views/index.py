#!/usr/bin/python3
"""  """
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def get_status():
    """ Return status of the APP as OK """
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def get_stats():
    """ Return count of every class in dictionary """
    return jsonify(amenity=storage.count('Amenity'),
                   cities=storage.count('City'),
                   places=storage.count('Place'),
                   reviews=storage.count('Review'),
                   states=storage.count('State'),
                   users=storage.count('User'))
