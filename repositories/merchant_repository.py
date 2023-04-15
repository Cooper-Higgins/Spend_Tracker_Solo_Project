from db.run_sql import run_sql

from models.merchant import Merchant

def create(merchant):
    sql = "INSERT INTO merchants (merchant) VALUES (%s) RETURNING *"
    values = [merchant.merchant]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['merchant'])
        merchants.append(merchant)
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        merchant = Merchant(result['merchant'])
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(merchant):
    sql = "UPDATE merchants SET (merchant) = %s WHERE id = %s"
    values = [merchant.merchant]
    run_sql(sql, values)