
from pydantic import BaseModel, EmailStr, Field


# Schema for user registration
class UserCreate(BaseModel):

    full_name: str = Field(
        min_length=3,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128
    )
