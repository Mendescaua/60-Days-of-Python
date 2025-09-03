from typing import Optional
#renomeei por conta que o sqlalchemy tbm tem BaseModel e para não confundir renomeei(ScBaseModel)
from pydantic import BaseModel as SCBaseModel

class UserSchema(SCBaseModel):
  id: Optional[int]
  name: str
  email: str
  password: int

  class Config:
    orm_mode = True
