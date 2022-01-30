from flask import Flask, render_template, request
from flask import jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
import cv_model.query
import scrape_thredup

app = Flask(__name__)

# # Display your index page
# @app.route("/")
# def index():
#     return render_template('index.html')

# A function to add two numbers
@app.route("/query")
def query():
    url = request.args.get('url')
    # (a_size, a_price, a_brand, a_title) = (1, 2, 3, 4)
    # (b_size, b_price, b_brand, b_title) = (1, 2, 3, 4)
    # (c_size, c_price, c_brand, c_title) = (1, 2, 3, 4)
    # return jsonify(
    #     {"1link": "https://www.gap.com/webcontent/0018/528/146/cn18528146.jpg",
    #     "1img": "HI",
    #     "1size": a_size, 
    #     "1price": a_price, 
    #     "1brand": a_brand,
    #     "1title": a_title,
    #     "2link": "hi",
    #     "2img": "https://www.gap.com/webcontent/0018/528/146/cn18528146.jpg",
    #     "2size": b_size, 
    #     "2price": b_price, 
    #     "2brand": b_brand,
    #     "2title": b_title,  
    #     "3link": "hi",
    #     "3img": "https://www.gap.com/webcontent/0018/528/146/cn18528146.jpg",
    #     "3size": c_size, 
    #     "3price": c_price, 
    #     "3brand": c_brand,
    #     "3title": c_title})
    [[a, b, c]] = cv_model.query.query(url)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    (a_size, a_price, a_brand, a_title) = scrape_thredup.get_size_price_brand(driver, a[0])
    (b_size, b_price, b_brand, b_title) = scrape_thredup.get_size_price_brand(driver, b[0])
    (c_size, c_price, c_brand, c_title) = scrape_thredup.get_size_price_brand(driver, c[0])
    driver.quit()
    return jsonify(
        {"1link": a[0],
        "1img": a[1],
        "1size": a_size, 
        "1price": a_price, 
        "1brand": a_brand,
        "1title": a_title,
        "2link": b[0],
        "2img": b[1],
        "2size": b_size, 
        "2price": b_price, 
        "2brand": b_brand,
        "2title": b_title,
        "3link": c[0],
        "3img": c[1],
        "3size": c_size, 
        "3price": c_price, 
        "3brand": c_brand,
        "3title": c_title})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)