from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    filePath = "static/CADE Hap Generated Files 2022-06-10/cade_abt_analysis/scenario_data_20220601192555474.json"
    with open(filePath, 'r') as f:
        data = json.load(f)
    return render_template("cade-tree.html", data=data, filePath=filePath)


if __name__ == '__main__':
    app.run()
