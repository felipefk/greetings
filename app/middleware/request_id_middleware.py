from fastapi import Request
import uuid

async def request_id_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id  # Attach UUID to the request state
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id  # Include UUID in the response headers
    return response
