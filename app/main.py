from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MONGO_DBNAME'] = 'db1'
app.config['MONGO_URI'] = 'mongodb://root:root123@ds113915.mlab.com:13915/db1'

mongo = PyMongo(app)


@app.route("/")
def hello():
    listings1 = (
        {
            'title': "Wrangler shield is too OP",
            'tags': ['#tf2', '#engineer'],
            'info': 'We all know wrangler has blah blah blah s s s s s s s s s ss s s s',
            'up': 100, 
            'down': 10
        },
        {
            'title': "Wrangler shield is too OP",
            'tags': ['#tf2', '#engineer'],
            'info': 'We all know wrangler has blah blah blah s s s s s s s s s ss s s s',
            'up': 100, 
            'down': 10
        },
        {
            'title': "Wrangler shield is too OP",
            'tags': ['#tf2', '#engineer'],
            'info': 'We all know wrangler has blah blah blah s s s s s s s s s ss s s s',
            'up': 100, 
            'down': 10
        }
    )
    return render_template("main.html", listings1=listings1)


@app.route("/card")
def cards():
    return render_template("card.html")


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
