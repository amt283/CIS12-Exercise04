import turtle

def main():
    # Create a turtle object
    t = turtle.Turtle()

    #Create turtle settings
    turtle_setup(t)

    # create graphics window
    create_canvas(t, 600, 600)

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


def rhombus(t, side_length, angle):
    """Draws rhombus using side_length and angle"""

    # Draw the rectangle
    for i in range(2):
        t.forward(side_length)   # Draw side
        t.left(angle)          # Larger angle
        t.forward(side_length)   # Draw side again
        t.left(180 - angle)          # Smaller angle

main()