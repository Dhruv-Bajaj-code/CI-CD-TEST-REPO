from fastapi import FastAPI
from app.routers import health

app = FastAPI()

# Include the health check router
app.include_router(health.router)
