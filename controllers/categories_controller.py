from flask import render_template, request, redirect
from flask import Blueprint
from models.category import Category
import repositories.category_repository as category_repository

categories_blueprint = Blueprint("categories", __name__)

@categories_blueprint.route("/categories/")
def categories_index():
     categories = category_repository.select_all() 
     return render_template("/categories/index.html", categories=categories)

@categories_blueprint.route("/categories", methods=['POST'])
def create_category():
    category_name = request.form['category_name']
    inactive = request.form['inactive']
    category = Category(category_name, inactive)
    category_repository.create(category)
    return redirect('/categories')

@categories_blueprint.route("/categories/<id>", methods=['GET'])
def show_category(id):
    category = category_repository.select(id)
    return render_template('categories/update.html', category=category)

@categories_blueprint.route("/categories/<id>", methods=['POST'])
def update_category(id):
    category_name = request.form['category_name']
    inactive = request.form['inactive']
    category = Category(category_name, inactive, id)
    category_repository.update(category)
    return redirect('/categories')

@categories_blueprint.route("/categories/<id>/delete", methods=['POST'])
def delete_category(id):
    category_repository.delete(id)
    return redirect('/categories')