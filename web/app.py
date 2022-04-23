import flask
from flask import Flask, request, render_template

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route('/run', methods=['POST', 'GET'])
def run():
    a = request.form.get('number')
    if a == '1' or a == '2' or a == '4':
        return render_template("wrong.html")
    else:
        return render_template("correct.html")


@app.route("/more")
def information_page():
    return render_template("information.html")\



@app.route("/correct")
def correct_answer_page():
    return render_template("correct.html")\



@app.route("/wrong")
def wrong_answer_page():
    return render_template("wrong.html")


if __name__ == '__main__':
   app.run(debug = True)