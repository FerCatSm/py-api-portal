
def get_schema():
	personschema = {
	  "$schema": "http://json-schema.org/draft-04/schema#",
	  "type": "object",
	  "properties": {
	    "age": {
	      "type": "integer"
	    },
	    "lastName": {
	      "type": "string"
	    },
	    "name": {
	      "type": "string"
	    },
	    "nationalId": {
	      "type": "string"
	    },
	    "originPlanet": {
	      "type": "string"
	    },
	    "pictureUrl": {
	      "type": "string"
	    }
	  },
	  "required": [
	    "age",
	    "lastName",
	    "name",
	    "nationalId",
	    "originPlanet",
	    "pictureUrl"
	  ]
	}
	return personschema
