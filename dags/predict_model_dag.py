from airflow.decorators import dag, task
from datetime import datetime, timedelta
import sys
import pandas as pd
import joblib
from sqlalchemy import create_engine

sys.path.append('/opt/airflow/scripts')

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'email_on_failure': False,
    'email_on_retry': False,
    'email_on_success': False
}


@dag(
    dag_id='predict_model_dag',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=['ml', 'predict']
)


def prediction_pipeline():

    @task()
    def procesar_datos():
        df = pd.read_csv('/opt/airflow/data/nuevas_consultas.csv')

        df["sexo"] = df["sexo"].map({"M": 0, "F": 1})
        df_filtrado = df[["id_paciente", "edad", "sexo", "hipertension", 
                          "diabetes", "visitas_ultimo_mes"]]
        df_filtrado.to_csv('/opt/airflow/data/datos_procesados.csv', index=False)
        print("✅ Datos procesados guardados en datos_procesados.csv")


    @task()
    def predecir():
        engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres/airflow')
        df = pd.read_sql("SELECT * FROM datos_entrada WHERE fecha_consulta = CURRENT_DATE", engine)
        if df.empty:
            print("No hay datos para la fecha actual. No se realizarán predicciones")
            return

        modelo = joblib.load('/opt/airflow/models/modelo_entrenado.pkl')
        X = df[["edad", "sexo", "hipertension", "diabetes", "visitas_ultimo_mes"]]
        df["riesgo_hospitalizacion"] = modelo.predict(X)
        df[['id_paciente', 'riesgo_hospitalizacion']].to_sql('predicciones', engine, if_exists='append', index=False)

        print("Predicciones guardadas en la base de datos de PostgreSQL")

    procesar = procesar_datos()
    predecir = predecir()
    procesar >> predecir

dag_instance = prediction_pipeline()

