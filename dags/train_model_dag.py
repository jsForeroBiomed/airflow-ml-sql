from airflow.decorators import dag, task
from datetime import datetime, timedelta
import sys
from airflow.utils.email import send_email

sys.path.append('/opt/airflow/scripts')  # Importar desde el contenedor


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'email_on_failure': False,
    'email_on_retry': False,
    'email_on_success': False
}



def success_email(context):
    task = context["task_instance"]
    subject = f"Éxito en la tarea: {task.task_id}"
    body = f"""
    La tarea <b>{task.task_id}</b> finalizó exitosamente.<br>
    Fecha de ejecución: {context['execution_date']}<br>
    Ver logs: <a href="{task.log_url}">{task.log_url}</a>
    """
    send_email(to="JSFORERO.BIOMED@GMAIL.COM", subject=subject, html_content=body)



def failure_email(context):
    task = context["task_instance"]
    subject = f"Fallo en la tarea_ {task.task_id}"
    body = f"""
    La tarea <b>{task.task_id}</b> falló.<br>
    Fecha de ejecución: {context['execution_date']}<br>
    Ver logs: <a href="{task.log_url}">{task.log_url}</a>
    """
    send_email(to="JSFORERO.BIOMED@GMAIL.COM", subject=subject, html_content=body)




@dag(
    dag_id='train_model_dag',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,  
    catchup=False,
    tags=['ml', 'train'],
    on_success_callback=success_email,
    on_failure_callback=failure_email
)


def train_pipeline():

    @task()
    def run_training():
        from train_model import train_model
        train_model()

    run_training()


dag_instance = train_pipeline()



