#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, abort, redirect
import unitOfWork
from jsonschema import validate
import validationschema

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def root_app():
	dataset = unitOfWork.Repository().select_all_users()		
	return jsonify(dataset)
	
@app.route('/api/people')
def mainpage():
	dataset = unitOfWork.Repository().select_all_users()		
	return jsonify(dataset)
	
@app.route('/api/people/<string:nationalId>', methods=['GET'])
def get(nationalId):
	dataset = unitOfWork.Repository().select_user(nationalId)
	if dataset is None:
         abort(404, 'The person does not exist')
	return jsonify(dataset)

@app.route('/api/people', methods=['POST'])
def post():
	if not is_valid_json(request.json):
		abort(400)
	dataset = unitOfWork.Repository().select_user(request.json["nationalId"])
	if dataset:		
         abort(400, 'The person already exists')
	try:
		if request.content_type != 'application/json':
			abort(400, 'Invalid Content-Type Header')
		unitOfWork.Repository().add_user(request.json)
		status_code = 201
		return jsonify({'Message':'Success'}), status_code, {'location': '/api/people/'+ request.json['nationalId']}
	except:
		abort(500)
		
@app.route('/api/people/<string:nationalId>', methods=['PUT'])
def put(nationalId):
	if not is_valid_json(request.json):
		abort(400)
	dataset = unitOfWork.Repository().select_user(nationalId)
	if dataset is None:
         abort(404, 'The person does not exist')
	try:
		if request.content_type != 'application/json':
			abort(400, 'Invalid Content-Type Header')

		unitOfWork.Repository().update_user(nationalId, request.json)
		return jsonify()
	except:
		abort(500)		
		

@app.route('/api/people/<string:nationalId>', methods=['DELETE'])
def delete(nationalId):
	dataset = unitOfWork.Repository().select_user(nationalId)
	if dataset is None:
         abort(404)
	unitOfWork.Repository().delete_user(nationalId)
	return jsonify()

def is_valid_json(jsonData):
	try:    
		personschema = validationschema.get_schema()
		validate(instance = jsonData, schema=personschema)
	except Exception as err:
		abort(400, "{}".format(err.message))
	return True	
	
	
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
