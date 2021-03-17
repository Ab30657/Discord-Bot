import requests
import json
querystring = {"fragment":"true","json":"true"}

headers = {
    'x-rapidapi-key': "e012d59038msh17ee95930b32c9cp1afd7bjsn54e24c8fcbf9",
    'x-rapidapi-host': "numbersapi.p.rapidapi.com"
    }


def get_response(_url):
  response= (requests.request("GET", _url, headers=headers, params=querystring))
  json_data= json.loads(response.text)
  return json_data

def get_num_fact(num):
  url = "https://numbersapi.p.rapidapi.com/{0}/math".format(num)
  json_data=get_response(url)
  return json_data['text'].capitalize()

def get_random_fact():
  url="https://numbersapi.p.rapidapi.com/random/trivia"
  json_data=get_response(url)
  return {'num': json_data['number'], 'fact': json_data['text'].capitalize()}