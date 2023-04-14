from flask import Flask, render_template

from controllers.spend_tracker_controller import spend_tracker_blueprint

app = Flask(__name__)

app.register_blueprint(spend_tracker_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
