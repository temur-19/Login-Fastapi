from typing import Any

from pydantic import BaseModel, Field
from sqlalchemy import null


class LoginSchema(BaseModel):
    username: str
    password: str = Field(min_length=8)

class RegisterSchema(BaseModel):
    def __init__(self, /, **data: Any):
        super().__init__(null, data)
        self.user = None
    username: str
    password: str

