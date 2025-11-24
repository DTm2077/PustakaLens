import tensorflow as tf

try:
    # Replace with the path to your actual model file
    MODEL_PATH = 'ml_backend/artifact_classifier.keras'  # For example: 'model/batik_classifier.keras'
    
    # Load the model
    model = tf.keras.models.load_model(MODEL_PATH)
    
    # If successful, print a success message
    print("Model loaded successfully.")

except Exception as e:
    # If there's an error, print the error message
    print(f"Error loading model: {e}")
