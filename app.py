import os
import json
import requests

from flask import Flask, render_template, request


app = Flask(__name__)
app.config['DEBUG']=True


@app.route("/")
def index():
    r = requests.get('https://pomber.github.io/covid19/timeseries.json')
    f=json.loads(r.text)['Iraq']
    deaths=[]
    date=[]
    confirmed=[]
    recovered=[]
    legend = 'Monthly Data'
    for i in f:
        date.append(i['date'])
    for i in f:
        deaths.append(i['deaths'])
    for i in f:
        confirmed.append(i['confirmed'])
    for i in f:
        recovered.append(i['recovered'])
    maxdeaths=max(deaths)
    maxconfirmed=max(confirmed)
    maxrecovered=max(recovered)
    active=maxconfirmed - maxrecovered - maxdeaths

    return render_template("index.html", f=f,deaths=deaths,date=date,confirmed=confirmed,recovered=recovered,maxdeaths=maxdeaths,maxconfirmed=maxconfirmed,maxrecovered=maxrecovered, active=active)
