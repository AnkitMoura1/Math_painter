from canvas import Canvas
from rectangle import Rectangle
from sqare import Square


height = int(input("Enter height of canvas: "))
width = int(input("Enter width of canvas: "))
red = input("enter amount of red out of 255: ")
green = input("enter amount of green out of 255: ")
blue = input("enter amount of blue out of 255: ")
filename = "canvas1.png"
answer = input("Enter 'Y' if u want to draw some shapes and enter 'Q' for Quit: ")
if answer == "Y":
    canvas = Canvas(height, width, [red, green, blue], filename)
    canvas.make()
    x = int(input("Enter x coordinate of rectangle: "))
    y = int(input("Enter y coordinate of rectangle: "))
    width2 = int(input("Enter the width of rectangle: "))
    height2 = int(input("Enter height of rectangle: "))
    red2 = input("enter amount of red out of 255: ")
    green2 = input("Enter amount of green out of 255: ")
    blue2 = input("Enter amount of blue out of 255: ")
    rect = Rectangle(x, y, [red2, green2, blue2], width=width2, height=height2)
    rect.draw(canvas)
else:
    print("thx for using!")
