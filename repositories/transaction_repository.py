from db.run_sql import run_sql

from models.transaction import Transaction
import repositories.user_repository as user_repository

def create(transaction):
    sql = "INSERT INTO transactions (tx_value, merchant_name, category_name, time_stamp, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [transaction.tx_value, transaction.merchant_name, transaction.category_name, transaction.time_stamp, transaction.user.id]
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
        transaction = Transaction(row['tx_value'], row['merchant_name'], row['category_name'], row['time_stamp'], user, row['id'] )
        transactions.append(transaction)
    return transactions

def select_tx_by_id(id):
    transaction = None

    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        user = user_repository.select(result['user_id'])
        transaction = Transaction(result['tx_value'], result['merchant_name'], result['category_name'], result['time_stamp'], user, result['id'] )
    return transaction

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET (tx_value, merchant_name, category_name, time_stamp, user_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [transaction.tx_value, transaction.merchant_name, transaction.category_name, transaction.time_stamp, transaction.user.id, transaction.id]
    print(values)
    run_sql(sql, values)

# Need to find a way to call this in transactions/index.html 
def total_value():
    sql = "SELECT SUM(tx_value) FROM transactions"
    results = run_sql(sql)
    return results