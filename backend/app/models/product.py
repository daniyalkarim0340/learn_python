
from sqlalchemy import String, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Product(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String(500),
        nullable=True
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    is_available: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )
