import tensorflow as tf

category_list = []
image_path_list = []
data_type_list = []
# category names
with open('list_category_cloth.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        if i > 1:
            category_list.append(line.split(' ')[0])

# category map
with open('list_category_img.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        if i > 1:
            image_path_list.append([word.strip() for word in line.split(' ') if len(word) > 0])


# train, valid, test
with open('list_eval_partition.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        if i > 1:
            data_type_list.append([word.strip() for word in line.split(' ') if len(word) > 0])




def init_model() -> tf.keras.Model:
    res_model = tf.keras.applications.resnet50.ResNet50(weights='imagenet', include_top=False, pooling = "avg")
    simple_res_model = tf.keras.models.Sequential()
    simple_res_model.add(res_model)
    simple_res_model.add(tf.keras.layers.Flatten())
    return simple_res_model


