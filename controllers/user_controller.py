from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/account/")
def account_index():
    users = user_repository.select_all()
    return render_template("/account/index.html", users=users)

@users_blueprint.route("/account/<id>", methods=['POST'])
def update_account(id):
    budget = request.form['budget']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    city = request.form['city']
    email = request.form['email']
    user = User(first_name, last_name, dob, city, email, budget, id)
    user_repository.update(user)
    return redirect('/account')