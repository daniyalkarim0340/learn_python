
from app.database.connection import Base, engine

# Import models so SQLAlchemy knows about their tables
from app.models.user import User


def create_tables():

    print("Creating -database tables...")

    Base.metadata.create_all(bind=engine)

    print("Database tables created successfully!")


if __name__ == "__main__":
    create_tables()
