from db.run_sql import run_sql

from models.merchant import Merchant

def create(merchant):
    sql = "INSERT INTO merchants (merchant) VALUES (%s) RETURNING *"
    values = [merchant.merchant]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)
