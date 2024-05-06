from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task

default_args = {
    'owner': 'P-roq',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
    'trigger_rule': 'all_success',
}

with DAG(
    'scrapy_pipeline',
    default_args=default_args,
    description='Scrape and store data from oryx website.',
    schedule='00 14 * * *',
    start_date=datetime(2023, 12, 11, 0, 0, 0),
    catchup=False,
    tags=['oryx'],
    ) as dag:

    @task(task_id='run_scrapy_pipeline')
    def scrape_and_store():
        from spider_runner import main

        return main()

    @task(task_id='check_for_pipeline_errors')
    def check_scrapy_log():
        from log_check_runner import check_errors

        try:
            return check_errors()
        except Exception as e:
            ti = check_scrapy_log.get_task_instance()
            ti.log.error(f'Task failed with exception: {e}')
            raise

    task_a = check_scrapy_log()
    task_b = scrape_and_store()
    task_c = scrape_and_store()

    task_a >> task_b >> task_c


if __name__ == '__main__':
    dag.test()