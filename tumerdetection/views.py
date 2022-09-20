from django.shortcuts import render,redirect
from .models import DetectionImage

import cv2
from keras.models import load_model
from PIL import Image
import numpy as np
import os
from pathlib import Path

# Create your views here.

def home(request):
    if request.method == 'POST':
        uimage = request.FILES['image1']
        file_save = DetectionImage(image =uimage)
        file_save.save()


 
        link ='C:\\Users\\PC\\Desktop\\Brain-Tumor\\' + str(file_save.image)
        print(link)
        model = load_model('braintumorbinary10epoch.h5')
        image = cv2.imread(link)
        print(image)
        img = Image.fromarray(image)

        img = img.resize((64,64))
        img = np.array(img)

        print(img)

        img = np.expand_dims(img,axis=0)

        result = model.predict(img)
        print(result)
        return render(request, 'result.html',{'result':result})
    return render(request, 'home.html')