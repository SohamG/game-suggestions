from flask import Flask, render_template

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'db1'
app.config['MONGO_URI'] = 'mongodb://root:root123@ds113915.mlab.com:13915/db1'

mongo = PyMongo(app)

@app.route("/")
def hello():
    suggestions = 
    return render_template("main.html")

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
