from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True






@app.route("/signup")
def index():
    




app.run()