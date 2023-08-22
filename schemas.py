from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class AccountCreate(BaseModel):
    name:str
    surname:str
    email: str
    birthdate: datetime
    phone_number: Optional[str]
    password: