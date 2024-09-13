import turtle

# Initialize turtle
kalem = turtle.Turtle()
w = turtle.Screen()
w.setup(width=720, height=420)
w.bgcolor("red")
kalem.speed(5)

# Function to draw filled circles
def draw_circle(x, y, radius, color):
    kalem.penup()
    kalem.goto(x, y - radius)
    kalem.pendown()
    kalem.color(color)
    kalem.begin_fill()
    kalem.circle(radius)
    kalem.end_fill()

# Function to draw the star
def draw_star(x, y, length):
    kalem.penup()
    kalem.goto(x, y)
    kalem.pendown()
    kalem.color("white")
    kalem.begin_fill()
    kalem.setheading(288)  # Correct alignment for the star
    for _ in range(5):
        kalem.forward(length)
        kalem.right(144)
    kalem.end_fill()

# Draw the crescent
draw_circle(-100, 0, 120, "white")   # Outer white circle
draw_circle(-70, 0, 100, "red")      # Inner red circle to create the crescent

# Draw the star in the middle of the crescent
draw_star(40, 35, 80)

# Add a smaller white circle in the middle of the star
draw_circle(25, 5, 17, "white")  # Smaller white circle to ensure the star's center is white

# Move turtle out of the way
kalem.hideturtle()

# Close window on click
w.exitonclick()
