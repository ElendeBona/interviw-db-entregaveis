from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2023, 1, 1),
    'catchup': False,
}

with DAG(
    dag_id='dbt_pipeline_dag_modular',
    default_args=default_args,
    schedule_interval='@daily',  # Uma vez por dia (00:00 UTC)
    description='Pipeline DBT completo: staging, marts e testes',
    tags=['dbt', 'movie_stream'],
) as dag:

    run_staging = BashOperator(
        task_id='run_dbt_staging',
        bash_command='cd /opt/airflow/dags/movie_stream_dbt && dbt run --select staging',
    )

    run_marts = BashOperator(
        task_id='run_dbt_marts',
        bash_command='cd /opt/airflow/dags/movie_stream_dbt && dbt run --select marts',
    )

    run_tests = BashOperator(
        task_id='run_dbt_tests',
        bash_command='cd /opt/airflow/dags/movie_stream_dbt && dbt test',
    )

    run_staging >> run_marts >> run_tests