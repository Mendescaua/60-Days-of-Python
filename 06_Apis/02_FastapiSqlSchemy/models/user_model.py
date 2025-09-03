from core.configs import settings
from sqlalchemy import Column, Integer, String


class UserModel(settings.DBBaseModel):
    __tablename__ = 'user'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(100))
    email: str = Column(String(100))
    password: int = Column(Integer)
