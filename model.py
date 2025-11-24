import tensorflow as tf

# Load the model
def load_model(model_path: str):
    model = tf.keras.models.load_model(model_path)
    return model
