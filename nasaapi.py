import os
import json
import requests
import pandas as pd


with open("config.json") as f:
    config = json.load(f)

url = config['url']
params = config['params']


def descargar_info(u: str, p: dict):
    res = requests.get(u, p)
    data = res.json()
    return data

# data = descargar_info(url, params)
# df = pd.json_normalize(data)
# df = df.iloc[:, :5]
# df['Date'] = df.iloc[:,0].str.slice(0,10)
# df['id'] = df.iloc[:,0].str.slice(9,13)
# df.to_csv('data.csv', index=False)

url_com = config['comm']['url_com']
params_com = config['comm']['params']
data_com = descargar_info(url_com,params_com)
df_com = pd.json_normalize(data_com)
df_com.to_csv('data_com.csv', index=False)
print(df_com)

