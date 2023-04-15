from db.run_sql import run_sql

from models.category import Category

def create(category):
    sql = "INSERT INTO categories (category) VALUES (%s) RETURNING *"
    values = [category.category]
    results = run_sql(sql, values)
    id = results[0]['id']
    category.id = id
    return category

def delete_all():
    sql = "DELETE FROM categories"
    run_sql(sql)
