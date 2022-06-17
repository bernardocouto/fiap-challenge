from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime, timedelta

import os

default_args = {
    'depends_on_past': False,
    'owner': 'fiap',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('databricks',
    catchup=False,
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2022, 1, 1)
) as dag:

    heatl_bronze = DatabricksRunNowOperator(
        databricks_conn_id='databricks_default',
        job_id=os.environ.get('HEALTH_BRONZE_JOB'),
        task_id='health_bronze'
    )

    heatl_silver = DatabricksRunNowOperator(
        databricks_conn_id='databricks_default',
        job_id=os.environ.get('HEALTH_SILVER_JOB'),
        task_id='health_silver'
    )

    sales_bronze = DatabricksRunNowOperator(
        databricks_conn_id='databricks_default',
        job_id=os.environ.get('SALES_BRONZE_JOB'),
        task_id='sales_bronze'
    )

    sales_silver = DatabricksRunNowOperator(
        databricks_conn_id='databricks_default',
        job_id=os.environ.get('SALES_SILVER_JOB'),
        task_id='sales_silver'
    )

    heatl_bronze >> heatl_silver
    sales_bronze >> sales_silver
