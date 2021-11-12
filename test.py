from flask import Flask
app = Flask(__name__)




@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

#routes
@app.route('/information')
def info():
    return '<h1>Puppies are cute!</h1>'

# dynamic routes
@app.route('/information/<name>')
def slug(name):
    return '<h1>User: {}</h1>'.format(name)

#debug
if __name__=='__main__':
    app.run(debug=True)