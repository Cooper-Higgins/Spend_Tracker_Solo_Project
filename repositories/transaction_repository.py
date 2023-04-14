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

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        user = user_repository.select(result['user_id'])
        transaction = Transaction(result['tx_value'], result['merchant'], result['category'], result['time_stamp'], user, result['id'] )
    return transaction

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)