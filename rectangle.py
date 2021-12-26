from PIL import Image


class Rectangle:

    def __init__(self, x, y, color, width, height):
        self.height = height
        self.width = width
        self.color = color
        self.y = y
        self.x = x

    def draw(self, not_canvas):
        not_canvas.data[self.x:self.x + self.height, self.y:self.y + self.width] = self.color
        img = Image.fromarray(not_canvas.data, "RGB")
        img.save(not_canvas.file_name)
