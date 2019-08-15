import turtle
import os

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


# Keyboard bindings
# win.onkey(left_movement, "Left")
# win.onkey(right_movement, "Right")
# in order to keep turtle moving continuously without multiple presses
turtle.getcanvas().bind('<Right>', right_movement)
turtle.getcanvas().bind('<Left>', left_movement)

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


win.mainloop()
