import requests
import json
from typing import Union

'''
pantry_wrapper - a Python wrapper for the Pantry API (https://getpantry.cloud)

This is a simple, one-file wrapper for Python to cut down the code for making calls to the Pantry API

For more information and documentation about pantry_wrapper, see the GitHub repo here: https://github.com/alexmulligan/pantry_wrapper

For more information about Pantry itself, go to their webpage or their GitHub repo at https://github.com/imRohan/Pantry
'''

# sets what the wrapper functions will return by default
# can be 'response' or 'body'
#	  'response' will return a Response object (from requests)
#   'body' will return the body of the response as a dict if it's json, or just a string for anything else
DEFAULT_RETURN_TYPE = 'response'


def _format_body(res: str) -> Union[str, dict]:
	"""private function used to return response body as a dict if it's JSON, and as a string otherwise"""
	
	res = res.strip() # remove any extra whitespace or newline characters at beginning or end
	try:
		body = json.loads(res)
	except: # if json.loads fails, it must not be JSON so return it as is
		body = res
	return body


def _pantry_call(pantry_id: str, request_type: str, name: str=None, contents: dict=None, return_type: str=DEFAULT_RETURN_TYPE) -> Union[str, dict]:
	"""private base function for other API call functions"""
	
	url = f"https://getpantry.cloud/apiv1/pantry/{pantry_id}"
	if name != None and name.strip() != '':
		# if a basket name is passed, it should be added to the URL
		url += f"/basket/{name}"
	
	# if data is passed as 'contents', convert it to string to add to the request, else leave it empty
	if contents != None:
		payload = json.dumps(contents)
	else:
		payload = ""
	
	headers= {
		'Content-Type': 'application/json'
	}
	# request_type is passed by the individual wrapper functions;
	# the Pantry API uses the same-ish URL endpoint but different HTTP methods for the different functions 
	response = requests.request(request_type, url, headers=headers, data=payload)
	
	# two options to return: the whole Response object, or just the data from the body (string or JSON)
	if return_type.strip().lower() == 'response':
		return response
	elif return_type.strip().lower() == 'body':
		return _format_body(response.text)
	else:
		return None
		

def pantry_info(pantry_id: str, return_type: str=DEFAULT_RETURN_TYPE) -> Union[str, dict]:
	"""returns info about the pantry, including a list of baskets stored inside"""
	return _pantry_call(pantry_id, request_type='GET', return_type=return_type)


def get_contents(pantry_id: str, name: str, return_type: str=DEFAULT_RETURN_TYPE) -> Union[str, dict]:
	"""returns full contents of basket"""
	return _pantry_call(pantry_id, request_type='GET', name=name, return_type=return_type)


def create_basket(pantry_id: str, name: str, contents: dict, return_type: str=DEFAULT_RETURN_TYPE) -> Union[str, dict]:
	"""creates a new basket or replaces an existing one"""
	return _pantry_call(pantry_id, request_type='POST', name=name, contents=contents, return_type=return_type)
	

def append_basket(pantry_id: str, name: str, contents: dict, return_type: str=DEFAULT_RETURN_TYPE) -> Union[str, dict]:
	"""appends contents to new or existing basket; will overwrite values of existing keys and append values to nested objects or arrays"""
	return _pantry_call(pantry_id, request_type='PUT', name=name, contents=contents, return_type=return_type)


def delete_basket(pantry_id: str, name: str, return_type: str=DEFAULT_RETURN_TYPE) -> Union[str, dict]:
	"""deletes entire basket and its contents"""
	return _pantry_call(pantry_id, request_type='DELETE', name=name, return_type=return_type)

