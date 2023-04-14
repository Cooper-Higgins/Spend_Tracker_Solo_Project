from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from models.user import User
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository

spend_tracker_blueprint = Blueprint("spend_tracker", __name__)

@spend_tracker_blueprint.route("/")
def index():
    return render_template("/index.html")

@spend_tracker_blueprint.route("/transactions/")
def transactions():
    return render_template("/transactions/index.html")

@spend_tracker_blueprint.route("/merchants/")
def merchants():
    return render_template("/merchants/index.html")

@spend_tracker_blueprint.route("/categories/")
def categories():
    return render_template("/categories/index.html")

@spend_tracker_blueprint.route("/account/")
def account():
    return render_template("/account/index.html")