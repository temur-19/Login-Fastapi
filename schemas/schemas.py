from typing import Any

from pydantic import BaseModel, Field
from sqlalchemy import null


class LoginSchema(BaseModel):
    username: str
    password: str = Field(min_length=8)

class RegisterSchema(BaseModel):
    username: str
    password: str

