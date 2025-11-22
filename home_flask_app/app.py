from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = int(request.form['age'])

        return render_template('index.html', submitted=True,
                               name=name, city=city, hobby=hobby, age=age)

    return render_template('index.html', submitted=False)


if __name__ == '__main__':
    app.run(debug=True)