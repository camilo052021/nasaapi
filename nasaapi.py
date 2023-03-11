import os
import json
import requests
import pandas as pd


with open("config.json") as f:
    config = json.load(f)

url = config['url']
params = config['params']


def descargar_info(*args):
    res = requests.get(url, params=params)
    data = res.json()
    return data

data = descargar_info(url, params)
df = pd.json_normalize(data)
df = df.iloc[:, :5]
df.to_csv('data.txt', index=False)

