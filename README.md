# FastAPI Data Analytics API
A simple FastAPI backend for storing and analyzing transaction data.

## Endpoints
1. Add a Transaction
   - Method: POST
   - URL: /transactions
   - Body (JSON):
   - json
   - Copy
{
  "transaction_id": 1,
  "customer_id": 101,
  "product_id": 201,
  "quantity": 2,
  "price": 25.99,
  "timestamp": "2023-10-01T12:34:56"
}

2. Get All Transactions
   - Method: GET
   - URL: /transactions

3. Get Transactions for a Customer
   - Method: GET
   - URL: /transactions/customer/{customer_id}

4. Get Transactions for a Product
   - Method: GET
   - URL: /transactions/product/{product_id}

5. Get Sales Analytics
  - Method: GET
  - URL: /analytics/sales

6. Get Customer Analytics
   - Method: GET
   - URL: /analytics/customer/{customer_id}

7. Get Product Analytics
   - Method: GET
   - URL: /analytics/product/{product_id}
