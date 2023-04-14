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
