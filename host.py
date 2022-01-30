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
    print(type(url))
    [[a, b, c]] = cv_model.query.query(url)
    return jsonify({"a": a[0], "b":b[0], "c":c[0]})
    # TODO: return 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    

# from flask import Flask, request, render_template

# app = Flask(__name__)
# app.debug = True


# @app.route("/", methods=['GET', 'POST'])
# def index():
#     if request.method == "POST":
#         name = request.form["name"]
#         return name + " Hello"
#     return render_template("index.html")


# if __name__ == "__main__":
#     app.run()