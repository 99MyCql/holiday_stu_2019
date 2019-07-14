from flask import Flask
from flask import request


app = Flask(__name__)

def do_the_login():
	return "do_the_login"

def show_the_login_form():
	return "show_the_login_form"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #do_the_login()
        return "do_the_login"
    else:
        #show_the_login_form()  # error
        return "show_the_login_form"


if __name__ == '__main__':
    app.run()