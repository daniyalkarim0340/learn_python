
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate


def create_product(db: Session, product: ProductCreate):

    # Convert schema data into a database model object
    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price
    )

    # Add product to database session
    db.add(new_product)

    # Save changes to PostgreSQL
    db.commit()

    # Get the generated ID and other database values
    db.refresh(new_product)

    return new_product
