from turtle import Turtle,Screen

tim=Turtle()
s=Screen()

tim.width(2)

def move_forward():
    tim.fd(10)

def turn_left():
    tim.left(10)

def move_back():
    tim.backward(10)

def turn_right():
    tim.right(10)


s.listen()
s.onkey(key="w",fun=move_forward)
s.onkey(key="s",fun=move_back)
s.onkey(key="a",fun=turn_left)
s.onkey(key="d",fun=turn_right)
s.onkey(key="c",fun=t.reset)
s.exitonclick()
