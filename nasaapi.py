import os
import json
import requests


with open("config.json") as data:
    params = json.load(data)

url = f"{params['url']}startDate={params['dateinit']}&endDate{params['dateend']}&api_key={params['apikey']}"
#url = "https://api.nasa.gov/DONKI/CME?startDate=2020-10-10&endDate=2020-12-31&api_key=MtjvxnRz8LlJjBd0Y5RrZpwwRdhHw7XlfxayRFif"
print(url)

# params = {
#     params['dateinit'],
#     params['dateend'],
#     params['apikey']sss
#  }

def descargar_info():
    res = requests.get(url)
    return res.text


print(descargar_info())