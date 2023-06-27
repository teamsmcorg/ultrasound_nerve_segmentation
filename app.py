from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import pickle
model=pickle.load(open("C:/Users/royal/Desktop/nerve 2/model_nerve"))
# model = tf.keras.models.load_model('C:\\Users\\royal\\Desktop\\nerve 2\\model_nerve', compile=False, custom_objects={'Adam': tf.keras.optimizers.Adam})


app = Flask(__name__)
#model = pickle.load(open('C:\\Users\\royal\Desktop\\nerve 2\\model_nerve', 'rb'))

def preprocess_image(image):
    image = image.convert('L')  # Convert to grayscale
    image = image.resize((256, 256))  # Resize to model input shape
    image = np.array(image)  # Convert to numpy array
    image = image / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route('/')
def index():
    return render_template('sindex.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded image from the form
    image_file = request.files['image']
    image = Image.open(image_file)
    
    # Preprocess the image
    preprocessed_image = preprocess_image(image)
    
    # Perform prediction
    prediction = model.predict(preprocessed_image)
    
    # Post-process the prediction (e.g., apply thresholding, convert to binary mask, etc.)
    # Replace the following code with your own post-processing logic
    
    threshold = 0.5
    predicted_mask = (prediction > threshold).astype(np.uint8) * 255
    
    # Create PIL image from the predicted mask
    predicted_image = Image.fromarray(predicted_mask[0], mode='L')
    
    # Return the predicted image as a response
    return predicted_image

if __name__ == '__main__':
  app.run()
   

