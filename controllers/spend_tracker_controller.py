from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from models.user import User
from models.category import Category
from models.merchant import Merchant
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository
import repositories.category_repository as category_repository
import repositories.merchant_repository as merchant_repository

spend_tracker_blueprint = Blueprint("spend_tracker", __name__)

### - GET / Display Routes - ###
@spend_tracker_blueprint.route("/")
def index():
    return render_template("/index.html")

@spend_tracker_blueprint.route("/categories/")
def categories_index():
     categories = category_repository.select_all() 
     return render_template("/categories/index.html", categories=categories)

@spend_tracker_blueprint.route("/merchants/")
def merchants_index():
    merchants = merchant_repository.select_all() 
    return render_template("/merchants/index.html", merchants=merchants)

@spend_tracker_blueprint.route("/transactions/")
def transactions_index():
    transactions = transaction_repository.select_all() 
    return render_template("/transactions/index.html", transactions=transactions)

@spend_tracker_blueprint.route("/account/")
def account_index():
    users = user_repository.select_all()
    return render_template("/account/index.html", users=users)


### - POST / Create Routes - ###
@spend_tracker_blueprint.route("/categories", methods=['POST'])
def create_category():
    category_name = request.form['category_name']
    inactive = request.form['inactive']
    category = Category(category_name, inactive)
    category_repository.create(category)
    return redirect('/categories')

@spend_tracker_blueprint.route('/merchants', methods=['POST'])
def create_merchant():
    merchant_name = request.form['merchant_name']
    inactive = request.form['inactive']
    merchant = Merchant(merchant_name, inactive)
    merchant_repository.create(merchant)
    return redirect('/merchants')

# @spend_tracker_blueprint.route("/transactions", methods=['POST'])
# def create_transaction():
#     tx_value= request.form['tx_value']
#     merchant = request.form['merchant']
#     category = request.form['category']
#     time_stamp = request.form['time_stamp']
    
#     # Want this to take in 'logged in' user by default, not sure what to pass - don't want to have to have a form to take user id?
#     user = user_repository.select()
#     transaction = Transaction(tx_value, merchant, category, time_stamp, user)
#     transaction_repository.create(transaction)
#     return redirect('/transactions')


### - GET / Show Routes - ###
@spend_tracker_blueprint.route("/categories/<id>", methods=['GET'])
def show_category(id):
    category = category_repository.select(id)
    return render_template('categories/update.html', category=category)

@spend_tracker_blueprint.route("/merchants/<id>", methods=['GET'])
def show_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/update.html', merchant=merchant)

@spend_tracker_blueprint.route("/transactions/<id>", methods=['GET'])
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template('transactions/update.html', transaction=transaction)


# UPDATE
# PUT '/categories/<id>'
@spend_tracker_blueprint.route("/categories/<id>", methods=['POST'])
def update_category(id):
    category_name = request.form['category_name']
    inactive = request.form['inactive']
    category = Category(category_name, inactive, id)
    category_repository.update(category)
    return redirect('/categories')

@spend_tracker_blueprint.route("/merchants/<id>", methods=['POST'])
def update_merchant(id):
    merchant_name = request.form['merchant_name']
    inactive = request.form['inactive']
    merchant = Merchant(merchant_name, inactive, id)
    merchant_repository.update(merchant)
    return redirect('/merchants')


### - POST / Delete Routes - ###
@spend_tracker_blueprint.route("/categories/<id>/delete", methods=['POST'])
def delete_category(id):
    category_repository.delete(id)
    return redirect('/categories')

@spend_tracker_blueprint.route("/merchants/<merchant>/delete", methods=['POST'])
def delete_merchant(merchant):
    merchant_repository.delete(merchant)
    return redirect('/merchants')

@spend_tracker_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')