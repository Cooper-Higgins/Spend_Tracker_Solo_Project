from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.category_repository as category_repository
import repositories.merchant_repository as merchant_repository
import repositories.user_repository as user_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions/")
def transactions_index():
    transactions = transaction_repository.select_all()
    total_value = transaction_repository.total_value()
    merchants = merchant_repository.select_all()
    categories = category_repository.select_all()
    users = user_repository.select_all()
    return render_template("/transactions/index.html", transactions=transactions, total_value=total_value, merchants=merchants, categories=categories, users=users)

@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    tx_value = request.form['tx_value']
    merchant_name = request.form['merchant_name']
    category_name = request.form['category_name']
    time_stamp = request.form['time_stamp']
    user_id = request.form['user_id']
    user        = user_repository.select(user_id)
    transaction = Transaction(tx_value, merchant_name, category_name, time_stamp, user)
    transaction_repository.create(transaction)
    return redirect('/transactions')

@transactions_blueprint.route("/transactions/<id>", methods=['GET'])
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template('transactions/update.html', transaction=transaction)

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')