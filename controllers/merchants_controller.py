from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants/")
def merchants_index():
    merchants = merchant_repository.select_all() 
    return render_template("/merchants/index.html", merchants=merchants)

@merchants_blueprint.route('/merchants', methods=['POST'])
def create_merchant():
    merchant_name = request.form['merchant_name']
    inactive = request.form['inactive']
    merchant = Merchant(merchant_name, inactive)
    merchant_repository.create(merchant)
    return redirect('/merchants')

@merchants_blueprint.route("/merchants/<id>", methods=['GET'])
def show_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/update.html', merchant=merchant)

@merchants_blueprint.route("/merchants/<id>", methods=['POST'])
def update_merchant(id):
    merchant_name = request.form['merchant_name']
    inactive = request.form['inactive']
    merchant = Merchant(merchant_name, inactive, id)
    merchant_repository.update(merchant)
    return redirect('/merchants')

@merchants_blueprint.route("/merchants/<merchant>/delete", methods=['POST'])
def delete_merchant(merchant):
    merchant_repository.delete(merchant)
    return redirect('/merchants')