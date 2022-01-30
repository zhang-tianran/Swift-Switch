from sklearn.neighbors import NearestNeighbors
import tensorflow as tf
import numpy as np
from PIL import Image
import urllib.request
import pickle

DB_EMBEDS = "cv_model/db_embeddings.txt"
DB_LIST = "cv_model/db_pickled.txt"

def convert_image_to_numpy(url: str):
    urllib.request.urlretrieve(url, 'temp.jpg')
    img = Image.open('temp.jpg')
    img_to_numpy_array = tf.keras.preprocessing.image.img_to_array(img)
    x = tf.cast(img_to_numpy_array, tf.float32)
    return tf.expand_dims(tf.keras.applications.resnet50.preprocess_input(img_to_numpy_array), 0)

def get_embeddings(model: tf.keras.Model, image: np.ndarray) -> np.ndarray:
    return model.predict(image)

def get_knn(input: np.ndarray, database: np.ndarray) -> np.ndarray:
    neigh = NearestNeighbors(n_neighbors=3)
    neigh.fit(database)
    return neigh.kneighbors(input, return_distance = False)

def init_model() -> tf.keras.Model:
    res_model = tf.keras.applications.resnet50.ResNet50(weights='imagenet', include_top=False, pooling = "avg")
    simple_res_model = tf.keras.models.Sequential()
    simple_res_model.add(res_model)
    simple_res_model.add(tf.keras.layers.Flatten())
    return simple_res_model

def load_db_embeddings() -> list:
    pickle_off = open(DB_EMBEDS, "rb")
    loaded = pickle.load(pickle_off)
    return np.squeeze(np.array(loaded))

def load_db_list() -> list:
    pickle_off = open (DB_LIST, "rb")
    loaded = pickle.load(pickle_off)
    return np.array(loaded)
