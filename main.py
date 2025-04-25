from turtle import Turtle,Screen

tim=Turtle()
sc=Screen()

tim.width(2)

def move_forward():
    tim.fd(10)

def turn_left():
    tim.left(10)

def move_back():
    tim.backward(10)

def turn_right():
    tim.right(10)


sc.listen()
sc.onkey(key="w",fun=move_forward)
sc.onkey(key="s",fun=move_back)
sc.onkey(key="a",fun=turn_left)
sc.onkey(key="d",fun=turn_right)
sc.onkey(key="c",fun=t.reset)
sc.exitonclick()
