
import os
import requests
import json
from fastapi import APIRouter, Request

GPT_ROUTER = APIRouter(tags=["Chat-GPT"])

secret_key = os.getenv('OPENAI_API_KEY') #login into openai to generate a secret key
QUERY_MESSAGE = "list the possible ingredients that might be present in {} along with possible GI value for each ingredient. provide the response in the json format without any additional information, where the key will be the ingredient and value will be the GI value of that ingredient. Note: GI value should be an integer containing the value of GI"

@GPT_ROUTER.post('/v1/gpt', name="fetch response from chat gpt")
def get_ingredients(ingredient: str, request: Request):
	"""
	function to fetch the ingredients along with the GI values from GPT
	"""
	# Points need to be added in the API:
	# --> sort based on max used ingredient (even if the GI value is more, we need to show which ingredient is used in higher quantity)
	# --> Calarories, carbs, fats (Apart from ingredient name and GI value, we need to add these 3 parameters)
	try:
		url = 'https://api.openai.com/v1/chat/completions'
		headers = {"Content-Type": "application/json", "Authorization": "Bearer {}".format(secret_key)}
		payload = {
		"model": "gpt-3.5-turbo",
		"messages": [{"role": "user"}]
		}
		payload['messages'][0]['content'] = QUERY_MESSAGE.format(ingredient)

		response = requests.post(url, headers=headers, data=json.dumps(payload))
		response = eval(response.text) #formating the string to a Json/ dictionary format
		response = eval(response['choices'][0]['message']['content']) # fetching the Json response related to the ingredients
	except Exception as ex:
		response = {"status": "Failed To Fetch Response from GPT", "reason": str(ex)}
	return response
 