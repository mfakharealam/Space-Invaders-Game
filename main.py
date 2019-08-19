import turtle
import math
import random

turtle.tracer(1)
turtle.setundobuffer(1)

# Setting up screen
win = turtle.Screen()
win.bgcolor("black")
win.setup(700, 700)
win.title("Space Invaders")
win.bgpic("space_invaders_background.gif")

# for shapes

turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

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

# Adding score

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 275)
score_str = "Score: %s" % score
score_pen.write(score_str, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15   # pixels to move

invader_speed = 2

# creating multiple invaders

no_of_invaders = 5

invaders_list = []

for i in range(no_of_invaders):
    # Enemy creation
    invaders_list.append(turtle.Turtle())

for invader in invaders_list:
    invader.color("red")
    invader.shape("invader.gif")
    invader.penup()
    invader.speed(0)
    random_x = random.randint(-200, 200)
    random_y = random.randint(100, 250)
    invader.setposition(random_x, random_y)

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


def is_collision(turtle1, turtle2):
    distance = math.sqrt(math.pow(turtle1.xcor() - turtle2.xcor(), 2) + math.pow(turtle1.ycor() - turtle2.ycor(), 2))
    if distance < 16:
        return True
    return False


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
    for invader in invaders_list:
        inv_x = invader.xcor()
        inv_x += invader_speed
        invader.setx(inv_x)
        # moving invaders down and in reverse
        if invader.xcor() > 280:
            for i in invaders_list:
                i.sety(i.ycor() - 40)
            invader_speed *= -1

        if invader.xcor() < -280:
            for i in invaders_list:
                i.sety(i.ycor() - 40)
            invader_speed *= -1

        # check for collision between invader and gunfire

        if is_collision(gunfire, invader):
            gunfire.hideturtle()
            gunfire_state = "ready"  # to fire it again
            gunfire.setposition(0, -400)
            # reset the invader
            random_x = random.randint(-200, 200)
            random_y = random.randint(100, 250)
            invader.setposition(random_x, random_y)
            # score update
            score += 10
            score_str = "Score: %s" % score
            score_pen.clear()
            score_pen.write(score_str, False, align="left", font=("Arial", 14, "normal"))

        if is_collision(player, invader):
            player.hideturtle()
            invader.hideturtle()
            print("Game Over")
            break

    # moving the gunfire
    if gunfire_state == "fire":
        gunfire.sety(gunfire.ycor() + gunfire_speed)

    # gunfire border

    if gunfire.ycor() > 275:
        gunfire_state = "ready"
        gunfire.hideturtle()


win.mainloop()
