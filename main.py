import os

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Главная страница')


@app.route('/about-us')
def about():
    return render_template('about-us.html')

@app.route('/states')
def galery():
    return render_template('states.html')


@app.route('/weekend-1')
def weekend_1():
    return render_template('weekend_1.html')


@app.route('/weekend-2')
def weekend_2():
    return render_template('weekend_2.html')
    

@app.route('/weekend-3')
def weekend_3():
    return render_template('weekend_3.html')


@app.route('/weekend-end')
def weekend_end():
    return render_template('weekend_end.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)