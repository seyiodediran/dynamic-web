from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template('home.html', title="Home")


@app.route("/about us")
def about_us():
    return render_template('about us.html', title="About Us")


@app.route("/services")
def services():
    return render_template('services.html', title="Services")


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/example'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run(host="0.0.0.0", port=int(7096), debug=True)
