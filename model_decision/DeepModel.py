# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 17:53:20 2022

@author: talha
"""

import matplotlib.image as mpimg
import torch
import time
import math
import numpy as np
import torch.optim as optim
import os

from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
import torchvision.transforms as transforms
import os
import math
import numpy as np
from PIL import Image

from Model import *
size = 128
img_path = "C:/Users/talha/Desktop/CXR_Detecter/src/Cxr_images/COVID-5.png"
imgs = Image.open(img_path)

test_transforms = transforms.Compose([
            transforms.Resize([size,size]),
            transforms.ToTensor(),

        ])


if __name__ == "__main__":


    import pickle

    loaded_model = pickle.load(open("C:/Users/talha/Desktop/CXR_Detecter/src/Models/model.p", 'rb'))
    
    model = Model()
    
    model = loaded_model

    img = (test_transforms (imgs)).reshape(1,1,128,128)
    
    with torch.no_grad():

        y_pred = model(img)
