from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.category_repository as category_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository 

dashboard_blueprint = Blueprint("dashboard", __name__)

@dashboard_blueprint.route("/")
def dashboard_index():
     users = user_repository.select_all()
     merchants = merchant_repository.select_all()
     categories = category_repository.select_all()
     transactions = transaction_repository.select_all()
     total_value = transaction_repository.total_value()
     num_merchants = merchant_repository.num_merchants()
     num_categories = category_repository.num_categories()

     return render_template("/index.html", users=users, merchants=merchants, categories=categories, transactions=transactions, total_value=total_value, num_merchants=num_merchants, num_categories=num_categories)