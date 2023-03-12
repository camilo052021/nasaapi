import os
import json
import requests
import pandas as pd

"""
Abre y carga un archivo JSON de configuración.
"""
with open("config.json") as f:
    config = json.load(f)


url = config['url']
params = config['params']

"""
Define una función para descargar información de una URL utilizando la biblioteca "requests".
Utiliza los datos cargados del archivo JSON para enviar una solicitud HTTP a la URL.
Devuelve los datos de la solicitud como resultado de la función.
"""
def descargar_info(u: str, p: dict):
    res = requests.get(u, p)
    data = res.json()
    return data

"""
Llama a la función "descargar_info" para obtener los datos de una URL utilizando los parámetros especificados.
Normaliza los datos JSON utilizando la función "pd.json_normalize".
Selecciona las primeras 5 columnas del dataframe utilizando la función "iloc".
Agrega una nueva columna "Date" utilizando la función "str.slice".
Agrega una nueva columna "id" utilizando la función "str.slice".
"""
data = descargar_info(url, params)
df = pd.json_normalize(data)
df = df.iloc[:, :5]
df['Date'] = df.iloc[:,0].str.slice(0,10)
df['id'] = df.iloc[:,0].str.slice(9,13)
df.to_csv('data.csv', index=False)

"""
Guarda el dataframe resultante en un archivo CSV utilizando la función "to_csv".
Carga la URL y los parámetros de comentarios desde el archivo de configuración.
Llama a la función "descargar_info" para obtener los datos de la URL y los parámetros de comentarios.
Normaliza los datos JSON 
Guarda el dataframe resultante en un archivo CSV utilizando la función "to_csv".
Imprime el dataframe resultante en la consola utilizando la función "print".
"""
url_com = config['comm']['url_com']
params_com = config['comm']['params']
data_com = descargar_info(url_com,params_com)
df_com = pd.json_normalize(data_com)
df_com.to_csv('data_com.csv', index=False)
print(df_com)

