from flask import Flask
from flask import render_template
app = Flask(__name__)   


@app.route('/')
def index():
        return '<h1> Witaj na stronie SP23 <br> Let\'s medival </h1'

@app.route('/kot')
def kot():
    return '<img src="https://i.ytimg.com/vi/iluoNqC-PhA/hqdefault.jpg">'


@app.route('/pies')
def pies():
    return '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4uK53FmaLGHTPiCChjG9s70jLeOCq5rxxPGXn9n7owINxfcya">'

@app.route('/kon')
def kon():
    return '<img src="http://bi.gazeta.pl/im/33/41/16/z23338291V,Kon.jpg">'


@app.route('/zyrafa')
def zyrafa():
    return '<img src="">'


@app.route('/golab')
def golab():
    return '<img src="https://janinadaily.com/wp-content/uploads/2016/07/13557692_1791276351108190_4843299797269144502_n.jpg">'



@app.route('/user/name')
def kot(name):
    return render_template("user.html", imie=name)











