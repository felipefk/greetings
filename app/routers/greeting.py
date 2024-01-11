from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse

# Create a FastAPI router instance
router = APIRouter()

# Dictionary mapping customer IDs to their respective greetings
greetings = {
    "A": "Hi",
    "B": "Dear Sir or Madam",
    "C": "Moin",
}

# Define a route for greeting customers
# The route uses a path parameter (customer_id) to determine the greeting
@router.get("/greet/{customer_id}", response_class=PlainTextResponse)
async def greet_customer(customer_id: str) -> str:
     # Retrieve the greeting based on the customer ID
    greeting = greetings.get(customer_id)

    # If the greeting is not found, return a 404 error
    if greeting is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    # Return the greeting as a plain text response
    return greeting
