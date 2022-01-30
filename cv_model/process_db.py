import tensorflow as tf
import numpy as np
import functions
from tqdm import tqdm
import pickle

END = 400
DB_FILEPATH = "products/db_all.txt"

def read_db(filepath: str) -> list:
    db_list = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            db_list.append(line.replace('\n','').split(','))
    
    return db_list

def build_db_embeddings(model: tf.keras.Model, db: list, filepath: str) -> None:
    db_list = []
    for entry in tqdm(db[200:END]):
        db_list.append(functions.get_embeddings(model, functions.convert_image_to_numpy(entry[1])))

    with open(filepath, 'wb') as fh:
        pickle.dump(db_list, fh)

def pickle_db_list(db: list):
    with open('db_pickled.txt', 'wb') as fh:
        pickle.dump(db, fh)

if __name__ == '__main__':
    pickle_db_list(read_db(DB_FILEPATH))
    model = functions.init_model()
    build_db_embeddings(model, read_db(DB_FILEPATH), 'db_embeddings.txt')

