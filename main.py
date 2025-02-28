from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

# Data model
class Transaction(BaseModel):
    transaction_id: int
    customer_id: int
    product_id: int
    quantity: int
    price: float
    timestamp: datetime

# In-memory storage
transactions = []

# Add a new transaction
@app.post("/transactions")
async def add_transaction(transaction: Transaction):
    transactions.append(transaction)
    return {"message": "Transaction added successfully"}

# Get all transactions
@app.get("/transactions")
async def get_transactions():
    return {"transactions": transactions}

# Get a specific transaction by ID
@app.get("/transactions/{transaction_id}")
async def get_transaction(transaction_id: int):
    for transaction in transactions:
        if transaction.transaction_id == transaction_id:
            return transaction
    raise HTTPException(status_code=404, detail="Transaction not found")

# Get all transactions for a specific customer
@app.get("/transactions/customer/{customer_id}")
async def get_customer_transactions(customer_id: int):
    customer_transactions = [t for t in transactions if t.customer_id == customer_id]
    if not customer_transactions:
        raise HTTPException(status_code=404, detail="No transactions found for this customer")
    return {"customer_id": customer_id, "transactions": customer_transactions}

# Get all transactions for a specific product
@app.get("/transactions/product/{product_id}")
async def get_product_transactions(product_id: int):
    product_transactions = [t for t in transactions if t.product_id == product_id]
    if not product_transactions:
        raise HTTPException(status_code=404, detail="No transactions found for this product")
    return {"product_id": product_id, "transactions": product_transactions}

# Get sales analytics
@app.get("/analytics/sales")
async def get_sales_analytics():
    total_revenue = sum(t.quantity * t.price for t in transactions)
    total_transactions = len(transactions)
    average_order_value = total_revenue / total_transactions if total_transactions > 0 else 0
    return {
        "total_revenue": total_revenue,
        "total_transactions": total_transactions,
        "average_order_value": average_order_value,
    }

# Get customer analytics
@app.get("/analytics/customer/{customer_id}")
async def get_customer_analytics(customer_id: int):
    customer_transactions = [t for t in transactions if t.customer_id == customer_id]
    if not customer_transactions:
        raise HTTPException(status_code=404, detail="No transactions found for this customer")
    
    total_spend = sum(t.quantity * t.price for t in customer_transactions)
    total_orders = len(customer_transactions)
    return {
        "customer_id": customer_id,
        "total_spend": total_spend,
        "total_orders": total_orders,
    }

# Get product analytics
@app.get("/analytics/product/{product_id}")
async def get_product_analytics(product_id: int):
    product_transactions = [t for t in transactions if t.product_id == product_id]
    if not product_transactions:
        raise HTTPException(status_code=404, detail="No transactions found for this product")
    
    total_units_sold = sum(t.quantity for t in product_transactions)
    total_revenue = sum(t.quantity * t.price for t in product_transactions)
    return {
        "product_id": product_id,
        "total_units_sold": total_units_sold,
        "total_revenue": total_revenue,
    }