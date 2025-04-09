from airflow.decorators import dag, task
from datetime import datetime, timedelta
import sys
sys.path.append('/opt/airflow/scripts')  # Importar desde el contenedor


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'email_on_failure': False,
    'email_on_retry': False,
    'email_on_success': False
}


@dag(
    dag_id='train_model_dag',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,  # Ejecutamos manualmente por ahora
    catchup=False,
    tags=['ml', 'train']
)


def train_pipeline():

    @task()
    def run_training():
        from train_model import train_model
        train_model()

    run_training()


dag_instance = train_pipeline()

