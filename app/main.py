from fastapi import FastAPI
from middleware import request_id_middleware
from routers import greeting

app = FastAPI()

# Add request ID middleware
app.middleware("http")(request_id_middleware.request_id_middleware)

# Include routers
app.include_router(greeting.router)
