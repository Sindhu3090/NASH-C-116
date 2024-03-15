from flask import Flask, render_template

app = Flask(__name__)

#in the function return render_template(‘index.html’)
@app.route("/")

def first_webpage():
    #Create a variable
    name = 'Nashwan Ridwan'
    # Pass the variable in the template
    return render_template('SA_index.html', index_variable = name)

app.run(debug=True)