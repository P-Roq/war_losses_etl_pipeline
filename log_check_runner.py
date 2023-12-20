import re
import os
from env_model import settings
from spider_runner import project_root_path

log_path = project_root_path + '/oryx_scrape/log_files/scrapy.log'

with open(log_path, 'r') as file:
    log = file.readlines() 


def check_errors():
    for line in log:
        if re.findall('\sERROR\s', line,):
            raise Exception('An error has been found during a scrapy run.')
    else:
        return