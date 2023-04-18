from flask import Flask, render_template

from controllers.categories_controller import categories_blueprint
from controllers.merchants_controller import merchants_blueprint
from controllers.transactions_controller import transactions_blueprint
from controllers.users_controller import users_blueprint
from controllers.dashboard_controller import dashboard_blueprint

app = Flask(__name__)

app.register_blueprint(categories_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(transactions_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(dashboard_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
