from flask import Flask, render_template

app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True



# Routes
@app.route("/")
def hello():
    #listings1 =  
    return render_template("main.html", listings1={'title': 'WIP'})


@app.route("/card")
def cards():
    return render_template("card.html")


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
