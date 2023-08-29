from flask_app import app
from flask import render_template, request, redirect, session, flash
import pprint
from flask_app.models.user_model import User
from flask_app.models.car_model import Car
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#RENDER ADD CAR PAGE
@app.route("/new")
def index_car():
    data = {"user_id":session['user_id']}
    amounts = ["4000", "5000", "6000", "7000", "8000", "9000", "10,000"]
    years = ["1990", "1995", "1998", "2000", "2005"]
    user = User.get_user_by_id(data)
    return render_template("new.html", amounts = amounts, years = years, user=user)

#RENDER EDIT CAR PAGE
@app.route("/edit/<int:id>")
def index_edit(id):
    car = Car.get_car_by_id({"id":id})
    return render_template("edit.html", car=car)

#RENDER SHOW CAR PAGE
@app.route("/show/<int:id>")
def index_show(id):
    car = Car.get_car_by_id({"id":id})
    data={"id":car['user_id']}
    seller = User.get_user_by_id(data)
    return render_template("show.html", car=car, seller=seller)



#SAVE CAR ROUTE
@app.route("/save/new", methods=['POST'])
def car_save():
    if not Car.validation(request.form):
        return redirect("/new")
    data = {
        "price":request.form['price'],
        "model":request.form['model'],
        "make":request.form['make'],
        "year":request.form['year'],
        "description":request.form['description'],
        "user_id": session['user_id']
    }
    print("FUCK")
    pprint.pprint(session['user_id'])
    Car.car_save(data)
    return redirect("/welcome")


#EDIT CAR ROUTE
@app.route("/edit", methods=['POST'])
def edit():
    if not Car.validation(request.form):
        return redirect(f"/edit/{request.form['id']}")
    data = {
        "price":request.form['price'],
        "model":request.form['model'],
        "make":request.form['make'],
        "year":request.form['year'],
        "description":request.form['description'],
        "id": request.form['id']
    }
    Car.update_car(data)
    return redirect("/welcome")

#DELETE CAR ROUTE
@app.route("/delete/<int:id>")
def delete(id):
    data={"id":id}
    Car.delete(data)
    pprint.pprint("FUCK")
    return redirect("/welcome")