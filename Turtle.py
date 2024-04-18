import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Food Collector")
screen.setup(width=600, height=600)
screen.bgcolor("lightgreen")

# Create the turtle
turtle.shape("turtle")
turtle.color("blue")
turtle.penup()
turtle.speed(0)  # Set the turtle's speed to maximum

# Create food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# Function to move the turtle forward
def move():
    turtle.forward(10)

# Function to turn the turtle left
def turn_left():
    turtle.left(30)

# Function to turn the turtle right
def turn_right():
    turtle.right(30)

# Keyboard bindings
screen.listen()
screen.onkeypress(move, "Up")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")

# Main game loop
while True:
    # Move the turtle forward
    move()

    # Check for collision with food
    if turtle.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

    # Check for collision with screen edges
    if turtle.xcor() > 290:
        turtle.setx(290)
        turtle.left(180)
    elif turtle.xcor() < -290:
        turtle.setx(-290)
        turtle.left(180)
    elif turtle.ycor() > 290:
        turtle.sety(290)
        turtle.left(180)
    elif turtle.ycor() < -290:
        turtle.sety(-290)
        turtle.left(180)

