from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime

from . import Base


class User(Base):
    """ユーザー

    Args:
        Base (_type_): settingsで作成したBase
    """
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    age = Column('age', Integer)
    email = Column('email', String(100))

