from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as book_repository
import repositories.user_repository as author_repository

books_blueprint = Blueprint("spend_tracker", __name__)