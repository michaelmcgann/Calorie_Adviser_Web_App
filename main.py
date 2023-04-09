from flask import Flask, render_template, request, url_for
from calories import Calorie
from temperature import Temperature

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calories', methods=['GET', 'POST'])
def calories_form_page():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        city = request.form['city']
        country = request.form['country']
        temperature = Temperature(country=country, city=city).get()

        calories = Calorie(age=age, weight=weight, height=height, temperature=temperature).calculate()

        return render_template('calories_form_page.html', result=True, calories=calories)
    else:
        return render_template('calories_form_page.html')


if __name__ == '__main__':
    app.run(debug=True)




