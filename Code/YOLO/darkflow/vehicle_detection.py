import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt 

options = {
    'model': './cfg/yolo.cfg',
    'load': './bin/yolov2.weights',
    'threshold': 0.3
}

tfnet = TFNet(options)
inputPath = os.getcwd() + "/test_images/"
outputPath = os.getcwd() + "/output_images/"

def detectVehicles(filename):
    global tfnet, inputPath, outputPath
    img = cv2.imread(inputPath + filename, cv2.IMREAD_COLOR)
    result = tfnet.return_predict(img)
    for vehicle in result:
        label = vehicle['label']
        if label in ["car", "bus", "bike", "truck", "rickshaw"]:
            top_left = (vehicle['topleft']['x'], vehicle['topleft']['y'])
            bottom_right = (vehicle['bottomright']['x'], vehicle['bottomright']['y'])
            img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
            img = cv2.putText(img, label, top_left, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    outputFilename = outputPath + "output_" + filename
    cv2.imwrite(outputFilename, img)
    print('Output image stored at:', outputFilename)

for filename in os.listdir(inputPath):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        detectVehicles(filename)

print("Done!")
