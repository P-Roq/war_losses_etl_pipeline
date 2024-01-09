import pytest
from database.db_models import (
    DBSession,
    TanksUkraine,
    AfvUkraine,
    IfvUkraine,
    ApcUkraine,
    ImvUkraine,
    TanksRussia,
    AfvRussia,
    IfvRussia,
    ApcRussia,
    ImvRussia,
)
from database.db_setup import SessionLocal
from sqlalchemy.orm import session
from sqlalchemy.orm.decl_api import DeclarativeMeta


#### Ukraine

@pytest.fixture
def test_db_operator():
    db_session = DBSession(SessionLocal, TanksUkraine)

    return db_session


def test_instantiate_db_session_tanks_ukraine(test_db_operator):

    assert isinstance(test_db_operator.SessionLocal, session.sessionmaker)
    assert isinstance(test_db_operator.Table, DeclarativeMeta)


#-----------------------------------------------------------------------------

@pytest.fixture
def test_db_operator():
    db_session = DBSession(SessionLocal, AfvUkraine)

    return db_session


def test_instantiate_db_session_afv_ukraine(test_db_operator):

    assert isinstance(test_db_operator.SessionLocal, session.sessionmaker)
    assert isinstance(test_db_operator.Table, DeclarativeMeta)


#-----------------------------------------------------------------------------

@pytest.fixture
def test_db_operator():
    db_session = DBSession(SessionLocal, IfvUkraine)

    return db_session


def test_instantiate_db_session_ifv_ukraine(test_db_operator):

    assert isinstance(test_db_operator.SessionLocal, session.sessionmaker)
    assert isinstance(test_db_operator.Table, DeclarativeMeta)

#-----------------------------------------------------------------------------

@pytest.fixture
def test_db_operator():
    db_session = DBSession(SessionLocal, ApcUkraine)

    return db_session


def test_instantiate_db_session_apc_ukraine(test_db_operator):

    assert isinstance(test_db_operator.SessionLocal, session.sessionmaker)
    assert isinstance(test_db_operator.Table, DeclarativeMeta)


#-----------------------------------------------------------------------------

@pytest.fixture
def test_db_operator():
    db_session = DBSession(SessionLocal, ImvUkraine)

    return db_session


def test_instantiate_db_session_imv_ukraine(test_db_operator):

    assert isinstance(test_db_operator.SessionLocal, session.sessionmaker)
    assert isinstance(test_db_operator.Table, DeclarativeMeta)


#-----------------------------------------------------------------------------

#### Russia

@pytest.fixture
def test_db_operator():
    db_session = DBSession(SessionLocal, TanksRussia)

    return db_session


def test_instantiate_db_session_tanks_russia(test_db_operator):

    assert isinstance(test_db_operator.SessionLocal, session.sessionmaker)
    assert isinstance(test_db_operator.Table, DeclarativeMeta)


#-----------------------------------------------------------------------------

@pytest.fixture
def test_db_operator():
    db_session = DBSession(SessionLocal, AfvRussia)

    return db_session


def test_instantiate_db_session_afv_russia(test_db_operator):

    assert isinstance(test_db_operator.SessionLocal, session.sessionmaker)
    assert isinstance(test_db_operator.Table, DeclarativeMeta)


#-----------------------------------------------------------------------------

@pytest.fixture
def test_db_operator():
    db_session = DBSession(SessionLocal, IfvRussia)

    return db_session


def test_instantiate_db_session_ifv_russia(test_db_operator):

    assert isinstance(test_db_operator.SessionLocal, session.sessionmaker)
    assert isinstance(test_db_operator.Table, DeclarativeMeta)

#-----------------------------------------------------------------------------

@pytest.fixture
def test_db_operator():
    db_session = DBSession(SessionLocal, ApcRussia)

    return db_session


def test_instantiate_db_session_apc_russia(test_db_operator):

    assert isinstance(test_db_operator.SessionLocal, session.sessionmaker)
    assert isinstance(test_db_operator.Table, DeclarativeMeta)


#-----------------------------------------------------------------------------

@pytest.fixture
def test_db_operator():
    db_session = DBSession(SessionLocal, ImvRussia)

    return db_session


def test_instantiate_db_session_imv_russia(test_db_operator):

    assert isinstance(test_db_operator.SessionLocal, session.sessionmaker)
    assert isinstance(test_db_operator.Table, DeclarativeMeta)


