from flask import Flask, request, redirect, render_template,render_template_string

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template('welcome.html', username=username)


@app.route("/signup", methods=['POST','GET'])
def index():
    username = request.args.get("username")

    if request.method == 'GET':
        username = ""
        return render_template('signup.html', username=username)

    if request.method == 'POST':
        username = request.form['username']
#        password = request.form['password']
#        verify = request.form['verify']
#        email = request.form['email']

#First doing just username verification
        if username == "":
            error = "Please enter a username."
            return render_template("signup.html",username=username, error=error)

        if (len(username) < 3) or (len(username) > 20):
            error = "Username must be between 3 and 20 characters long."
            return render_template("signup.html",username=username, error=error)

        space_test = username
        for i in list(space_test):
            if i == " ":
                error = "Username cannot contain a space."
                return render_template("signup.html",username=username, error=error)

        


#This is the working part
        return render_template("welcome.html",username=username)
        




app.run()