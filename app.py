from flask import Flask, render_template, request, jsonify
from flask_frozen import Freezer
from sql_traceability.logic.parser import parse_sql

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trace', methods=['POST'])
def trace():
    sql_script = request.form['sql_script']
    traceability_data = parse_sql(sql_script)
    return jsonify(traceability_data)

if __name__ == '__main__':
    freezer.freeze()
