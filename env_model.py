from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


if os.getenv("PROJECTS_CONFIG"):

    config_path = os.getenv("PROJECTS_CONFIG")
    dotenv_path = f'{config_path}/war_losses_etl_pipeline_config/.env'

    load_dotenv(dotenv_path)

    class Settings(BaseSettings):
        # Database related.
        username: str = os.getenv("USER_NAME")
        key_db: str = os.getenv("SECRET_KEY")
        port: str = os.getenv("PORT")
        host: str = os.getenv("HOST")
        database: str = os.getenv("DATABASE")

else:
    class Settings(BaseSettings):

        load_dotenv()

        def get_secret(secret: str) -> str:
            with open(secret, 'r') as f:
                return f.read()
            
        key_db: str = get_secret(os.getenv('MYSQL_PASSWORD'))
        database: str = os.getenv('MYQL_DATABASE')
        username: str = os.getenv('MYSQL_USER')
        host: str = os.getenv('MYSQL_HOST')
        port: str = os.getenv('PORT')

settings = Settings()

