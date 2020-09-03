import turtle
wn = turtle.Screen()
wn.title("My first turtle Peoject")
wn.bgcolor("sky blue")
wn.setup(height= 50,width=70)
wn.tracer(0)

GROUND_LVL=-40

# Drawing ground
pen=turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.shape("square")
pen.color("red")
pen.penup()

# Darwing line 
pen.goto(-400,GROUND_LVL)
pen.pendown()
pen.goto(400,GROUND_LVL)
pen.penup()

# Jumping character 
jumper=turtle.Turtle()
jumper.speed(0)
jumper.shape("square")
jumper.color("green")
jumper.penup()
jumper.width=20
jumper.height=20
jumper.dx=0
jumper.dy=0
jumper.state="ready"
jumper.goto(-200, GROUND_LVL +jumper.height/2)

GRAVITY=-0.8

def jump():
    if jumper.state=="ready":
        jumper.dy=12
        jumper.state="jumping"
        
wn.listen()
wn.onkeypress(jump, "space")

while True:
    # Gravity
    jumper.dy += GRAVITY
    
    # Moving the jumper
    y= jumper.ycor()
    y += jumper.dy
    jumper.sety(y)
    
    # More ground functions 
    if jumper.ycor()< GROUND_LVL + jumper.height/2:
        jumper.sety(GROUND_LVL +jumper.height /20)
        jumper.dy=0
        jumper.state="ready"
        
    wn.update()
    