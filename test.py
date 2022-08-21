import cv2
from keras.models import load_model
from PIL import Image
import numpy as np

model = load_model('braintumorbinary10epoch.h5')
image = cv2.imread('image/pred/pred0.jpg')

img = Image.fromarray(image)

img = img.resize((64,64))
img = np.array(img)

# print(img)

img = np.expand_dims(img,axis=0)

result = model.predict(img)
print(result)