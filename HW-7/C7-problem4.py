from graphics import *
from time import sleep


def main():
    height = float(input("Enter the starting height in meters: "))

    win = GraphWin("Bouncing Ball", 400, 600)
    win.setCoords(0, 0, 10, height + 1)

    ground = Line(Point(0, 0), Point(10, 0))
    ground.draw(win)

    ball = Circle(Point(5, height), 0.3)
    ball.setFill("red")
    ball.draw(win)

    while height >= 0.001:

        ball.move(0, -height)
        sleep(0.3)

        height = height * 0.60

        ball.move(0, height)
        sleep(0.3)

    win.getMouse()
    win.close()


main()