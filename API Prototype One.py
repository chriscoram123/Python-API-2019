import flask
from flask import request, jsonify
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 04:19:36 2019

@author: christophercoram
"""
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Test data for catalog in the form of a list of directories
books = [
    {'id':0,
     'title': 'A Fire Upon The Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless',
     'year_published': '1992',
     },
     {'id':1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Usula k. Le Guin',
     'first_sentence': 'with a clamor of bells that set the swallows soaring high above.',
     'year_published': '1973',
     },
      {'id':2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city',
     'year_published': '1975',
     }
 ]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1>This site is a prototype API for distant reading"

# A route to return all available entries in our catalog.
@app.route('/api/v1/resources.books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1.resources/books/all', methods=['GET'])
def api_id():
    # Check if an ID was provided of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify."
    
    # Create an empty list for our results
    results = []
    
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many fields
    for book in books:
        if book['id'] == id:
            results.append(book)
            
    return jsonify(results)


app.run() 