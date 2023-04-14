from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository

spend_tracker_blueprint = Blueprint("spend_tracker", __name__)

@spend_tracker_blueprint.route("/home")
def all_transactions():
    transactions = transaction_repository.select_all()
    return render_template("home/index.html", all_transactions = transactions)