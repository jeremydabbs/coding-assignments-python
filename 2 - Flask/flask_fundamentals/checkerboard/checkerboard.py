from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html", rows=8, columns=8)

@app.route('/4')
def checkerboard4():
    return render_template("index.html", rows=4, columns=8)

@app.route('/<x>/<y>')
def checkerboardxy(x,y):
    return render_template("index.html", rows=int(x), columns=int(y))




# The following if statement always has to be at the bottom
if __name__=="__main__":
    app.run(debug=True)