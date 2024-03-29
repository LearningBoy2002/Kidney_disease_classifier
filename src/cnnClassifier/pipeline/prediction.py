import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
        else:
            prediction = 'Normal'
            return [{ "image" : prediction}]
        



    # def predict(self):
    #     # Load model (ensure the output layer has units=4)
    #     model = load_model(os.path.join("artifacts","training", "model.h5"))

    #     # Load and preprocess image
    #     imagename = self.filename
    #     test_image = image.load_img(imagename, target_size=(224, 224))
    #     test_image = image.img_to_array(test_image)
    #     test_image = np.expand_dims(test_image, axis=0)

    #     # Predict probabilities for all classes
    #     predictions = model.predict(test_image)

    #     # Get the class with the highest probability
    #     predicted_class = np.argmax(predictions[0])
    #     class_names = ["Cyst", "Normal", "Stone", "Tumor"]  # Update with your actual class names

    #     # Return the predicted class and image
    #     return {
    #         "image": class_names[predicted_class],
    #         "probabilities": predictions[0].tolist(),  # Optional: return all probabilities
    #     }