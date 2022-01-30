import functions
import numpy as np

INPUT_IMAGE_URL = 'https://media1.popsugar-assets.com/files/thumbor/OZTN2C1c-Ur2QoMhOgKGvdJB7iE/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2018/01/24/981/n/1922398/shop08XKid/i/Shein-Sequin-Detail-Glitter-Mesh-Wrap-Dress.jpg'

if __name__ == '__main__':
    db_embeddings = functions.load_db_embeddings()
    db_list = functions.load_db_list()
    model = functions.init_model()
    input_img_numpy = functions.convert_image_to_numpy(INPUT_IMAGE_URL)
    embedding = functions.get_embeddings(model, input_img_numpy)
    print(np.shape(db_list))
    print(np.shape(db_embeddings))
    neighbors = functions.get_knn(embedding, db_embeddings)
    print(db_list[neighbors])


