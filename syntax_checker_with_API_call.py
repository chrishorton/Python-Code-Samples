import requests
import json
code_input = input("Enter a line of code")

paren_counter = 0
quote_counter = 0

for letter in code_input:
	if letter == "(" or letter == ")":
		paren_counter += 1
	elif letter == "\"":
		quote_counter += 1

if paren_counter % 2 == 0 and quote_counter % 2 == 0:
	print("syntax looks correct")
else: 
	print("syntax not correct")

api_key = "a257243860d54c9ab9d6527ddbe92034"
example_text = code_input # the text to be spell-checked
endpoint = "https://api.cognitive.microsoft.com/bing/v5.0/spellcheck"

data = {'text': example_text}
params = {
    'mkt':'en-us',
    'mode':'spell'
    }
headers = {
'Content-Type': 'application/x-www-form-urlencoded',
'Ocp-Apim-Subscription-Key': api_key,
}

response = requests.post(endpoint, headers=headers, params=params, data=data)
json_response = response.json()
print(json.dumps(json_response, indent=4))
