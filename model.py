from typing import Optional, List
from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel


class UserType(str, Enum):
    user = "user"
    admin = "admin"
    fuel_supplier = "fuel_supplier"

    

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    username: str
    email: str
    first_name: Optional[str]
    password: str
    roles: List[UserType]

