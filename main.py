from flask import Flask, request # importing libraries Flask: server
from datetime import datetime

app = Flask('My First Application') # initiating  a server and I give it a name.

@app.route('/')# when y

def index():
    # return 'Hello, This is my first API. This is my front of my website'#
    return """
    <h1> Arnaud Websites</h1>
    <p> My name is Arnaud</p>
    """
@app.route('/contact')

def contact_page():
    return 'contact me at flask@gmail.com or 0784337888'

@app.route('/date')
def show_date():
    date = str(datetime.now())
    return f'Today is {date}'

@app.route('/birthyear',methods = ['POST','GET'])
def calc_bithyear():
    if request.method == 'POST':# User is posting or submitting his or her information
        # return f"you declared your age as {request.form.get('birthyear')}"
        return f"""
        <form action='/birthyear' method ='POST'>
        <input type='number' name ='birthyear' placeholder ='birthday e.g e.g 2020'>
        <input type="submit" value = "submit"> 
        </form>
        you declared your age as {2022-int(request.form.get('birthyear'))}
        
        """
    elif request.method == 'GET': # User is asking for this page
        return """
        <form action='/birthyear' method ='POST'>
        <input type='number' name ='birthyear' placeholder ='birthday e.g e.g 2020'>
        <input type="submit" value = "submit"> 
        </form>
        """

if __name__ =='__main__': #
    app.run()