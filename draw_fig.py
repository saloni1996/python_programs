import turtle

brad = turtle.Turtle()

#customise brad
brad.shape("turtle")
brad.color("blue")
brad.speed(100)

def draw_shape():
    #Input length
    #print "Enter the length of square!!"
    #length = input()

    #initialise the drawing canvas
    window = turtle.Screen()
    window.bgcolor("black")

    #draw a square
    #draw_square(100)

    #draw a triangle
    #draw_triangle(100)

    #draw a circle
    #draw_circle(100)

    #to draw rgombys
    #draw_rhombus(100)

    #draw  a flower
    draw_flower()

    #draw a pattern
    #draw_pattern()

    #The window should exit when the image is drawn.
    window.exitonclick()


#To draw a straight line
def draw_straight_line(length):
    brad.forward(length)

#To draw a square
def draw_square(length):
    for i in range(1,5):
        brad.forward(length)
        brad.right(90)

#To draw a triangle
def draw_triangle(length):
    for i in range(1,4):
        brad.left(120)
        brad.forward(length)

#to draw a circle
def draw_circle(radius):
    brad.circle(radius)

#to draw a diamond
def draw_rhombus(length):
    brad.left(45)
    for i  in range(1,5):
        brad.left(90)
    #brad.forward(2*length)
    #brad.left(90)
        brad.forward(length)
    #brad.left(90)
    #brad.forward(length)
    #brad.left(90)
    #brad.forward(2*length)

#To draw a pattern
def draw_pattern():
    for i in range(1,37):
        draw_square(100)
        brad.right(10)
    brad.right(90)
    draw_straight_line(300)

#to draw a flower
def draw_flower():
    for i in range(1,37):
        draw_rhombus(100)
        brad.right(10)

    #for j in range(1,37):
        #draw_circle(50)
        #brad.right(10)

    for j in range(1,37):
        draw_circle(10)
        brad.right(10)

    for k in range(1,181):
        draw_straight_line(100)
        brad.right(180)
        draw_straight_line(100)
        brad.right(1)

    brad.right(90)
    draw_straight_line(300)


draw_shape()
