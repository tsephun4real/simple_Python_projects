import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.color("Black")
pen.speed(1) 

num_squares = 36  # Number of squares
side_length = 200  # Length of each side of the square
angle = 360 / num_squares 

def draw_square(side_length):
    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)

for _ in range(num_squares):
    draw_square(side_length)
    pen.right(angle)

pen.hideturtle()
turtle.done()
