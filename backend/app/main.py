
from fastapi import FastAPI

from app.schemas.user import UserCreate
from app.routes.product import router as product_router

app = FastAPI(
    title="User Registration API",
    version="1.0.0"
)

# Register Product routes
app.include_router(product_router)


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
