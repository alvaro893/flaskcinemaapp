"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app
from services.finnkino import FinnKinoXML

finnkino = FinnKinoXML()

@app.route('/')
def main_page():
    months = ["January", "February", "March", "April"]
    my_dict = {"hello":"it is a greeting", 'mug':"it is a thing to hold coffee", "plate":"it is an object that contens food"}
    return render_template('mainpage.html', months = months, my_dict = my_dict)

@app.route('/movies')
def movies_page():
    movies = finnkino.get_movies_for_area(area_num)
    return render_template('maincinemapage.html', movies = movies)
    
@app.route('/movies/<area>')
def movies(area):
    movies = finnkino.get_movies_for_area(area)
    areas = finnkino.get_areas()
    return render_template('maincinemapage.html', movies = movies, areas = areas)

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
