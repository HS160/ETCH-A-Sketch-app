from turtle import Turtle, Screen

tim  = Turtle()
tim.shape("turtle")
tim.pensize(5)
tim.color('blue')
screen = Screen()

def forward():
    tim.forward(50)
def backword():
    tim.backward(50)
def clockwise():
    tim.right(10)
def anti_clockwise():
    tim.left(10)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(forward,'w')
screen.onkey(backword,'s')
screen.onkey(anti_clockwise,'a')
screen.onkey(clockwise,'d')
screen.onkey(clear_screen,'c')

screen.exitonclick()