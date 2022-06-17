from airflow import DAG
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.airbyte.sensors.airbyte import AirbyteJobSensor
from datetime import datetime, timedelta

import os

default_args = {
    'depends_on_past': False,
    'owner': 'fiap',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('airbyte',
    catchup=False,
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2022, 1, 1)
) as dag:

    heatl_landing = AirbyteTriggerSyncOperator(
        airbyte_conn_id='airbyte_default',
        asynchronous=False,
        connection_id=os.environ.get('HEALTH_LANDING_CONNECTION'),
        task_id='heatl_landing'
    )

    heatl_landing_sensor = AirbyteJobSensor(
        airbyte_conn_id='airbyte_default',
        airbyte_job_id=heatl_landing.output,
        task_id='heatl_landing_sensor'
    )

    sales_landing = AirbyteTriggerSyncOperator(
        airbyte_conn_id='airbyte_default',
        asynchronous=False,
        connection_id=os.environ.get('SALES_LANDING_CONNECTION'),
        task_id='sales_landing'
    )

    sales_landing_sensor = AirbyteJobSensor(
        airbyte_conn_id='airbyte_default',
        airbyte_job_id=sales_landing.output,
        task_id='sales_landing_sensor'
    )

    heatl_landing >> heatl_landing_sensor
    sales_landing >> sales_landing_sensor
