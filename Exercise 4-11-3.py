import turtle

def main():
    # Create a turtle object
    t = turtle.Turtle()

    #Create turtle settings
    turtle_setup(t)

    # create graphics window
    create_canvas(t, 600, 600)

    #draw rectangle
    rectangle(t, 90, 40)

    # Move turtle to location
    jump(t, 120, 0)

    # Draw rhombus
    rhombus(t, 80, 40)

    # Close the turtle graphics window when clicked
    turtle.exitonclick()

def turtle_setup(t):
    """Creates turtle settings such as speed/hideturtle, etc"""

    # Hide the turtle, set speed and set line color
    t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
    t.hideturtle()
    t.color("white")

def jump(t, x, y):
    """Moves turtle to specific location on canvas"""

    t.penup()
    t.goto(x, y)
    t.pendown()

def create_canvas(t, width, height):
    """Creates graphics canvas that turtle draws in using width and height"""

    # Create a window to draw in
    # Create a new turtle screen and set its background color
    screen = turtle.Screen()
    screen.bgcolor("darkblue")
    # Set the width and height of the screen
    screen.setup(width=width, height=height)
    # Clear the screen
    t.clear()

def parallelogram(t, side1, side2, angle):
    """Draws rhombus using side_length and angle"""

    # Draw the shape
    for i in range(2):
        t.forward(side1)   # Draw side
        t.left(angle)          # Larger angle
        t.forward(side2)   # Draw side again
        t.left(180 - angle)          # Smaller angle

def rectangle(t, width, height):
    parallelogram(t,width, height, 90)

def rhombus(t, side_length, angle):
    parallelogram(t, side_length, side_length, angle)

main()