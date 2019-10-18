import turtle

turtle.speed(10000000000000000)
global angel_1
angel_1=0

def Square(x,y,size,color,angel):
    global angel_1
    turtle.pendown ()
    turtle.color (color)
    turtle.penup ()
    turtle.setx ( x )
    turtle.sety ( y )
    turtle.begin_fill ()
    turtle.pendown ( )
    turtle.right(angel)
    turtle.right(angel-angel_1)
    angel_1= angel_1+angel
    turtle.forward (size)
    turtle.right(90)
    turtle.forward ( size )
@@ -19,14 +23,16 @@ def Square(x,y,size,color,angel):
    turtle.forward ( size )
    turtle.end_fill ()
def Parallelogram(x,y,size,color,angel):
    global angel_1
    turtle.pendown ()
    turtle.color (color)
    turtle.penup ()
    turtle.setx ( x )
    turtle.sety ( y )
    turtle.begin_fill ()
    turtle.pendown ( )
    turtle.right(angel)
    turtle.right(angel-angel_1)
    angel_1 = angel_1+ angel
    turtle.forward (size)
    turtle.right(60)
    turtle.forward ( size )
@@ -36,42 +42,23 @@ def Parallelogram(x,y,size,color,angel):
    turtle.forward ( size )
    turtle.end_fill ()
def Triangle(x,y,size,color,angel):
    global angel_1
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(angel)
    turtle.right(angel-angel_1)
    angel_1 = angel_1 + angel
    turtle.forward(size)
    turtle.right(60)
    turtle.right(90)
    turtle.forward(size)
    turtle.end_fill()


Square(0,0,160,'red',0)
Triangle(-20,1,120,'green',60)
Square(45,-45,70,"blue",-30)

Parallelogram(0,150,160, 'yellow', 30)
Parallelogram(65,190, 70,"black", 120)

Square(-400,-100,100,"green",90)
Parallelogram(-350,0, 50,"black", 120)
Parallelogram(-326,40, 50,"black", 120)
Triangle(-300,-50,180,'red',240)
Triangle(-300,-400,40,'green',120)

Triangle(-300,-400,0,'green',-120)
Square(-400,300,200,"#c49b64",120)
Square(-340,250,30,"green",90)
Square(-370,250,30,"white",90)
Square(-280,250,30,"green",90)
Square(-250,250,30,"white",90)
Parallelogram(-340,200, 80,"red", 90)
Triangle(-400,300,66,'brown',90)
Triangle(-300,-400,0,'green',-80)
Triangle(-290,300,66,'brown',-300)
if(angel_1>360):
    angel_1=angel_1-360


Triangle(0,0,700,"#3e83a3",0)
turtle.mainloop()
