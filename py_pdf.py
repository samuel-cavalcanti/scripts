#!/usr/bin/env python

from fpdf import FPDF

pdf = FPDF()

dir = "solidos/images/"
images = []
for i in range(1,288,1):
    image = dir + str(i) + ".png"
    images.append(image)


print("creating PDF...")
   

for i in images:

    pdf.add_page()
    pdf.image(i,-5,-5,220)   
    print(i)

pdf.output("solidos.pdf","F")



