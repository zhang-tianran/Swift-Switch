import cv_model.functions as functions
import urllib.error

def query(input_url : str) -> list:
    db_embeddings = functions.load_db_embeddings()
    db_list = functions.load_db_list()
    model = functions.init_model()
    try: 
        input_img_numpy = functions.convert_image_to_numpy(input_url)
    except urllib.error.HTTPError as e:     
        print(e.reason)
    embedding = functions.get_embeddings(model, input_img_numpy)
    neighbors = functions.get_knn(embedding, db_embeddings)
    return db_list[neighbors]


