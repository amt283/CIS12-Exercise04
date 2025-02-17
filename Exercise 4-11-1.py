import turtle

def main():
    # Create a turtle object
    t = turtle.Turtle()

    #Create turtle settings
    turtle_setup(t)

    # create graphics window
    create_canvas(t, 600, 600)

    # Draw rectangle
    rectangle(t, 80, 40)

    # Close the turtle graphics window when clicked
    turtle.exitonclick()

def turtle_setup(t):
    # Hide the turtle, set speed and set line color
    t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
    t.hideturtle()
    t.color("white")

def create_canvas(t, width, height):
    """Creates graphics canvas that turtle draws in using width and height"""

    # Create a window to draw in
    # Create a new turtle screen and set its background color
    screen = turtle.Screen()
    screen.bgcolor("darkblue")
    # Set the width and height of the screen
    screen.setup(width=600, height=600)
    # Clear the screen
    t.clear()


def rectangle(t, width, height):
    """Draws rectangle using width and height"""

    # Draw the rectangle
    for i in range(2):
        t.forward(width)   # Draw the longer side
        t.left(90)          # Turn 90 degrees
        t.forward(height)   # Draw the shorter side
        t.left(90)          # Turn 90 degrees

main()