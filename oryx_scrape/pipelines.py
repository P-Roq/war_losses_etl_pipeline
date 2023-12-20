import sys
import os
import re

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
project_root = re.sub('/oryx_scrape', '', project_root)
sys.path.append(project_root)

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
from datetime import datetime

from database.db_setup import SessionLocal
import database.db_models as models
from oryx_scrape.spiders_settings import spider_ukraine, spider_russia


class OryxScrapePipeline:
    def __init__(self,):
        self.spider_ukraine = spider_ukraine
        self.spider_russia = spider_russia

    def process_item(self, item, spider):
        """ The `item` is `total_casualties` dictionary with the keys:
        'tank', 'afv', 'ifv', 'apc', 'imv'.
        """

        if spider.name == self.spider_ukraine:
            table_classes = models.table_classes_ukraine

        if spider.name == self.spider_russia:
            table_classes = models.table_classes_russia

        for index, key in enumerate(list(item.keys())):
            resource = item[key]

            Table = table_classes[index]

            db_session = models.DBSession(SessionLocal, Table)
            
            dates = db_session.fetch_scraped_at_dates()

            if dates:
                now = datetime.utcnow()
                today = datetime(now.year, now.month, now.day)

                if today not in dates:
                    db_session.add_resource(resource)
                else:
                    message = 'An entry in the database table already as the same scraped date ("scraped_at").'
                    logging.info(message)
            else:
                db_session.add_resource(resource)
        
        return item
