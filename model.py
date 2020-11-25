from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Boolean

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    username = Column(String(150), unique=True)
    email = Column(String(150))
    password = Column(String(150))
    is_active = Column(Boolean(), default=True)
