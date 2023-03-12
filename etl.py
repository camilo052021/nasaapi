""" importamos las librerías necesarias para el etl y paso de la infromación a postgresql"""
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

""" hacemos la llamda a los archivos producto de la extracción hecha en el mudulo nasaapi usando pandas"""
dc = pd.read_csv("data_com.csv")
datamain = pd.read_csv("data.csv")
fy = pd.read_csv("fundation.txt", encoding='utf-8')
tbu = pd.read_csv("tablaunion.txt")

""" abrimos y alamcenamos la infromacion que hay en el arhcivo de configuración json"""
with open("config.json") as f:
    config = json.load(f)

""" abrimos y alamcenamos la infromacion que hay en el arhcivo de sql"""
with open("codigo_sql.sql") as s:
    sql = s.read()

""" asignamos las variables para la conexión a la base de datdos, la información la extraemos del 
    archivo config.json """
database = config['cnx']['database']
user = config['cnx']['user']
password = config['cnx']['password']

""" 
Unir "datamain" y "tbu" en una nueva tabla "result" utilizando la columna "id" como clave primaria en ambas tablas
Unir "result" y "dc" en "result" utilizando la columna "id_cmr" como clave primaria en "result" y "id" en "dc"
Unir "result" y "fy" en "result" utilizando la columna "brand" como clave primaria en "result" y "brand_com" en "fy"
Convertir "result" en un dataframe de pandas
Eliminar las columnas "id_cmr", "id_ns" y "brand_com" de "result" Guardar "result" en un archivo CSV llamado 
"resultado.csv" sin incluir los índices de las filas
"""
result = pd.merge(left=datamain,right=tbu, how='right', left_on='id', right_on='id_ns')
result = pd.merge(left=result,right=dc, how='left', left_on='id_cmr', right_on='id')
result = pd.merge(left=result, right=fy, how='left', left_on='brand', right_on='brand_com')
df = pd.DataFrame(result)
result = df.drop(['id_cmr','id_ns','brand_com'], axis=1)    
result.to_csv('resultado.csv', index=False)


"""
Definir una función llamada cargaDataSql que toma dos argumentos: "data" y "tbl" (el nombre de la tabla)
"""
def cargaDataSql(data, tbl):

    conn = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host="localhost",
    port="5432"
    )

    # Crear un cursor para ejecutar comandos SQL en la base de datos
    cursor = conn.cursor()

    # Ejecutar una sentencia SQL (almacenada en la variable "sql") para crear la tabla "tbl"
    create_table = sql
    cursor.execute(create_table)
    
    # Confirmar los cambios en la base de datos y cerrar la conexión
    conn.commit()
    conn.close()

    # Crear un motor SQLAlchemy para interactuar con la base de datos PostgreSQL
    # Convertir los datos a un marco de datos de pandas
    # Escribir el marco de datos en la tabla especificada en la base de datos utilizando el motor SQLAlchemy
    engine = create_engine("postgresql://postgres:1234@localhost:5432/dbpruebas")
    data = pd.DataFrame(data)
    data.to_sql(tbl, con=engine, if_exists='replace', index=False)

""" llamada a la función creada para cargara la información a una tabla en especifico """
cargaDataSql(result, 'results')