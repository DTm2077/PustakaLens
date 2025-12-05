import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

# Load the model
model = tf.keras.models.load_model('artifact_classifier.keras')

# Load a sample image to predict
img_path = 'img1.jpg'  # Change to the path of your test image
img = image.load_img(img_path, target_size=(180, 180))  # Ensure it matches the input size of the model

# Convert the image to a numpy array and expand dimensions (since the model expects a batch)
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

# Normalize the image
img_array = img_array / 255.0  # Same normalization used in training

# Make predictions
predictions = model.predict(img_array)

# Get the predicted class
  # Replace with your actual class names
predicted_class = class_names[np.argmax(predictions)]

# Print the result
print(f"Predicted class: {predicted_class}")
print(f"Prediction probabilities: {predictions}")
