import sqlalchemy as sa
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.future.engine import Engine
from typing import Optional
from models.model_base import ModelBase

__engine: Optional[Engine] = None


def create_engine():
    """
    Função para configurar a conexão ao banco de dados.
    """
    global __engine

    if __engine:
        return

    conn_str = 'postgresql://postgres:@Mc140723@localhost:5732/USERS'
    __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    """
    Função para criar a sessão de conexão ao banco de dados
    """

    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session


def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()

    import models.__all_models
    ModelBase.metadata.drop.all(__engine)
    ModelBase.metadata.creat.all(__engine)
