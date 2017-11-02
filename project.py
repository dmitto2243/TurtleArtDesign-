import turtle 
turtle.bgcolor("black")
bob = turtle.Turtle()
turtle.tracer(0)

bob.speed(10)
bob.color("red")
for times in range(180):
    bob.forward(100)
    bob.right(30)
    bob.forward(20)
    bob.left(60)
    bob.forward(50)
    bob.right(30)
    
    bob.penup()
    bob.setposition(0, 0)
    bob.pendown()
    
    bob.right(2)
    

for times in range(256):
    bob.circle(10000)
    bob.right(120)
    bob.left(180)
    bob.right(150)
    bob.left(120)
    bob.right(110)
    bob.left(100)
    bob.right(20)
    bob.left(80)
    bob.right(12)
    bob.left(18)
    bob.right(2)
    bob.left(8)
