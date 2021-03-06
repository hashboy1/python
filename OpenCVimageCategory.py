import cv2
import numpy as np
import tensorflow
from keras.applications import imagenet_utils
from keras.applications.inception_v3 import InceptionV3
from keras.applications.vgg19 import VGG19

model = VGG19(weights='imagenet') # load the model weights
cam = cv2.VideoCapture(0)           #开网络摄像头
while True:
    ret, frame = cam.read()
    k = cv2.waitKey(1)
    if k%256 == 27: # if esp key is pressed
        break
frame_pred = cv2.resize(frame,(224, 224))
frame_pred = cv2.cvtColor(frame_pred, cv2.COLOR_BGR2RGB).astype(np.float32)
frame_pred = frame_pred.reshape((1, ) + frame_pred.shape)
frame_pred = imagenet_utils.preprocess_input(frame_pred)
predictions = model.predict(frame_pred)
(imageID, label, score) = imagenet_utils.decode_predictions(predictions)[0][0]
cv2.putText(frame, "%s with Probability %.2f" % (label, score), (25, 25), cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 0, 250), 2)
cv2.imshow('Computer Vision on a Budget', frame)
cam.release()
cv2.destroyAllWindows()