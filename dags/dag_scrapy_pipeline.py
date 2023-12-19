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
    description='run_the_pipeline_script',
    schedule='00 15 * * *',
    start_date=datetime(2023, 12, 11, 0, 0, 0),
    catchup=False,
    tags=['oryx_pipeline'],
    ) as dag:

    @task(task_id='run_scrape_pipeline')
    def scrape_and_store():
        import sys
        sys.path.append('../oryx_war_losses')
        from spider_runner import run_spiders

        return run_spiders()

    @task(task_id='check_for_pipeline_errors')
    def check_scrapy_log():
        import sys
        sys.path.append('../oryx_war_losses')
        from log_check_runner import check_errors

        return check_errors()


    task_1 = scrape_and_store()
    task_2 = check_scrapy_log()

    task_1 >> task_2


if __name__ == '__main__':
    dag.test()