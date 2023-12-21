import os
import json
import logging

current_dir = os.getcwd()

rel_runs_count_path = 'oryx_scrape/log_files/runs_count.json'
abs_runs_count_path = os.path.join(current_dir, rel_runs_count_path)

rel_scrapy_log_path = 'oryx_scrape/log_files/scrapy.log'
abs_scrapy_log_path = os.path.join(current_dir, rel_scrapy_log_path)


def register_run(count_path: str, log_file_path: str) -> None:
    """Register each log append per pipeline run by checking number of 
    scrapy runs in `log_counts.json`. If the number
    of runs exceeds 10, clean the scrapy log file.
    Note: each pipeline run equates to two crawling processes that
    are appended in sequence to the scrapy log file. For the intended
    purposes, they count as one (combined) run. 
    """

    with open(count_path, 'r') as file:
        runs_dump = json.load(file)
        runs = runs_dump['runs']
    
    if runs < 10:
        with open(count_path, 'w') as file:
            updated_runs = runs + 1
            dump = {"runs": updated_runs}
            json.dump(dump, file,)
    else:
        with open(count_path, 'w') as file:
            dump = {"runs": 1}
            json.dump(dump, file,)
        
        logging.basicConfig(
            filename=log_file_path,
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filemode='w',
            )

log_maintenance = register_run(abs_runs_count_path, abs_scrapy_log_path)
