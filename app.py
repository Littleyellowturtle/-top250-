from flask import Flask,render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/index')
def home():
    return render_template("index.html")
    #return index()
@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect("movie250.db")
    cur = con.cursor()
    sql = "select*from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()


    return render_template("movie.html",movies = datalist)
@app.route('/team')
def team():
    return render_template("team.html")
@app.route('/score')
def score():
    num = []
    sum = []
    con = sqlite3.connect("movie250.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        num.append(item[0])
        sum.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html",num = num,sum = sum)
@app.route('/word')
def word():
    return render_template("word.html")





if __name__ == '__main__':
    app.run()
