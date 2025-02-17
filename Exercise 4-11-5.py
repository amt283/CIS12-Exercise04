import turtle
import math

def main():
    # Create a turtle object
    t = turtle.Turtle()

    #Create turtle settings
    turtle_setup(t)

    # create graphics window
    create_canvas(t, 600, 600)

    # Draw flower
    """FLOWER FUNCTION HERE"""
    draw_flower(t, 6,100,80)

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

def arc(t, radius, angle):
    """Draws an arc with a given radius and angle."""
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    steps = 30  # Calculate the number of steps for smoothness
    step_length = arc_length / steps
    step_angle = float(angle) / steps

    for _ in range(steps):
        t.forward(step_length)
        t.left(step_angle)

# Function to draw one petal using the arc function
def petal(t, radius, angle):
    """Draws a petal by combining two arcs."""
    for _ in range(2):  # Two arcs for each petal
        arc(t, radius, angle)
        t.left(180 - angle)  # Angle to create the other side of the petal

# Function to draw the flower by repeating the petals
def draw_flower(t, num_petals, radius, angle):
    """Draws a flower with the given number of petals, radius, and arc angle."""
    for _ in range(num_petals):
        petal(t, radius, angle)
        t.left(360 / num_petals)

main()