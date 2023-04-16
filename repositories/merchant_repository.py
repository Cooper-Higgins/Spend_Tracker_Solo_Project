from db.run_sql import run_sql

from models.merchant import Merchant

def create(merchant):
    sql = "INSERT INTO merchants (merchant_name, inactive) VALUES (%s, %s) RETURNING *"
    values = [merchant.merchant_name, merchant.inactive]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['merchant_name'], row['inactive'], row['id'])
        merchants.append(merchant)
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        merchant = Merchant(result['merchant_name'], result['inactive'], result['id'])
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(merchant):
    sql = "UPDATE merchants SET (merchant_name, inactive) = (%s, %s) WHERE id = %s"
    values = [merchant.merchant_name, merchant.inactive, merchant.id]
    run_sql(sql, values)