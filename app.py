import os
import json
import requests
from flask import Flask, render_template, request
from flask_assets import Bundle, Environment
app = Flask(__name__)


@app.route("/")
def index():
    r = requests.get('https://pomber.github.io/covid19/timeseries.json')
    IraqInfo = json.loads(r.text)['Iraq']
    deaths = []
    date = []
    confirmed = []
    recovered = []
    legend = 'Monthly Data'
    for i in IraqInfo:
        date.append(i['date'])
    for i in IraqInfo:
        deaths.append(i['deaths'])
    for i in IraqInfo:
        confirmed.append(i['confirmed'])
    for i in IraqInfo:
        if i['recovered'] is not None:
            recovered.append(i['recovered'])
    print(recovered)
    maxdeaths = max(deaths)
    maxconfirmed = max(confirmed)
    maxrecovered = max(recovered)
    active = max(confirmed) - max(recovered) - max(deaths)

    return render_template(
        "index.html",
        IraqInfo=IraqInfo,
        deaths=deaths,
        date=date,
        confirmed=confirmed,
        recovered=recovered,
        maxdeaths=maxdeaths,
        maxconfirmed=maxconfirmed,
        maxrecovered=maxrecovered,
        active=active)
