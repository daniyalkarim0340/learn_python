
from fastapi import FastAPI

from app.schemas.user import UserCreate

app = FastAPI(
    title="User Registration API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "User Registration API is running"
    }


@app.post("/test-validation")
def test_validation(user: UserCreate):

    return {
        "message": "Validation successful",
        "full_name": user.full_name,
        "email": user.email
    }
