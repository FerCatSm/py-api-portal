#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, abort, redirect
import unitOfWork

app = Flask(__name__)


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
	
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
