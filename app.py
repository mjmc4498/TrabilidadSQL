from flask import Flask, render_template, request, jsonify
from sql_traceability.logic.parser import parse_sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trace', methods=['POST'])
def trace():
    sql_script = request.form['sql_script']
    traceability_data = parse_sql(sql_script)
    return jsonify(traceability_data)

if __name__ == '__main__':
    app.run(debug=True)
