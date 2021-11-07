from myapp import myapp_obj
from myapp.forms import TopCities
from flask import render_template, flash, redirect

from myapp import db
from myapp.models import City

@myapp_obj.route("/")
def begin():
    return redirect("/home")

@myapp_obj.route("/home", methods=["GET", "POST"])
def home():
    form = TopCities()
    if form.validate_on_submit():
        new_city = City(name=form.city_name.data, rank=form.city_rank.data)
        db.session.add(new_city)
        db.session.commit()
    posts = [{}]
    return render_template('home.html', title = 'Top Cities', form = form, name = 'Phuc', posts = posts)
