from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def info():
    return '2020112757 컴퓨터학부 글로벌소프트웨어학과 김유진'

@app.route('/mushroom/')
def mushroom():
    return render_template('index2.html', my_img='mushroom.jpeg')

if __name__ == "__main__":
    app.run(debug=True)