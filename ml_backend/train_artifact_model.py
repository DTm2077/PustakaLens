import tensorflow as tf
import pathlib

# ============================================================================== 
# 1. PREPARING DATA
# ==============================================================================

print("Preparing dataset...")

# Specify the path to your dataset directory
data_dir = pathlib.Path('dataset')

# Parameters for images
batch_size = 32
img_height = 180
img_width = 180

# Create training dataset (80% of the data)
train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

# Create validation dataset (20% of the data)
val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

# Get class names (from folder names)
class_names = train_ds.class_names
num_classes = len(class_names)
print(f"Dataset loaded successfully. Found {num_classes} classes.")
print("Class names:", class_names)

# Optimize dataset performance
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# ============================================================================== 
# 2. TRANSFER LEARNING WITH MOBILENETV2
# ==============================================================================

print("\nBuilding model with Transfer Learning...")

# Load pre-trained MobileNetV2 model without the top classification layer
base_model = tf.keras.applications.MobileNetV2(input_shape=(img_height, img_width, 3), include_top=False, weights='imagenet')

# Freeze the base model to prevent its weights from being updated during training
base_model.trainable = False

# Create a new model by adding layers on top of the base model
model = tf.keras.Sequential([
  base_model,
  tf.keras.layers.GlobalAveragePooling2D(),  # Convert the 2D matrix to a 1D vector
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(num_classes, activation='softmax')  # Softmax for multi-class classification
])

# ============================================================================== 
# 3. TRAIN THE MODEL
# ==============================================================================

print("Compiling model...")

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['accuracy'])

print("Training model...")

# Set the number of epochs (how many times the model sees the entire dataset)
epochs = 15

# Train the model on the dataset
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)

print("\nTraining completed!")

# ============================================================================== 
# 4. SAVE THE MODEL
# ==============================================================================

# Save the trained model to a file (this will be used in the backend API)
model_filename = 'artifact_classifier_transfer.keras'
model.save(model_filename)
print(f"\nModel saved as '{model_filename}'")
