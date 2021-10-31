import turtle
from turtle import Turtle, Screen
import random
import RegExService
import numpy



X=0
Y=0
turtle_1 = Turtle()
turtle_2 = Turtle()
turtle_1.shape("circle")
turtle_2.shape("circle")
turtle_2.color("Black")
turtle_2.hideturtle()
turtle_2.penup()

turtle.colormode(255)


colours = ["Red", "Blue", "Purple", "Orange","Yellow", "Green", "Pink", "Black", "Violet","Cyan","Grey","green yellow","dark cyan","medium violet red","Grey","orange red","light sky blue"]



def show_path(solution,no_of_trucks,fileName):
    capacityLimit, graph, demand, optimalValue,trucks = RegExService.getData(fileName)
    X,Y=graph[1]
    X=X*-5
    Y=Y*-5
    vertices = list(graph.keys())
    vertices.remove(1)
    print(graph)
    print(solution)
    turtle_1.pensize(2)
    turtle_1.penup()
    turtle_1.goto(X,Y)
    turtle_1.pendown()





    for j in range(0,no_of_trucks):
        turtle_1.color(colours[j])
        turtle_1.goto(X,Y)
        turtle_1.pendown()
        for i in solution[0][j]:
            x, y = graph[i]
            turtle_1.goto(x*-5, y*-5)
            turtle_2.goto(x*-5, y*-5)
            turtle_2.pendown()
            turtle_2.pensize(1)
            turtle_2.write(f" {i} ({x}, {y})", align="center", font=("poppins", 5, "normal"))
            turtle_2.penup()
        turtle_1.goto(X, Y)
        turtle_1.penup()

# screen = Screen()
#
# show_path(Solution, 5)
# screen.exitonclick()




