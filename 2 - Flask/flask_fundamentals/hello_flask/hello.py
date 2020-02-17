from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id:" + id

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name}"

@app.route('/repeat/<int:multiplier>/<message>')
def multiply_message(multiplier, message):
    return f"{message} " * (multiplier)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again."


# The following if statement always has to be at the bottom
if __name__=="__main__":
    app.run(debug=True)