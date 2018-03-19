#!/usr/bin/env python

from fpdf import FPDF
import sys


pdf = FPDF()

def getImages (dir , initImage, finalImage):
    
    images = []
    for i in range(initImage,finalImage+1,1):
        image = dir + str(i) + ".png"
        images.append(image)
    
    return images



def createPDF(listImage,nameFile):

    for i in listImage:

        pdf.add_page()
        pdf.image(i,-5,-5,220)   
       

    pdf.output(nameFile,"F")

    return

if __name__ == "__main__":

    dir = sys.argv[1]
    initImage = int(sys.argv[2])
    finalImage = int(sys.argv[3])
    nameFile = sys.argv[4]

    
    images = getImages(dir,initImage,finalImage)

    print("creating PDF...")

    createPDF(images,nameFile)