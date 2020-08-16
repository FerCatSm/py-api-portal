#!/usr/bin/env python3

from main import app
import pytest


@pytest.fixture
def test_not_found_data():
	return "111111111-7"

	
def test_root_app():
	r = app.test_client().get()
	assert r.status_code == 200	
	
def test_get(test_not_found_data):
	r = app.test_client().get(test_not_found_data)
	assert r.status_code == 404

	

