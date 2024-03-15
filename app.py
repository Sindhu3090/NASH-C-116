#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

def first_flask():
    return 'Nashwan'


@app.route("/flask2")

def second_flask():
    return 'Ridwan'

app.run(debug=True)