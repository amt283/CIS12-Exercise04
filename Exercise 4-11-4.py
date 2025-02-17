import turtle

def main():
    # Create a turtle object
    t = turtle.Turtle()

    #Create turtle settings
    turtle_setup(t)

    # create graphics window
    create_canvas(t, 600, 600)

    # Draw pie
    draw_pie(t, 120, 6)

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

def triangle(t, side_length):
    """Draws triangle using side_length"""

    # Draw triangle
    for i in range(3):
        t.forward(side_length)   # Draw side
        t.left(120)          # Angle of triangle

def draw_pie(t, side_length, num_triangles):
    """Draws pie with equal sized triangles using side_length and num_triangles for slice amount"""

    # Calculate the angle to turn to form the pie
    angle = 360 / num_triangles

    # Draw the pie with the specified number of slices
    for i in range(num_triangles):
        triangle(t, side_length)  # Draw one triangle
        t.left(angle)          # Turn to form the next slice

main()