import PIL
from PIL import Image, ImageDraw, ImageOps
#from Tkinter import *

class Kaleido:
    def __init__(self, ini_width, ini_height):
        self.width = ini_width
        self.height = ini_height
        self.chunk_size = 0
        
    def setImage(self, image_file):
        '''Sets an image to be kaleidoscoped.'''
        self.image_file = PIL.Image.open(image_file)
        return self.image_file

    def triangleGrab(self, loc_x, loc_y, chunk_size):
        self.chunk_size = chunk_size
        #self.image_file.size(chunk_size)
        self.triangle = self.image_file.crop((loc_x, loc_y, loc_x-self.chunk_size, loc_y-self.chunk_size))
        return self.triangle
    
    def saveKaleido(self, file_name):
        self.triangle.save(file_name + '.jpg')
        
myKaleido = Kaleido(800,500)
myKaleido.setImage("image.jpg")
myKaleido.triangleGrab(20,30,5)
myKaleido.saveKaleido("kaleido")