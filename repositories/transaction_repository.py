from db.run_sql import run_sql

from models.transaction import Transaction
from models.user import User
import repositories.user_repository as user_repository

def create(transaction):
    sql = "INSERT INTO transactions (tx_value, merchant, category, time_stamp, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [transaction.tx_value, transaction.merchant, transaction.category, transaction.time_stamp, transaction.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        transaction = Transaction(row['tx_value'], row['merchant'], row['category'], row['time_stamp'], user, row['id'] )
        transactions.append(transaction)
    return transactions