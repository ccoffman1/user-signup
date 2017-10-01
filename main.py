from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/welcome")
def welcome():
    
    return render_template('welcome.html')


@app.route("/signup", methods=['POST','GET'])
def index():

    if request.method == 'GET':
        return render_template('signup.html')

    if request.method == 'POST':
        username = request.form['username']
#        password = request.form['password']
#        verify = request.form['verify']
#        email = request.form['email']

#First doing just username verification
        if username == "":
            error = "Please enter a username."
            return redirect("/signup")

        if (len(username) < 3) or (len(username) > 20):
            error = "Username must be between 3 and 20 characters long."
            return redirect("/signup")

        space_test = username
        for i in list(space_test):
            if i == " ":
                error = "Username cannot contain a space."
                return redirect("/signup")

        



        return redirect("/welcome")
        




app.run()