from cinema import app
from flask import render_template, request


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/movies')
def movies():
    return render_template('movies.html')


if __name__ == '__main__':
    app.run(debug=True)
