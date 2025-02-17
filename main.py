from turtle import Turtle,Screen

t=Turtle()
s=Screen()

t.width(2)

def move_forward():
    t.fd(10)

def turn_left():
    t.left(10)

def move_back():
    t.backward(10)

def turn_right():
    t.right(10)


s.listen()
s.onkey(key="w",fun=move_forward)
s.onkey(key="s",fun=move_back)
s.onkey(key="a",fun=turn_left)
s.onkey(key="d",fun=turn_right)
s.onkey(key="c",fun=t.reset)
s.exitonclick()