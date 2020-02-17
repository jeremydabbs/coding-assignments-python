from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {str(int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple']))} fruits")
    strawberry_quantity = request.form['strawberry']
    raspberry_quantity = request.form['raspberry']
    apple_quantity = request.form['apple']
    first_name_from_form = request.form['first_name']
    last_name_from_form = request.form['last_name']
    student_id_from_form = request.form['student_id']
    return render_template("checkout.html", strawberry_order=strawberry_quantity, raspberry_order=raspberry_quantity, apple_order=apple_quantity,first_name_submitted=first_name_from_form, last_name_submitted=last_name_from_form, student_id_submitted=student_id_from_form)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    