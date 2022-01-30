import tensorflow as tf
from tensorflow.keras import layers

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


class Model(tf.keras.Model):
    def __init__(self):
        self.learning_rate = 0.001
        self.epochs = 80
        self.siamese_epochs = 20
        self.embedding_size = (8736)
        self.batch_size = 120
        self.optimizer = tfa.optimizers.RectifiedAdam(self.learning_rate)

        input = tf.keras.Input(shape = self.embedding_size)
        x = layers.BatchNormalization()

        base_model = tf.keras.applications.resnet50.ResNet50(weights='imagenet', include_top=False, pooling = "avg")
        for layer in base_model.layers:
            layer.trainable = False

        x = layers.Flatten()(base_model.output)
        x = self.residual_block_conv(x)
        features_extracted = layers.Dense(512, activation='softmax')(x)
        predictions = layers.Dense(26, activation = 'softmax')(x)

        self.extractor = tf.keras.Model(inputs = input, outputs = features_extracted , name = 'extractor')      
        self.predictor = tf.keras.Model(inputs = input, outputs = predictions , name = 'predictor')      

    def residual_block_conv(self, input):
        """
        This residual block is made up of Conv1D layer(s).
        """
        x = layers.Conv1D(32, 3, padding = 'same', input_shape=(512, 1))(input)
        x = layers.BatchNormalization()(x)
        x = layers.Subtract()([x, input])
        x = layers.Activation('relu')(x)
        return x  


    def call(input):
        return self.predictor(input)


def train_whole_model(model, train_inputs, train_labels, freeze_siamese=False):
    """
    Train the entire model for the specified number of epochs.

    :param model: the model
    :param train_inputs: training inputs in the shape (batch_size, 2, 8736)
    :param train_labels: training labels in the shape (batch_size)
    :param freeze_siamese: if False, train the whole model, if True, only train the classifier network
    :return history: history of the model for visualization
    """
    # compile the model
    model.classifier.compile(loss = tf.keras.losses.BinaryCrossentropy(), optimizer = model.optimizer, metrics=[tf.keras.metrics.binary_crossentropy()])
    # train the model
    history = model.classifier.fit(train_image_list, epochs = model.epochs, batch_size = model.batch_size)
    model.classifier.save_weights('whole_model_weights')
    # return history
    return history

def test(model, test_inputs, test_labels):
    """
    Evaluates the entire model.

    :param model: the model
    :param test_inputs: testing inputs in the shape (batch_size, 2, 8736)
    :param test_labels: testing labels in the shape (batch_size)
    """
    return model.classifier.evaluate([test_inputs[:, 0], test_inputs[:, 1]], test_labels, verbose=2)