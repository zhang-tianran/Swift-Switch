# Thrift Switch

An Google extention developed by the Swiggies to sustainable alternative of clothes from thrift stores. 

--------------------------------------------------------------------------------------------------


## Inspiration
A lot of research suggests that the fast fashion industry is a main contributor to climate change. In comparison, buying secondhand clothes is a more sustainable alternative, since it reduces the demand for new clothes. However, the appeal of fast fashion is still very strong because it tends to look more stylish. Therefore, we decided to design a chrome extension that offers our users more sustainable alternatives when they’re shopping on fast fashion sites.

## What it does
The chrome extension extracts the image from the fast fashion site that the user is interested in and matches it with a database of secondhand items from online thrift stores. It will find the most similar items and list them as the sustainable alternatives to encourage the user to buy from the thrift stores instead of the fast fashion site. 

## How we built it
We scraped the images from the thrift store using selenium library and made an extensive database of products. The database is integrated into a pre-trained model ResNet50 which use CNN architecture to extract features from pictures. Then we built a chrome extension with html javascript that extracts the image source from the user’s web browser and feeds it into our model which produces several products with similar features such as color, pattern, and style. In order to allow the chrome extension to communicate with our model, we hosted our model on a local server that listens to requests from the extension.

## Challenges we ran into
This was our first time participating in a hackathon, and trying to build something impactful within such a short amount of time was very challenging. Also, it was our first time trying to build a Chrome extension as well, so we had to learn and apply a lot of new concepts on the spot.

## Accomplishments that we're proud of
We are very proud that we have a working product. As first-time hackers, we are very happy to say that our product has all of the basic functions that we planned on implementing.

## What we learned
We learned how to make a Chrome extension and how to apply the knowledge of deep learning in image recognition and product recommendation. We also honed our problem-solving skills in a time-sensitive and high-pressure environment.

## What's next for Good
We trained our model using data from only one online thrift store, so the number of choices is somewhat limited. Also, it takes a relatively long time for the extension to generate recommendations. However, we do see our product as an expandable model. It is possible to build a larger database with more online thrift shops or even convince local thrift stores to upload their inventory. That way, we would have a larger range of choices and even more similar items. Besides, with more time, we could also speed up the recommendation-generation process by having a pre-indexed database. 

### Why are we called the Swiggies
This project cost us 22 hours in the CIT's Swig Boardroom (not including the time we slept) (also during a blizzard).
