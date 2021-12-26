from canvas import Canvas
from rectangle import Rectangle
from sqare import Square

# Creating Canvas
height = int(input("Enter height of canvas: "))
width = int(input("Enter width of canvas: "))
red = input("enter amount of red out of 255: ")
green = input("enter amount of green out of 255: ")
blue = input("enter amount of blue out of 255: ")
filename = "canvas1.png"
canvas = Canvas(height, width, [red, green, blue], filename)
canvas.make()

# Creating shapes

while True:
    answer = input("Enter 'Y' if u want to draw some shapes and enter 'Q' for Quit: ")
    if answer == "Y":
        answer2 = input("what you want to draw?(rectangle or square): ")
        # creating rectangle
        if answer2.lower() == "rectangle":
            x = int(input("Enter x coordinate of rectangle: "))
            y = int(input("Enter y coordinate of rectangle: "))
            width2 = int(input("Enter the width of rectangle: "))
            height2 = int(input("Enter height of rectangle: "))
            red2 = input("enter amount of red out of 255: ")
            green2 = input("Enter amount of green out of 255: ")
            blue2 = input("Enter amount of blue out of 255: ")
            rect = Rectangle(x, y, [red2, green2, blue2], width=width2, height=height2)
            rect.draw(canvas)

        # creating square
        elif answer2.lower() == "square":
            x1 = int(input("Enter x coordinate of square: "))
            y1 = int(input("Enter y coordinate of square: "))
            side = int(input("Enter side of square: "))
            red3 = input("enter amount of red out of 255: ")
            green3 = input("enter amount of green out of 255: ")
            blue3 = input("enter amount of blue out of 255: ")
            sqr = Square(x1, y1, [red3, green3, blue3], side)
            sqr.draw(canvas)
        else:
            break
    else:
        print("thx for using!")
        break
