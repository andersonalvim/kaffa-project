from flask import *
import scripts
import pyrebase, requests

config = {
    "apiKey": "AIzaSyDRsKltjDQHVUrspqP_NbhZdc4xk2PszQA",
    "authDomain": "kaffaproject.firebaseapp.com",
    "databaseURL": "https://kaffaproject-default-rtdb.firebaseio.com",
    "projectId": "kaffaproject",
    "storageBucket": "kaffaproject.appspot.com",
    "messagingSenderId": "309346705957",
    "appId": "1:309346705957:web:6194b3ffced5d72e3915cc",
    "measurementId": "G-4GJ1WD2VWJ"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/task1.html', methods=['GET', 'POST'])
def basic1():
    if request.method == 'POST':
        if request.form.get('submit', False) == 'submit':
            cnpj = request.form['name']
            result = scripts.validaCnpj(cnpj)
            return render_template('task1.html', x=result)
    return render_template('task1.html')

@app.route('/task2.html', methods=['GET', 'POST'])
def basic2():
    if request.method == 'POST':
        if request.form.get('submit', False) == 'submit':
            cnpj = request.form['name']
            result = scripts.validaCnpj1(cnpj)
            return render_template('task2.html', x=result)
    return render_template('task2.html')

@app.route('/task3.html', methods=['GET','POST'])
def basic3():
    if request.method == 'POST':
        if request.form.get('submit', False) == 'submit':
            x1 = request.form['coordx1']
            y1 = request.form['coordy1']
            width1 = request.form['width1']
            height1 = request.form['height1']
            x2 = request.form['coordx2']
            y2 = request.form['coordy2']
            width2 = request.form['width2']
            height2 = request.form['height2']

            result = scripts.checkAndComputeIntersectionTwoRectangles(x1,y1,width1,height1,x2,y2,width2,height2)

            if result[0] == False:
                return render_template('task3.html', x='There is no intersection between this rectangles')
            else:
                return render_template('task3.html', x='There is intersection between this rectangles')
    return render_template('task3.html')

@app.route('/task4.html', methods=['GET','POST'])
def basic4():
    if request.method == 'POST':
        if request.form.get('submit', False) == 'submit':
            x1 = request.form['coordx1']
            y1 = request.form['coordy1']
            width1 = request.form['width1']
            height1 = request.form['height1']
            x2 = request.form['coordx2']
            y2 = request.form['coordy2']
            width2 = request.form['width2']
            height2 = request.form['height2']

            result = scripts.checkAndComputeIntersectionTwoRectangles(x1,y1,width1,height1,x2,y2,width2,height2)

            if result[0] == False:
                return render_template('task4.html', x='There is no intersection between this rectangles')
            else:
                return render_template('task4.html', x=result[1])
    return render_template('task4.html')

@app.route("/task5.html", methods=["GET","POST"])
def basic5():
    if request.method == 'POST':
        if request.form.get('submit', False) == 'add':
            name = request.form['name']
            db.child("todo").push(name)
            todo = db.child("todo").get()
            to = todo.val()
            return render_template('task5.html', t=to.values())
        elif request.form.get('submit', False) == 'delete':
            db.child("todo").remove()
        return render_template('task5.html')
    return render_template("task5.html")

@app.route("/task6.html", methods=["GET","POST"])
def basic6():
    request = requests.get('http://worldclockapi.com/api/json/utc/now')
    address_data = request.json()
    currentTime = address_data['currentDateTime']
    currentTime = currentTime[11:16]
    currentDate = address_data['currentDateTime']
    currentDate = currentDate[8:10]+"/"+currentDate[5:7]+"/"+currentDate[0:4]
    dayOfTheWeek = address_data['dayOfTheWeek']

    if currentTime:
        return render_template("task6.html", x=currentTime, y=dayOfTheWeek, z=currentDate)
    return render_template("task6.html")

@app.route("/task7.html", methods=["GET","POST"])
def basic7():
    request = requests.get('http://worldclockapi.com/api/json/utc/now')
    address_data = request.json()
    if address_data:
        return render_template('task7.html', x=address_data)
    return render_template("task7.html")

@app.route("/task8.html", methods=["GET","POST"])
def basic8():
    return render_template("task8.html")

@app.route("/task9.html", methods=["GET","POST"])
def basic9():
    return render_template("task9.html")

if __name__ == '__main__':
    app.run(debug=True)