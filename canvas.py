import  numpy as np
from PIL import Image

class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color


    def make(self,file_name):
