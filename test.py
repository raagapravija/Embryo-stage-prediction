import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
model = tf.keras.models.load_model('/Users/pravija/Desktop/project/transfer_learning.h5')


# Load the saved model
#model = tf.keras.models.load_model('path/to/saved/model')

# Load and preprocess the image
img_path = '/Users/pravija/Desktop/project/dataset/t4/D2011.03.21_S0074_I132_WELL3_RUN129.jpeg'
img = image.load_img(img_path, target_size=(500, 500))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Make the prediction
predictions = model.predict(x)
print(predictions)
top_predictions = np.argmax(predictions,axis=1)
# Get the top 5 predictions
top_predictions=np.argsort(predictions)[0][:5]
print(top_predictions)

class_labels=['t2','t3','t4','t5','t6','t7','t8','t9+','tB','tEB','tHB','tM','tPB2','tPNa','tPB2','tPNF','tSB']
count=1
for pred in top_predictions:
    print("Predicted class",count,":",class_labels[pred])
    count+=1