import turtle

# Initialize turtle
stift = turtle.Turtle()
w = turtle.Screen()
w.setup(width=720, height=420)
stift.speed(5)

# Function to draw a filled rectangle
def draw_rectangle(x, y, width, height, color):
    stift.penup()
    stift.goto(x, y)
    stift.pendown()
    stift.color(color)
    stift.begin_fill()
    
    for _ in range(2):
        stift.forward(width)
        stift.right(90)
        stift.forward(height)
        stift.right(90)
    
    stift.end_fill()

# German flag dimensions and drawing
def draw_german_flag():
    flag_width = 300
    flag_height = 180
    stripe_height = flag_height / 3

    # Draw the black stripe (top)
    draw_rectangle(-150, 90, flag_width, stripe_height, "black")
    
    # Draw the red stripe (middle)
    draw_rectangle(-150, 90 - stripe_height, flag_width, stripe_height, "red")
    
    # Draw the gold stripe (bottom)
    draw_rectangle(-150, 90 - 2 * stripe_height, flag_width, stripe_height, "gold")

# Draw the German flag
draw_german_flag()

# Move turtle out of the way
stift.hideturtle()

# Close window on click
w.exitonclick()
