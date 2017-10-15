from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://user1:passwd123@localhost/gamesuggest'

db = SQLAlchemy(app)

# Schemas


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poster = db.Column(db.String(80), unique=True, nullable=False)
    post_title = db.Column
    up = db.Column(db.Integer)
    down = db.Column(db.Integer)

    

    def __repr__(self):
        return '<User %r>' % self.


# Routes
@app.route("/")
def hello():
    #listings1 =  
    return render_template("main.html", listings1=listings1)


@app.route("/card")
def cards():
    return render_template("card.html")


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
