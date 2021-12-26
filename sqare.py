from PIL import Image


class Square:

    def __init__(self, x, y, color, side):
        self.x = x
        self.y = y
        self.color = color
        self.side = side

    def draw(self, not_canvas):
        not_canvas.data[self.x:self.x + self.side, self.y:self.y + self.side] = self.color
        img = Image.fromarray(not_canvas.data, "RGB")
        img.save(not_canvas.file_name)
