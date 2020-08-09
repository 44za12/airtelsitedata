from flask import Flask, jsonify, render_template, request
import json
from jsonData import site1Data, site2Data
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    keys = list(site1Data[0].keys())
    keys.pop(0)
    keys.pop(0)
    sites = set()
    for i in site1Data:
        sites.add(i.get("Site"))
    if not request.args:
        text = "The Table is empty please select site to continue"
        return render_template('index.html', text=text, keys=keys, sites=sites)
    else:
        selectedsite = request.args.get("site")
        data = []
        for i in site1Data:
            if i.get("Site") == selectedsite:
                data.append(i)
        return render_template('index.html', data=data, keys=keys, sites=sites)

@app.route("/pizzabox", methods=['GET', 'POST'])
def pizzabox():
    keys = list(site2Data[0].keys())
    sites = set()
    for i in site2Data:
        sites.add(i.get("GIS Code"))
    if not request.args:
        text = "The Table is empty please select site to continue"
        return render_template('pizzabox.html', text=text, keys=keys, sites=sites)
    else:
        selectedsite = request.args.get("site")
        data = []
        for i in site2Data:
            if i.get("GIS Code") == selectedsite:
                data.append(i)
        return render_template('pizzabox.html', data=data, keys=keys, sites=sites)

if __name__ == "__main__":
    app.run(debug=True)