from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# secret key removed

@app.route('/')
def index():
    if not 'visits' in session:
        #print("key 'visits' does NOT exist")
        session['visits'] = 1
    else:
        #print("key 'visits' exists!")
        session['visits'] += 1

    return render_template("index.html")

@app.route('/destroy-session')
def destroy():
    session['visits'] = 0
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)