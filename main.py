import turtle
import os

turtle.tracer(1)
turtle.setundobuffer(1)

# Setting up screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)     # lower is faster
border_pen.color("white")
border_pen.penup()
border_pen.goto(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()

# Player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15   # pixels to move

# Enemy creation

invader = turtle.Turtle()
invader.color("red")
invader.shape("circle")
invader.penup()
invader.speed(0)
invader.setposition(-200, 250)

invader_speed = 2

# Player's gunfire

gunfire = turtle.Turtle()
gunfire.color("yellow")
gunfire.shape("triangle")
gunfire.penup()
gunfire.speed(0)
gunfire.setheading(90)
gunfire.shapesize(0.5, 0.5)
gunfire.hideturtle()

gunfire_speed = 20

# State of the gun

gunfire_state = "ready"     # when game is started


# Movement of player


def left_movement(event):
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)


def right_movement(event):
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)


def gunfiring():
    global gunfire_state    # any changes here are reflected everywhere to this var
    if gunfire_state == "ready":
        gunfire_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        gunfire.setposition(x, y)
        gunfire.showturtle()


# Keyboard bindings
# win.onkey(left_movement, "Left")
# win.onkey(right_movement, "Right")
# in order to keep turtle moving continuously without multiple presses
turtle.getcanvas().bind('<Right>', right_movement)
turtle.getcanvas().bind('<Left>', left_movement)
turtle.onkey(gunfiring, "space")
win.listen()

# Main loop

while True:
    inv_x = invader.xcor()
    inv_x += invader_speed
    invader.setx(inv_x)
    if invader.xcor() > 280:
        invader_speed *= -1
        invader.sety(invader.ycor() - 40)

    if invader.xcor() < -280:
        invader_speed *= -1
        invader.sety(invader.ycor() - 40)

    # moving the gunfire
    if gunfire_state == "fire":
        gunfire.sety(gunfire.ycor() + gunfire_speed)

    # gunfire border

    if gunfire.ycor() > 275:
        gunfire_state = "ready"
        gunfire.hideturtle()

win.mainloop()
