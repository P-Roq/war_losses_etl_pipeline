from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry

from env_model import settings

engine = create_engine(
    f'mysql+pymysql://{settings.username}:{settings.key_db}@{settings.host}:{settings.port}/{settings.database}'
    )

mapper_registry = registry()

Base = mapper_registry.generate_base()

SessionLocal = sessionmaker(autoflush=False, bind=engine)
