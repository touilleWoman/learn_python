



tab = (
	(0,0,0,0,0,0,0,0,0,0),
	(0,0,0,0,0,0,0,0,0,0),
	(0,0,0,2,0,0,0,0,0,0),
	(0,0,0,1,1,0,0,0,0,0),
	(0,0,0,0,0,0,0,0,0,0),
	(0,0,0,0,0,0,0,0,0,0),
	(0,0,0,0,0,0,0,0,0,0),
	(0,0,0,0,0,0,0,3,0,0),
	(0,0,0,0,0,0,0,0,0,0),
	(0,0,0,0,0,0,0,0,0,0)
	)

import turtle

def border(t, screen_x, screen_y):
    """(Turtle, int, int)

    Draws a border around the canvas in red.
    """
    # Lift the pen and move the turtle to the center.
    t.penup()
    t.home()

    # Move to lower left corner of the screen; leaves the turtle
    # facing west.
    t.forward(screen_x / 2)
    t.right(90)
    t.forward(screen_y / 2)
    t.setheading(180)           # t.right(90) would also work.

    # Draw the border
    t.pencolor('red')
    t.pendown()
    t.pensize(10)
    for distance in (screen_x, screen_y, screen_x, screen_y):
        t.forward(distance)
        t.right(90)

    # Raise the pen and move the turtle home again; it's a good idea
    # to leave the turtle in a known state.
    t.penup()
    t.home()


def square(t, size, color):
    """(Turtle, int, str)

    Draw a square of the chosen colour and size.
    """
    t.pencolor(color)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)


def draw_all():
	screen = turtle.Screen()
	screen.title('Map')
	screen_x, screen_y = screen.screensize()
	t = turtle.Turtle()
	# Uncomment to draw the graphics as quickly as possible.
	# t.speed(0)
	border(t, screen_x, screen_y)
	# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
	# t.pensize(3)
	# square(t, screen_x / 2, colors[0])

draw_all()

print('1 stand for obstacles, 3 need to find the fastest way to 2')


turtle.shape("turtle")

turtle.forward(25)

turtle.exitonclick()

# i = 0
# while (i < 10):
# 	print(tab[i])
# 	i=i+1

# def find_pos(val, double_list):
# 	i = 0
# 	j = 0

# 	for j in range(10):
# 		for i in range(10):
# 			if double_list[i][j] == val:
# 				return (i, j)
# 		i = 0



# x, y = find_pos(3, tab)
# print(x, y)
