import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, height, width, color, file_name):
        self.width = width
        self.height = height
        self.color = color
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color
        self.file_name = file_name

    def make(self):
        img = Image.fromarray(self.data, "RGB")
        img.save(self.file_name)
