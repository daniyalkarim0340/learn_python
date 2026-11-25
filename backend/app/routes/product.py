
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.product import ProductCreate
from app.controllers.product import create_product


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    return create_product(db=db, product=product)
