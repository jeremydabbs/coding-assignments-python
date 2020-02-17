from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# secret key removed

@app.route('/')
def index():
    if not 'x' in session:
        session['x'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def get_gold():
    print("GOLD!!!")
    add_gold = 0
    import random
    if request.form['building'] == 'farm':
        add_gold = random.randint(10, 20)
        session['x'] += add_gold
        return redirect('/')
    if request.form['building'] == 'cave':
        add_gold = random.randint(5, 10)
        session['x'] += add_gold
        return redirect("/")
    if request.form['building'] == 'house':
        add_gold = random.randint(2, 5)
        session['x'] += add_gold
        return redirect("/")
    if request.form['building'] == 'casino':
        add_gold = random.randint(-50, 50)
        session['x'] += add_gold
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)