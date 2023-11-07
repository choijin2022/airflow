from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_conn_test",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 11, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
     # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )
    bash_t3 = BashOperator(
        task_id="bash_t3",
        bash_command="echo $HOSTNAME",
    )
    bash_t4 = BashOperator(
        task_id="bash_t4",
        bash_command="echo $HOSTNAME",
    )
    bash_t5 = BashOperator(
        task_id="bash_t5",
        bash_command="echo $HOSTNAME",
    )
    bash_t6 = BashOperator(
        task_id="bash_t6",
        bash_command="echo $HOSTNAME",
    )
    bash_t7 = BashOperator(
        task_id="bash_t7",
        bash_command="echo $HOSTNAME",
    )
    bash_t8 = BashOperator(
        task_id="bash_t8",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> [bash_t2, bash_t3] >> bash_t4 
    bash_t5 >> bash_t4
    [bash_t4, bash_t7] >> bash_t6 >> bash_t8
    # bash_t1.set_downstream([bash_t2, bash_t3])
    # bash_t4.set_upstream([bash_t2, bash_t3,bash_t5])
    # bash_t6.set_upstream([bash_t4, bash_t7])
    # bash_t6.set_downstream(bash_t8)

    

