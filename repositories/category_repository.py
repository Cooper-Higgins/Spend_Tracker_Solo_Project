from db.run_sql import run_sql

from models.category import Category

def create(category):
    sql = "INSERT INTO categories (category) VALUES (%s) RETURNING *"
    values = [category.category]
    results = run_sql(sql, values)
    id = results[0]['id']
    category.id = id
    return category

def select_all():
    categories = []

    sql = "SELECT * FROM categories"
    results = run_sql(sql)

    for row in results:
        category = Category(row['category'])
        categories.append(category)
    return categories

def select(id):
    category = None
    sql = "SELECT * FROM categories WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        category = Category(result['category'])
    return category 

def delete_all():
    sql = "DELETE FROM categories"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM categories WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(category):
    sql = "UPDATE categories SET (category) = %s WHERE id = %s"
    values = [category.category]
    run_sql(sql, values)