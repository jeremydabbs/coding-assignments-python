from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", times=3, color="blue")

@app.route('/play/<x>')
def playx(x):
    return render_template("index.html", times=int(x), color="blue")

@app.route('/play/<x>/<color>')
def playxcolor(x, color):
    return render_template("index.html", times=int(x), color=(color))



# The following if statement always has to be at the bottom
if __name__=="__main__":
    app.run(debug=True)