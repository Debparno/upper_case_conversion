from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def my_form_post():
    text = request.form['u']
    processed_text = text.upper()
    return processed_text

@app.route('/')
def my_form():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
