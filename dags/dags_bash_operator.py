from __future__ import annotations

import datetime
import pendulum
from airflow.operators.bash import BashOperator


from airflow.models.dag import DAG

# catchhup=False: 과거의 DAG Run을 실행하지 않음 -> 불필요하게 catchup을 할 경우 자원 낭비가 심함 ex) 하루 치 분량 실패 시 3달치를 전부 실행 

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
) as dag:
    bash_t1 = BashOperator(
                task_id="bash_t1",
                bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
                task_id="bash_t2",
                bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2
