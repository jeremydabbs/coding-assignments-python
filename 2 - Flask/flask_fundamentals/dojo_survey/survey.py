from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
        print("Got Post Info")
        print(request.form)
        name_from_form = request.form['username']
        dojo_from_form = request.form['dojo_location']
        fave_lang_from_form = request.form['favorite_language']
        comment_from_form = request.form['comment']
        return render_template("result.html", name_submitted=name_from_form, dojo_submitted=dojo_from_form, fave_lang_submitted=fave_lang_from_form, comment_submitted=comment_from_form)



if __name__ == "__main__":
    app.run(debug=True)