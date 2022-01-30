# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# import numpy as np
import csv
import cv_model.functions

# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")

def get_img_src(driver, URL):
    driver.get(URL)
    product_image = driver.find_element(By.XPATH, '//a[@class="u-relative u-w-full L1B2cM22taQyxi6ANVhC"]')
    img_src = product_image.get_attribute('href')

    return img_src

def get_pages(driver, URL):
    driver.get(URL)
    products = driver.find_elements(By.XPATH, '//a[@class="u-inset-0 u-absolute wAhTkKjWOmWyIy2F13MZ"]')
    urls = []
    for product in products:
        urls.append(product.get_attribute('href'))

    return urls

def get_size_price_brand(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # size = driver.find_elements(By.XPATH, '//div[@class="P9j6cGJ6kvC9bBgLk4pE"]')[0].get_attribute('innerHTML')
    # price = driver.find_elements(By.XPATH, '//span[@class="u-text-20 u-font-bold u-text-alert price"]')[0].get_attribute('innerHTML')
    size = driver.find_elements(By.XPATH, '//div[@class="P9j6cGJ6kvC9bBgLk4pE"]')[0].text
    price = driver.find_elements(By.XPATH, '//span[@class="u-text-20 u-font-bold u-text-alert price"]')[0].text
    brand = driver.find_elements(By.XPATH, '//a[@class="ui-link u-text-20"]')[0].get_attribute('title')
    title = driver.find_elements(By.XPATH, '//span[@class = "wc1Wg5BbXVFBe4MHxY3r"]')[0].text
    driver.quit()
    type(price)
    return size, price, brand, title

def add_db_details(db_filepath: str)
    url_list = cv_model.functions.load_db_list()

    with open('products/db_details.txt', 'w') as f:
        for (i, entry) in enumerate(url_list):
            tuple = get_size_price_brand(entry[0])
            url_list[i].extend(tuple)
        csv.writer(f, delimiter=',').writerows(url_img_src)

        

# if __name__ == "__main__":
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option('useAutomationExtension', False)
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     driver = webdriver.Chrome(options=options)
#
#     mainURL = "https://www.thredup.com/women/tops/t-shirts?department_tags=women&category_tags=tops&style_tags=t-shirts&sort=price_low_high&page="
#
#     for i in range(0, 40):
#         urls = get_pages(driver, mainURL+str(i+1))
#
#         url_img_src = []
#         for idx, url in enumerate(urls):
#             img_src = get_img_src(driver, url)
#             # print(idx, url, img_src)
#             url_img_src.append([url, img_src])
#
#         with open('products/db_'+str(i+1)+'.txt', 'w') as f:
#             csv.writer(f, delimiter=',').writerows(url_img_src)
#
#     driver.quit()
#
#     # # url_img_src = [['https://www.thredup.com/product/women-cotton-old-navy-green-long-sleeve-t-shirt/94262355?query_id=600579103082504192&result_id=600579103896199168', 'https://cf-assets-thredup.thredup.com/assets/283097661/retina.jpg'], ['https://www.thredup.com/product/women-spandex-j-peterman-orange-short-sleeve-t-shirt/104176634?query_id=600579103082504192&result_id=600579103896199168', 'https://cf-assets-thredup.thredup.com/assets/314437058/retina.jpg']]
#     # # print(url_img_src)
#     #
#
#     # with open('first_10.txt', 'r') as f:
#     #     reader = csv.reader(f, delimiter=',')
#     #     for row in reader:
#     #         print(row)
#
#     # a = np.array([1, 2, 3, 4])
#     # np.savetxt('first_10.txt', url_img_src, fmt='%s')
#     # b = np.loadtxt('first_10.txt', dtype='object')
#     # print( url_img_src == b )
#
#     # URL1 = "https://www.thredup.com/product/women-cotton-madewell-black-long-sleeve-t-shirt/115320641?query_id=600519482275831808&result_id=600519484045828096"
#     # URL2 = "https://www.thredup.com/product/women-cotton-old-navy-green-long-sleeve-t-shirt/94262355?query_id=600568322274131968&result_id=600568323201073152"
#     #
#     # options = webdriver.ChromeOptions()
#     # options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     # options.add_experimental_option('useAutomationExtension', False)
#     # options.add_argument("--disable-blink-features=AutomationControlled")
#     # driver = webdriver.Chrome(options=options)
#     #
#     # img_src1 = get_img_src(driver, URL1)
#     # img_src2 = get_img_src(driver, URL2)
#     # print(img_src1)
#     # print(img_src2)
#     #
#     # driver.quit()