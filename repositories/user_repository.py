from db.run_sql import run_sql

from models.user import User
from models.transaction import Transaction

def create(user):
    sql = "INSERT INTO users (first_name, last_name, dob, city, email, budget) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [user.first_name, user.last_name, user.dob, user.city, user.email, user.budget]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['first_name'], row['last_name'], row['dob'], row['city'], row['email'], row['budget'], row['id'] )
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        user = User(result['first_name'], result['last_name'], result['dob'], result['city'], result['email'], result ['budget'], result['id'] )
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(user):
    sql = "UPDATE users SET (first_name, last_name, dob, city, email, budget) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [user.first_name, user.last_name, user.dob, user.city, user.email, user.budget, user.id]
    run_sql(sql, values)

def transactions(user):
    transactions = []

    sql = "SELECT * FROM transactions WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        transaction = Transaction(row['tx_value'], row['merchant_name'], row['category_name'], row['time_stamp'], row['user_id'], row['id'])
        transactions.append(transaction)
    return transactions