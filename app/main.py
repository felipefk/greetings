from fastapi import FastAPI
from routers import greeting

app = FastAPI()

# Include router from greeting.py
app.include_router(greeting.router)
