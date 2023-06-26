# exchange data
exchange_dict = {
    "USD": 15000,
    "EUR": 16000,
    "SGD": 12000,
    "AUD": 10000,
}

# transaction data
transaction_data = [
    {"id": "002", "currency": "AUD", "amount": 200, "amount_idr": 0},
    {"id": "007", "currency": "SGD", "amount": 450, "amount_idr": 0},
    {"id": "004", "currency": "USD", "amount": 90, "amount_idr": 0},
    {"id": "001", "currency": "USD", "amount": 100, "amount_idr": 0},
    {"id": "005", "currency": "SGD", "amount": 120, "amount_idr": 0},
    {"id": "003", "currency": "EUR", "amount": 350, "amount_idr": 0},
    {"id": "008", "currency": "USD", "amount": 20, "amount_idr": 0},
    {"id": "006", "currency": "EUR", "amount": 130, "amount_idr": 0},
]

# Update transaction data and calculate amount in IDR
for transaction in transaction_data:
    currency = transaction["currency"]
    amount = transaction["amount"]
    exchange_rate = exchange_dict.get(currency, 1)
    amount_idr = amount * exchange_rate
    transaction["amount_idr"] = amount_idr

# Print the updated transaction data
for transaction in transaction_data:
    print(transaction)

# Group and sum the total amount_idr by currency
total_amount_idr_by_currency = {}
for transaction in transaction_data:
    currency = transaction["currency"]
    amount_idr = transaction["amount_idr"]
    total_amount_idr_by_currency[currency] = total_amount_idr_by_currency.get(currency, 0) + amount_idr

# Print the total amount_idr by currency
for currency, total_amount_idr in total_amount_idr_by_currency.items():
    print(f"{currency}: {total_amount_idr}")