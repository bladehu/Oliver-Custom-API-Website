import dictionary as dct
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from requests import HTTPError

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = "TopSecret"


class DictForm(FlaskForm):
    word = StringField("The word you want to look for", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def home():
    form = DictForm()
    if form.validate_on_submit():
        session["word"] = request.form.get("word")
        return redirect(url_for('result'))
    return render_template("index.html", form=form)


@app.route("/result")
def result():
    word = session["word"]
    try:
        dict_result = dct.request_word(word)
    except HTTPError:
        return redirect(url_for("page_not_found"))
    images = []
    for i in range(len(dict_result['definitions'])):
        images.append(dict_result['definitions'][i]['image_url'])
    length = len(dict_result['definitions'])
    return render_template("results.html", result=dict_result, img=images, len=length)


@app.route("/404")
def page_not_found():
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
