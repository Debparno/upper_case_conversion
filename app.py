from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', method = ['post'])
def my_form_post():
    text = request.form['u']
    processed_text = text.upper()

    return processed_text

if (__name__ == '__main__'):
    app.run()
