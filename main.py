import turtle
t = turtle.Turtle()

print("This programm draws a regular polygon as requested")

nr_sides = int(input("\nEnter the number of sides your regular polygon would like to have: "))
angle = 360/nr_sides
len_sides = int(input("Enter the length of sides your regular polygon would like to have: "))
color = input("Enter the color your regular polygon would like to have: ")
t.ht()
t.speed(0)
t.color(color)
t.begin_fill()
for i in range(nr_sides):
  t.fd(len_sides)
  t.lt(angle)
t.end_fill()