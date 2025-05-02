import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data/historico.csv')

engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres/airflow")

df.to_sql("datos_entrada", engine, if_exists='replace', index=False)

print("Datos históricos cargados en PostgreSQL")
