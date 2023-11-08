from __future__ import annotations
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
import datetime
import pendulum


with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 10, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    send_eamil_task = EmailOperator(
        task_id = 'send_eamil_task',
        to = 'choeji2022@gmail.com',
        subject = 'airflow 성공 메일',
        html_content = 'airflow 작업이 완료되었습니다',
        conn_id="your_smtp_connection", 
        dag=dag,

    )