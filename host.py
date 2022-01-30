from flask import Flask, render_template, request
from flask import jsonify
import cv_model.query

app = Flask(__name__)

# # Display your index page
# @app.route("/")
# def index():
#     return render_template('index.html')

# A function to add two numbers
@app.route("/query")
def query():
    url = request.args.get('url')
    print(url)
    [a, b, c] = cv_model.query.query(url)
    return jsonify({"a": a[0], "b":b[0], "c":c[0]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)