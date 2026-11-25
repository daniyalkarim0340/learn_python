
from pydantic import BaseModel, Field


# Schema for creating a product
class ProductCreate(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    description: str | None = Field(
        default=None,
        max_length=500
    )

    price: float = Field(
        gt=0
    )

