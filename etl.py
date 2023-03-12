import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import json

dc = pd.read_csv("data_com.csv")
datamain = pd.read_csv("data.csv")
fy = pd.read_csv("fundation.txt", encoding='utf-8')
tbu = pd.read_csv("tablaunion.txt")

with open("config.json") as f:
    config = json.load(f)

with open("codigo_sql.sql") as s:
    sql = s.read()

database = config['cnx']['database']
user = config['cnx']['user']
password = config['cnx']['password']

result = pd.merge(left=datamain,right=tbu, how='right', left_on='id', right_on='id_ns')
result = pd.merge(left=result,right=dc, how='left', left_on='id_cmr', right_on='id')
result = pd.merge(left=result, right=fy, how='left', left_on='brand', right_on='brand_com')
df = pd.DataFrame(result)
result = df.drop(['id_cmr','id_ns','brand_com'], axis=1)

result.to_csv('resultado.csv', index=False)


def cargaDataSql(data, tbl):

    conn = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host="localhost",
    port="5432"
    )

    cursor = conn.cursor()

    create_table = sql
    cursor.execute(create_table)
    
    conn.commit()
    conn.close()

    engine = create_engine("postgresql://postgres:1234@localhost:5432/dbpruebas")
    data = pd.DataFrame(data)
    data.to_sql(tbl, con=engine, if_exists='replace', index=False)


cargaDataSql(result, 'results')