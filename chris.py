'''
name=input("what's your name?")
print("hello"+name)
'''
'''
for i in range(1,10):
    print(i)

'''
'''
import turtle
turtle.speed(1)
turtle.pencolor('purple')
turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)
'''
import turtle
import random
turtle.bgcolor("black")
t=turtle.Pen()
t.speed(0)
t.width(2)
for x in range(300):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    turtle.colormode(255)
    t.color(r,g,b)
    
    t.forward(50 + x)
    t.right(90.911)    
turtle.done()

