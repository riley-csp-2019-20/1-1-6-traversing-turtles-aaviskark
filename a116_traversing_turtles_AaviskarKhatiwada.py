#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

# starts the pen at (0,0)
startx = 0
starty = 0

# calls the turtles to move
for t in my_turtles:
	t.penup()
	t.goto(startx, starty)
	t.pendown()
	t.right(45)     
	t.forward(50)
	t.color


	

#	tells the turtles to move a certain amount
	startx = t.xcor()
	starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()