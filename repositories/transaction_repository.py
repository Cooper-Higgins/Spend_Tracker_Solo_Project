from db.run_sql import run_sql

from models.transaction import Transaction
from models.user import User

def create(transaction):
    sql = "INSERT INTO transactions (tx_value, merchant, category, time_stamp, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [transaction.tx_value, transaction.merchant, transaction.category, transaction.time_stamp, transaction.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction
