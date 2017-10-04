from flask import Flask, request, redirect, render_template,render_template_string

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template('welcome.html', username=username)


@app.route("/signup", methods=['POST','GET'])
def index():
    user_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if request.method == 'GET':
        username = ""
        email = ""
        return render_template('signup.html', username=username, email=email)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

#First doing just username verification
        if username == "":
            user_error = "Please enter a username."
            

        if (len(username) < 3) or (len(username) > 20):
            user_error = "Username must be between 3 and 20 characters long."
            

        space_test = username
        for i in list(space_test):
            if i == " ":
                user_error = "Username cannot contain a space."
                

# Password section

        if password == "":
            password_error = "Please enter a password."
            

        if (len(password) < 3) or (len(password) > 20):
            password_error = "Password must be between 3 and 20 characters long."
            

        space_test = password
        for j in list(space_test):
            if j == " ":
                password_error = "password cannot contain a space."
                


# Password validation section 

        if verify == None:
            verify_error = "Please enter a password."
            

        if (len(verify) < 3) or (len(verify) > 20):
            verify_error = "Password must be between 3 and 20 characters long."
            

        space_test = verify
        for k in list(space_test):
            if k == " ":
                verify_error = "Password cannot contain a space."
               

# verify password = verify

        if password != verify:
            password_error = "The Passwords "
            verify_error = "do not match."
        

# email checking - only check if there is something in the email field
# Still allows weird things like "@.cats"  :(
        email_check = ""

        if email != "":

            if (len(email) < 3) or (len(email) > 20):
                email_error = "Password must be between 3 and 20 characters long."
                email_check = "fail"
            

            space_test = email
            for k in list(space_test):
                if k == " ":
                    email_error = "Password cannot contain a space."
                    email_check = "fail"

# only one @ symbol
        
            dot_count = 0
            at_count = 0
            symbol_test = email
            for k in list(symbol_test):
                if k == "@":
                    at_count = at_count + 1
            
                if k == ".":
                    dot_count = dot_count + 1
        
            if (dot_count != 1) or (at_count != 1):
                    email_error = "Please enter a valid email address with one '@' and only one '.'."
                    email_check = "fail"



#If any verification fails

        if (verify_error != "") or (password_error != "") or (user_error != "") or (email_check == "fail"):
            return render_template("signup.html",
                                    username=username,
                                    verify_error=verify_error,
                                    password_error=password_error, 
                                    user_error=user_error, 
                                    email_error=email_error)

        


#This is the working part
        return render_template("welcome.html",username=username)
        




app.run()