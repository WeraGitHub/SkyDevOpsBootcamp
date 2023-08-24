from flask import render_template
from application import app


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/hobbies/<firstname>', methods=['GET', 'POST'])
def hobbies():
    group_hobbies = ['Swimming, Gym, Football']
    return render_template('home.html', name=firstname, hobbies_list=group_hobbies)


@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html', title="About")


@app.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html', title="Contact!!!")
