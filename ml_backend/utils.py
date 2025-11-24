import io
import numpy as np
from PIL import Image
import tensorflow as tf

def process_image(image_bytes: bytes) -> np.ndarray:
    """
    This function processes the image to fit the model's input.
    It resizes, normalizes, and prepares the image.
    
    Args:
        image_bytes (bytes): The raw bytes of the image.

    Returns:
        np.ndarray: The preprocessed image, ready for model prediction.
    """
    IMG_SIZE = 180  # The expected input size of your model (update if needed)
    
    # Open the image from bytes and convert it to RGB
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    
    # Resize the image to the model's expected size
    img = img.resize((IMG_SIZE, IMG_SIZE))
    
    # Convert the image to a NumPy array
    img_array = np.array(img)
    
    # Normalize the pixel values (if needed, based on your model's training)
    img_array = img_array / 255.0  # Scaling pixel values to [0, 1]
    
    # Add a batch dimension (models expect batches of images)
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array
