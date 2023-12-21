import os
import time
import subprocess

from oryx_scrape.spiders_settings import spider_russia, spider_ukraine
from oryx_scrape.log_maintenance import log_maintenance

project_root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))

output_path_ukraine = project_root_path + '/scraped_data/losses_ukraine.json'
output_path_russia = project_root_path + '/scraped_data/losses_russia.json'

def run_spider(spider_name, output_file):
    """Since the data is being pipelined into a database we just keep the
    last scraped data into JSON files, overwriting it at every new run.
    """
    
    os.chdir(f'{project_root_path}/oryx_scrape/spiders')
    subprocess.run(['scrapy', 'crawl', spider_name, '-O', output_file,])

def run_spiders():
    spiders = [
        (spider_ukraine, output_path_ukraine),
        (spider_russia, output_path_russia)
        ]

    delay_between_runs = 2  

    for spider, data_path in spiders:
        run_spider(spider, data_path)
        time.sleep(delay_between_runs)

def main():
    log_maintenance
    run_spiders()

if __name__ == '__main__':
    main()