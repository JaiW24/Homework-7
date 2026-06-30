from graphics import *
from math import *


def drawPolygon(n, centerX, centerY, radius):
    points = []

    angle = 360 / n

    for i in range(n):
        currentAngle = radians(i * angle)

        x = centerX + radius * cos(currentAngle)
        y = centerY + radius * sin(currentAngle)

        points.append(Point(x, y))

    return Polygon(points)


def insideButton(click, button):
    p1 = button.getP1()
    p2 = button.getP2()

    x = click.getX()
    y = click.getY()

    if p1.getX() <= x <= p2.getX() and p1.getY() <= y <= p2.getY():
        return True
    else:
        return False


def main():
    win = GraphWin("N-Gon Graph", 500, 500)

    label = Text(Point(100, 30), "Number of Sides:")
    label.draw(win)

    entry = Entry(Point(250, 30), 10)
    entry.draw(win)

    button = Rectangle(Point(350, 15), Point(450, 45))
    button.draw(win)

    buttonText = Text(Point(400, 30), "Graph")
    buttonText.draw(win)

    while True:
        click = win.getMouse()

        if insideButton(click, button):
            break

    sides = int(entry.getText())

    polygon = drawPolygon(sides, 250, 250, 150)
    polygon.draw(win)

    buttonText.setText("Exit")

    while True:
        click = win.getMouse()

        if insideButton(click, button):
            break

    win.close()


main()