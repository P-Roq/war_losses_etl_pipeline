import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import registry

from env_model import settings


from dotenv import load_dotenv
import logging
import re 
import os

load_dotenv()

def check_database_connection() -> None:
    
    root_path = re.split(':', os.getenv('PYTHONPATH'))[0]
    log_path = f'{root_path}/database'

    logging.basicConfig(filename=f'{log_path}/database.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


    try:
        connection = pymysql.connect(host=settings.host, user=settings.username, password=settings.key_db, database=settings.database)
        connection.ping(reconnect=True)
        print('Successful connection to database.')
    
    except pymysql.MySQLError as e:
        logging.error('Connection error: %s', e)
        raise Exception('Connection error: %s', e)


engine = create_engine(
    f'mysql+pymysql://{settings.username}:{settings.key_db}@{settings.host}:{settings.port}/{settings.database}'
    )

mapper_registry = registry()

Base = mapper_registry.generate_base()

SessionLocal = sessionmaker(autoflush=False, bind=engine)
