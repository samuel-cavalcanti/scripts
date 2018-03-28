#!/usr/bin/env python

import cv2
import numpy
import sys

def createArucoMarkers(sizeBytes, numberOfMarkers):
    sizeBytes = int(sizeBytes)
    numberOfMarkers = int(numberOfMarkers)
    
    dictionary =  cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    

    for i in range(0,numberOfMarkers):
      arucoImage = cv2.aruco.drawMarker(dictionary,i,sizeBytes,1)
      imageName = "4x4Marker_" + str(sizeBytes) + "_" + str(i)  + ".png"

      cv2.imwrite(imageName,arucoImage)

    return





if __name__ == "__main__":

    sizeBytes = sys.argv[1]
    numberOfMarkers = sys.argv[2]
    createArucoMarkers(sizeBytes,numberOfMarkers)



