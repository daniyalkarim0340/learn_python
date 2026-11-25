
from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class User(Base):

    # PostgreSQL table name
    __tablename__ = "users"

    # User ID: Primary Key
    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    # User's full name
    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Email must be unique
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    # We store a password hash, never the original password
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # Account status
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    # Account creation date
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
