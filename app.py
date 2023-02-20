from flask import Flask, render_template, request, url_for
from faker import Faker
import requests
import csv

app = Flask(__name__)
fake = Faker()


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/requirements/")
def requirements():
    with open('requirements.txt', 'r') as file:
        content = file.read()
        return render_template("requirements.html", text=content.split('\n')[:-1])


@app.route("/generate-users/", methods=['GET'])
def generate_users():
    count = request.args.get('count', default='100', type=int)
    my_list = []
    for i in range(int(count)):
        user_name = fake.name()
        user_email = fake.ascii_free_email()
        user_info = 'name: ' + user_name + ' email: ' + user_email
        my_list.append(user_info)
    return render_template("generate_users.html", list_users=my_list)


@app.route("/mean/")
def mean():
    with open('hw.csv', 'r') as file:
        data = list(csv.reader(file, delimiter=','))
    height = list(float(row[1]) for row in data[1:] if row)
    weight = list(float(row[2]) for row in data[1:] if row)
    mean_height_cm = (sum(height)/len(height))*2.506
    mean_weight_kg = (sum(weight)/len(weight))/2.205
    return render_template("mean.html", mhc=mean_height_cm, mwk=mean_weight_kg)


@app.route("/space/")
def space():
    r = requests.get(' http://api.open-notify.org/astros.json')
    list_of_astro = []
    sum_of_astro = r.json()['number']
    for astro in range(len(r.json()['people'])):
        list_of_astro.append(r.json()['people'][astro]['name'])
    return render_template("space.html", list_astro=list_of_astro, number=sum_of_astro)