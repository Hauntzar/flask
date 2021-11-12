from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    some_variable="Jose"
    return render_template('basic.html',myVariable=some_variable)

if __name__=='__main__':
    app.run(debug=True)