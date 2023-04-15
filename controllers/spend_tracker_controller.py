from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from models.user import User
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository

spend_tracker_blueprint = Blueprint("spend_tracker", __name__)


### - GET Routes - ###

@spend_tracker_blueprint.route("/")
def index():
    return render_template("/index.html")


@spend_tracker_blueprint.route("/transactions/")
def transactions_index():
    transactions = transaction_repository.select_all() 
    return render_template("/transactions/index.html", transactions=transactions)


@spend_tracker_blueprint.route("/merchants/")
def merchants_index():
    return render_template("/merchants/index.html")


@spend_tracker_blueprint.route("/categories/")
def categories_index():
    return render_template("/categories/index.html")


@spend_tracker_blueprint.route("/account/")
def account_index():
    return render_template("/account/index.html")


### - POST / Create Routes - ###

@spend_tracker_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    tx_value= request.form['tx_value']
    merchant = request.form['merchant']
    category = request.form['category']
    time_stamp = request.form['time_stamp']
    
    # Want this to take in 'logged in' user by default, not sure what to pass - don't want to have to have a form to take user id?
    user = user_repository.select()
    transaction = Transaction(tx_value, merchant, category, time_stamp, user)
    transaction_repository.create(transaction)
    return redirect('/transactions')

@spend_tracker_blueprint.route('/merchants', methods=['POST'])
def create_merchant():
    return redirect('/merchants')

@spend_tracker_blueprint.route("/categories", methods=['POST'])
def create_category():
    return redirect('/categories')
