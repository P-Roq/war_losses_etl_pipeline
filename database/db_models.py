from sqlalchemy import (
    Column,
    Integer,
    Integer,
    DateTime,
    )

from sqlalchemy.sql import func

from datetime import datetime

from .db_setup import Base

class TanksUkraine(Base):
    __tablename__ = 'tank_ukraine'
    tanks_ukraine_id = Column(Integer, primary_key=True, autoincrement=True, unique=True,)
    total = Column(Integer, nullable=False,)
    destroyed = Column(Integer, nullable=False,)
    damaged = Column(Integer, nullable=False,)
    abandoned = Column(Integer, nullable=False,)
    captured = Column(Integer, nullable=False,)
    scraped_at = Column(DateTime, unique=True,)
    created_at = Column(DateTime(timezone=True,), default=datetime.utcnow, nullable=False)

class AfvUkraine(Base):
    __tablename__ = 'afv_ukraine'
    afv_ukraine_id = Column(Integer, primary_key=True, autoincrement=True, unique=True,)
    total = Column(Integer, nullable=False,)
    destroyed = Column(Integer, nullable=False,)
    damaged = Column(Integer, nullable=False,)
    abandoned = Column(Integer, nullable=False,)
    captured = Column(Integer, nullable=False,)
    scraped_at = Column(DateTime, unique=True,)
    created_at = Column(DateTime(timezone=True,), default=datetime.utcnow, nullable=False)

class IfvUkraine(Base):
    __tablename__ = 'ifv_ukraine'
    ifv_ukraine_id = Column(Integer, primary_key=True, autoincrement=True, unique=True,)
    total = Column(Integer, nullable=False,)
    destroyed = Column(Integer, nullable=False,)
    damaged = Column(Integer, nullable=False,)
    abandoned = Column(Integer, nullable=False,)
    captured = Column(Integer, nullable=False,)
    scraped_at = Column(DateTime, unique=True,)
    created_at = Column(DateTime(timezone=True,), default=datetime.utcnow, nullable=False)

class ApcUkraine(Base):
    __tablename__ = 'apc_ukraine'
    apc_ukraine_id = Column(Integer, primary_key=True, autoincrement=True, unique=True,)
    total = Column(Integer, nullable=False,)
    destroyed = Column(Integer, nullable=False,)
    damaged = Column(Integer, nullable=False,)
    abandoned = Column(Integer, nullable=False,)
    captured = Column(Integer, nullable=False,)
    scraped_at = Column(DateTime, unique=True,)
    created_at = Column(DateTime(timezone=True,), default=datetime.utcnow, nullable=False)


class ImvUkraine(Base):
    __tablename__ = 'imv_ukraine'
    imv_ukraine_id = Column(Integer, primary_key=True, autoincrement=True, unique=True,)
    total = Column(Integer, nullable=False,)
    destroyed = Column(Integer, nullable=False,)
    damaged = Column(Integer, nullable=False,)
    abandoned = Column(Integer, nullable=False,)
    captured = Column(Integer, nullable=False,)
    scraped_at = Column(DateTime, unique=True,)
    created_at = Column(DateTime(timezone=True,), default=datetime.utcnow, nullable=False)

#----------------------------------------------------------------------------------------------------

class TanksRussia(Base):
    __tablename__ = 'tank_russia'
    tanks_russia_id = Column(Integer, primary_key=True, autoincrement=True, unique=True,)
    total = Column(Integer, nullable=False,)
    destroyed = Column(Integer, nullable=False,)
    damaged = Column(Integer, nullable=False,)
    abandoned = Column(Integer, nullable=False,)
    captured = Column(Integer, nullable=False,)
    scraped_at = Column(DateTime, unique=True,)
    created_at = Column(DateTime(timezone=True,), default=datetime.utcnow, nullable=False)


class AfvRussia(Base):
    __tablename__ = 'afv_russia'
    afv_russia_id = Column(Integer, primary_key=True, autoincrement=True, unique=True,)
    total = Column(Integer, nullable=False,)
    destroyed = Column(Integer, nullable=False,)
    damaged = Column(Integer, nullable=False,)
    abandoned = Column(Integer, nullable=False,)
    captured = Column(Integer, nullable=False,)
    scraped_at = Column(DateTime, unique=True,)
    created_at = Column(DateTime(timezone=True,), default=datetime.utcnow, nullable=False)

class IfvRussia(Base):
    __tablename__ = 'ifv_russia'
    ifv_russia_id = Column(Integer, primary_key=True, autoincrement=True, unique=True,)
    total = Column(Integer, nullable=False,)
    destroyed = Column(Integer, nullable=False,)
    damaged = Column(Integer, nullable=False,)
    abandoned = Column(Integer, nullable=False,)
    captured = Column(Integer, nullable=False,)
    scraped_at = Column(DateTime, unique=True,)
    created_at = Column(DateTime(timezone=True,), default=datetime.utcnow, nullable=False)

class ApcRussia(Base):
    __tablename__ = 'apc_russia'
    apc_russia_id = Column(Integer, primary_key=True, autoincrement=True, unique=True,)
    total = Column(Integer, nullable=False,)
    destroyed = Column(Integer, nullable=False,)
    damaged = Column(Integer, nullable=False,)
    abandoned = Column(Integer, nullable=False,)
    captured = Column(Integer, nullable=False,)
    scraped_at = Column(DateTime, unique=True,)
    created_at = Column(DateTime(timezone=True,), default=datetime.utcnow, nullable=False)


class ImvRussia(Base):
    __tablename__ = 'imv_russia'
    imv_russia_id = Column(Integer, primary_key=True, autoincrement=True, unique=True,)
    total = Column(Integer, nullable=False,)
    destroyed = Column(Integer, nullable=False,)
    damaged = Column(Integer, nullable=False,)
    abandoned = Column(Integer, nullable=False,)
    captured = Column(Integer, nullable=False,)
    scraped_at = Column(DateTime, unique=True,)
    created_at = Column(DateTime(timezone=True,), default=datetime.utcnow, nullable=False)


#-----------------------------------------------------------------------------------------------------------------------

table_classes_ukraine = [
    TanksUkraine,
    AfvUkraine,
    IfvUkraine,
    ApcUkraine,
    ImvUkraine,
]

table_classes_russia = [
    TanksRussia,
    AfvRussia,
    IfvRussia,
    ApcRussia,
    ImvRussia,
]

#-----------------------------------------------------------------------------------------------------------------------

class DBSession:
    def __init__(self, session_local, Table,):
        self.SessionLocal = session_local
        self.Table = Table

    def add_resource(self, dump: dict) -> None:

        session_instance = self.SessionLocal()
        
        new_resource = self.Table(**dump)

        try:
            with session_instance as session:
                session.begin()
                session.add(new_resource)
                session.commit()

        except Exception as e:
            with session_instance as session:
                session.rollback()
                raise Exception(f"Failed to add item to database: {e}")
        
        return
    

    def fetch_scraped_at_dates(self,) -> list:

        session_instance = self.SessionLocal()

        dates = (
            session_instance
            .query(self.Table.scraped_at)
            .all()
            )
        
        dates = [tuple_[0] for tuple_ in dates] # unfold
        
        return dates


    def fetch_losses_by_loss_type(self, loss_type: str):

        column_identifier = getattr(self.Table, loss_type)

        session_instance = self.SessionLocal()

        dates = (
            session_instance
            .query(column_identifier, self.Table.scraped_at)
            .all()
            )
        
        return dates