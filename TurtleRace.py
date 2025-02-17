from turtle import Turtle,Screen
import random

is_race_on=False
s=Screen()
s.setup(500,400)
user_bet = s.textinput(title="Make a Bet.", prompt="Which turtle win the race? Enter color: ")
print(user_bet)
colors = ["red","orange","black","green","blue","purple"]
y_positions = [130,80,30,-20,-70,-120]
all_turtles = []

for i in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230,y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on =True
    
while(is_race_on):
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            win_color=turtle.pencolor()
            if win_color==user_bet:
                print(f"You've win! The {win_color} is the winner!!!")
            else:
                print(f"You've lost! The {win_color} is the winner!!!")

        run = random.randint(0,10)
        turtle.forward(run)

s.exitonclick()