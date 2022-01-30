import requests

image_url = "https://cf-assets-thredup.thredup.com/assets/283097661/retina.jpg"
img_data = requests.get(image_url).content
with open('images/image_name.jpg', 'wb') as handler:
    handler.write(img_data)