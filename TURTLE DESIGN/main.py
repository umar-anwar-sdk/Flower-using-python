import random
import turtle
from tkinter import *


def draw_flower():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    turtle.speed(2)

    # Draw petals
    for _ in range(6):
        turtle.color(random.choice(colors))
        turtle.begin_fill()
        turtle.circle(100, 60)
        turtle.left(120)
        turtle.circle(100, 60)
        turtle.end_fill()
        turtle.left(60)

    # Draw flower center
    turtle.color("brown")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.hideturtle()


def draw_flower_gui():
    root = Tk()
    root.title("Turtle Flower GUI")

    canvas = Canvas(root, width=400, height=400)
    canvas.pack()

    def draw_flower_on_canvas():
        canvas.delete("all")
        draw_flower()
        turtle.update()
        turtle.hideturtle()

    draw_button = Button(root, text="Draw Flower", command=draw_flower_on_canvas)
    draw_button.pack(pady=10)

    quit_button = Button(root, text="Quit", command=root.destroy)
    quit_button.pack(pady=10)

    root.mainloop()


# Call the function to draw the flower using GUI
draw_flower_gui()
