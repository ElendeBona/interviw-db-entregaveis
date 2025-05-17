from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2023, 1, 1),
    'catchup': False,
}

with DAG(
    dag_id='dbt_pipeline_dag',
    default_args=default_args,
    schedule_interval='0 8 * * *', # Executa diariamente às 08:00
    description='Executa o dbt build para os marts',
    tags=['dbt', 'movie_stream'],
) as dag:

    run_dbt = BashOperator(
        task_id='run_dbt_build_marts',
        bash_command='cd /opt/airflow/dags/movie_stream_dbt && dbt build --select marts',
    )

    run_dbt