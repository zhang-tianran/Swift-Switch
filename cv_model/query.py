import functions
import urllib.error

# INPUT_IMAGE_URL = 'https://media1.popsugar-assets.com/files/thumbor/OZTN2C1c-Ur2QoMhOgKGvdJB7iE/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2018/01/24/981/n/1922398/shop08XKid/i/Shein-Sequin-Detail-Glitter-Mesh-Wrap-Dress.jpg'

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


