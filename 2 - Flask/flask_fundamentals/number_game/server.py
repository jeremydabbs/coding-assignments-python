from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# secret key removed

@app.route('/')
def index():
    import random # import the random module
    if not 'x' in session:
        session['x'] = random.randint(1, 100) # random number between 1-100
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def compare():
    print("Guess has been submitted")
    if session['x'] == int(request.form['guess']):
        session['guess_status'] = 'correct'
        return redirect('/')
    if (session['x']) > int(request.form['guess']):
        session['guess_status'] = 'low'
        return redirect("/")
    if session['x'] < int(request.form['guess']):
        session['guess_status'] = 'high'
        return redirect("/")

@app.route('/reset', methods=['POST'])
def reset():
    import random
    session['x'] = random.randint(1, 100)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)