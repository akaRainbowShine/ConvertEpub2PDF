import os
from PIL import Image

source = "page"
images = []
from fpdf import FPDF
pdf = FPDF()
for i in range(2,299): #number of images
    #if (i!= 198 and i!=284):
        for file in os.listdir(source + str(i)):
            #print(file)
            if file.endswith(".png"):
                #print(file)
                images.append(Image.open(source + str(i) + "//" + file))
               # im1 = Image.open(source + str(i) + "//" + file)
im1 = Image.open("C://Users//RainbowShine//Desktop//EPUB//xhtml//pdf90hkf//page1//cornuco.png")#first page
#im1.resize((300,300))
im1.save("C://Users//RainbowShine//Desktop//thayyen//test.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=images)
