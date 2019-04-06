from __future__ import print_function
import cv2
from imutils import paths
import numpy as np
import imutils
import cv2,sys


class VideoCamera(object):

    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.KNOWN_DISTANCE = 96.0
        # initialize the known object width, which in this case, the piece of
        # paper is 12 inches wide
        self.KNOWN_WIDTH = 40.0
        
        # load the furst image that contains an object that is KNOWN TO BE 2 feet
        # from our camera, then find the paper marker in the image, and initialize
        # the focal length
        self.image = cv2.imread("test_data/come.jpg")
        self.marker = self.find_marker(self.image)
        self.focalLength = (self.marker[1][0] * self.KNOWN_DISTANCE) / self.KNOWN_WIDTH
        self.video = cv2.VideoCapture(0)
        self.value = 0.0
        self.lamb = 0.85
        self.i = 0
        
        
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()

    def find_marker(self,image):
	# convert the image to grayscale, blur it, and detect edges
        # print(image.shape)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 35, 125)
    
        # find the contours in the edged image and keep the largest one;
        # we'll assume that this is our piece of paper in the image
        cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        try :
            c = max(cnts, key = cv2.contourArea)
        except :
            c = 1.0
        # compute the bounding box of the of the paper region and return it
        return cv2.minAreaRect(c)

    def distance_to_camera(self,knownWidth, focalLength, perWidth):
        # compute and return the distance from the maker to the camera
        return (knownWidth * focalLength) / perWidth
        
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        self.i += 1
        marker = self.find_marker(image)
        inches = 2*self.distance_to_camera(self.KNOWN_WIDTH, self.focalLength, marker[1][0])
        self.value = round(((self.value*self.lamb) + ((1.0-self.lamb)*inches)),3)   
        
        # draw a bounding box around the image and display it
        
        box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
        box = np.int0(box)
        cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
        cv2.putText(image, "%.1fcm" % (self.value),
            (image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
            2.0, (0, 255, 0), 3)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes(),inches
        