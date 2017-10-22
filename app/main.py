from flask import Flask, render_template
import redis

app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

r = redis.Redis(host='172.17.0.2', port=6379)

if r is None:
    print("Redis aint workin yo")


'''
Format for Posts hash -  

Poster(str)    Title(str)   Tags(list(str))     Info(str)   Up(int)     Down(int)  

'''


# Routes
@app.route("/")
def hello():
    #listings1 =  
    # return render_template("main.html", listings1={'title': 'WIP'})
    return render_template('landing.html')


@app.route("/card")
def cards():
    return render_template("card.html")


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
