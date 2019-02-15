import turtle
def draw(radius,size):
    obj = turtle.Turtle()
    radius = int(radius)
    size = int(size)
    for i in range(int(radius)):
        obj.fd(int(size))
        x = 360 / int(radius)
        obj.lt(x)
   
ra = input("Enter radius for shape:")
si = input("Enter size for shape:")
draw(ra,si)
