import turtle
import random
import time
t=turtle
t.Screen()
t.title("THE FLAPPING BIRD")
t.bgcolor("lightblue")
t.bgpic("flapbirdbgpic1.gif")
t.setup(1450,710)
t.pu()
t.speed(0)
t.goto (-500,120)
turtle.register_shape("flap1.gif")
turtle.register_shape("flap2.gif")
turtle.register_shape("flap3.gif")
turtle.register_shape("flap4.gif")
turtle.register_shape("621ca8f0ceba0791000195.gif")
turtle.register_shape("heartlife.gif")
#t.shape("621ca8f0ceba0791000195.gif")
turtle.register_shape("fruit1.gif")
turtle.register_shape("fruit2.gif")
turtle.register_shape("fruit3.gif")
turtle.register_shape("pipeblock.gif")
turtle.register_shape("closegame1.gif")
turtle.register_shape("collapse.gif")
turtle.register_shape("mpot.gif")
turtle.register_shape("henl.gif")
turtle.register_shape("bird2.gif")
turtle.register_shape("bird2a.gif")
turtle.register_shape("henl2.gif")
turtle.register_shape("bat1.gif")
turtle.register_shape("bat2.gif")
turtle.register_shape("bat3.gif")
turtle.register_shape("crab1.gif")
turtle.register_shape("crab2.gif")
turtle.register_shape("p1.gif")
turtle.register_shape("p2.gif")
turtle.register_shape("p3.gif")


h=turtle.Turtle()
h.pu()
h.speed(0)
h.shape("henl.gif")
h.goto(310,-230)
h.st()

cr=turtle.Turtle()
cr.pu()
cr.speed(0)
cr.shape("crab1.gif")
cr.goto(700,-270)
cr.st()

ps=turtle.Turtle()
ps.pu()
ps.speed(0)
ps.shape("mpot.gif")
ps.goto(1000,1000)


cl=turtle.Turtle()
cl.speed(0)
cl.pu()
cl.goto(1100,-300)
cl.shape("pipeblock.gif")

cld=turtle.Turtle()
cld.speed(0)
cld.pu()
cld.goto(500,-250)
cld.shape("pipeblock.gif")

clo=turtle.Turtle()
clo.speed(0)
clo.pu()
clo.goto(-300,-270)
clo.shape("pipeblock.gif")

cl1=turtle.Turtle()
cl1.speed(0)
cl1.pu()
cl1.goto(100,300)
cl1.shape("pipeblock.gif")

cl2=turtle.Turtle()
cl2.speed(0)
cl2.pu()
cl2.goto(800,350)
cl2.shape("pipeblock.gif")

cl3=turtle.Turtle()
cl3.speed(0)
cl3.pu()
cl3.goto(1400,400)
cl3.shape("pipeblock.gif")

bt=turtle.Turtle()
bt.pu()
bt.speed(0)
bt.shape("bird2.gif")
bt.goto(1650,145)
bt.st()

b=turtle.Turtle()
b.pu()
b.speed(0)
b.shape("bird2.gif")
b.goto(1050,220)
b.st()



a=turtle.Turtle()
a.speed(0)
a.shape("fruit3.gif")
a.color("brown")
a.pu()
a.shapesize(.8)
a.goto(500,0)

an=turtle.Turtle()
an.speed(0)
an.shape("heartlife.gif")
an.pu()
an.goto(1000,1000)

w=turtle.Turtle()
w.speed(0)
w.pu()
w.ht()
w.goto(350,300)
w.write("POINTS : 0 ",font=("agency fb",25, "bold"))

l=turtle.Turtle()
l.speed(0)
l.pu()
l.ht()
l.goto(200,300)
l.pencolor("brown")
l.write("LIFE : 5 ",font=("impact",25))

cs=turtle.Turtle()
cs.pu()
cs.speed(0)
cs.shape("closegame1.gif")
cs.goto(1000,1000)
cs.ht()

s=turtle.Turtle()
s.pu()
s.shape("621ca8f0ceba0791000195.gif")
s.speed(0)
s.goto(-500,120)
s.st()

def fly():
    t.shape("flap1.gif")
    y=t.ycor()
    t.sety(y+73)
    t.shape("flap4.gif")
def right():
    t.shape("flap3.gif")
    x=t.xcor()
    t.setx(x+21)
    t.shape("flap4.gif")
def left():
    t.shape("flap2.gif")
    x=t.xcor()
    t.setx(x-18)
    t.shape("flap3.gif")
def down(x,y):
    sc=0
    lf=5
    lsc=0
    psc=0
    t.ht()
    t.goto(-550,450)
    t.st()
    s.ht()
    cs.ht()
    l.goto(200,300)
    l.color("brown")
    l.clear()
    l.write("LIFE : {} ".format(lf),font=("impact",25))
    w.clear()
    w.write("POINTS : 0 ",font=("agency fb",25, "bold"))
    while True:
        x2=random.randint(-100,600)
        cx2=random.randint(730,1060)
        y2=random.randint(-200,200)
        ycl=random.randint(-300,-210)
        ycl1=random.randint(230,300)
        ycl2=random.randint(230,300)
        ycl3=random.randint(230,300)
        yclo=random.randint(-300,-210)
        ycld=random.randint(-300,-210)
        px1=random.randint(100,600)
        by1=random.randint(15,180)
        t.update()
        t.shape("flap1.gif")
        h.shape("henl.gif")
        b.shape("bird2.gif")
        bt.shape("bat1.gif")
        cr.shape("crab2.gif")
        if t.ycor() >=-340:
            y=t.ycor()
            x=a.xcor()
            t.sety(y-28)
            a.setx(x-25)
            anx=an.xcor()
            an.setx(anx-26)
            xcl=cl.xcor()
            cl.setx(xcl-23)
            xclo=clo.xcor()
            clo.setx(xclo-23)
            xcld=cld.xcor()
            cld.setx(xcld-23)
            xcl1=cl1.xcor()
            cl1.setx(xcl1-23)
            xcl2=cl2.xcor()
            cl2.setx(xcl2-23)
            xcl3=cl3.xcor()
            cl3.setx(xcl3-23)
            ps.bk(23)
            h.bk(26)
            h.shape("henl2.gif")
            b.bk(27)
            b.shape("bird2a.gif")
            bt.bk(33)
            bt.shape("bat2.gif")
            cr.bk(28)
            cr.shape("crab1.gif")
        if t.ycor() >=200:
            y=t.ycor()
            t.sety(y-20)
            t.listen()
        if t.xcor() >=400:
            t.bk(20)
        if t.xcor() <=-600:
            t.fd(20)
        if t.distance(a)<=50:
            a.goto(900,y2)
            sc=sc+10
            lsc=lsc+1
            psc=psc+1
            w.clear()
            w.write("POINTS : {} ".format(sc),font=("agency fb",25, "bold"))
            shapes=random.choice(["fruit1.gif","fruit2.gif","fruit3.gif"])
            a.shape(shapes)
        if a.xcor()<=-740:
            a.goto(1200,y2)
            shapes=random.choice(["fruit1.gif","fruit2.gif","fruit3.gif"])
            a.shape(shapes)
        if cl.xcor() <=-750:
            cl.goto(1200,ycl)
        if cl1.xcor() <=-750:
            cl1.goto(1200,ycl1)
        if cl2.xcor() <=-750:
            cl2.goto(1200,ycl2)
        if cl3.xcor() <=-750:
            cl3.goto(1200,ycl3)
        if clo.xcor() <=-750:
            clo.goto(1200,yclo)
        if cld.xcor() <=-750:
            cld.goto(1200,ycld)
        if t.distance(cl)<=195 or t.distance(clo)<=195 or t.distance(cld)<=195:
            t.shape("collapse.gif")
            time.sleep(.4)
            t.ht()
            y=t.ycor()
            t.sety(y+120)
            t.st()
            lf=lf-1
            l.clear()
            l.write("LIFE : {} ".format(lf),font=("impact",25))
        if t.distance(cl1)<=180 or t.distance(cl2)<=180 or t.distance(cl3)<=180:
            t.shape("collapse.gif")
            time.sleep(.4)
            t.ht()
            y=t.ycor()
            t.sety(y-120)
            t.st()
            lf=lf-1
            l.clear()
            l.write("LIFE : {} ".format(lf),font=("impact",25))
        if t.ycor() <=-340:
            t.shape("collapse.gif")
            time.sleep(.4)
            t.shape("flap1.gif")
            t.ht()
            y=t.ycor()
            t.sety(y+300)
            t.st()
            t.shape("flap4.gif")
            lf=lf-1
            l.clear()
            l.write("LIFE : {} ".format(lf),font=("impact",25))
        if lf<=0:
            l.clear()
            l.goto(0,-10)
            l.pencolor("blue")
            l.write("GAME OVER",font=("mistral",50),align="center")
            cs.goto (100,-50)
            cs.st()
            s.shape("621ca8f0ceba0791000195.gif")
            s.goto (-100,-50)
            s.st()
            t.goto(1000,1000)
        if lsc>=5 and lf <5:
            lsc=0
            an.goto(x2,40)
        if t.distance(an)<=40:
            an.goto(1000,1000)
            lf=lf+1
            l.clear()
            l.write("LIFE : {} ".format(lf),font=("impact",25))
        if t.distance(ps)<=60:
            ps.goto(px1,-240)
            sc=sc+15
            w.clear()
            w.write("POINTS : {} ".format(sc),font=("agency fb",25, "bold"))
            if lf<5:
                lf=lf+1
                l.clear()
                l.write("LIFE : {} ".format(lf),font=("impact",25))
        if ps.xcor()<=-800:
            ps.goto(px1,-240)
        if h.xcor()<=-800:
            h.goto(960,-230)
        if t.distance(h)<=85:
            hy=t.ycor()
            t.sety(hy+60)
            t.shape("flap2.gif")
            h.shape("collapse.gif")
            time.sleep(.3)
            h.goto(900,-230)
            sc=sc-5
            w.clear()
            w.write("POINTS : {} ".format(sc),font=("agency fb",25, "bold"))
        if t.distance(b)<=95:
            by=t.ycor()
            t.sety(by-60)
            t.shape("flap2.gif")
            b.shape("collapse.gif")
            time.sleep(.4)
            b.goto(1050,by1)
            sc=sc-5
            w.clear()
            w.write("POINTS : {} ".format(sc),font=("agency fb",25, "bold"))
        if b.xcor()<=-800:
            b.goto(1050,by1)
        if cr.xcor()<=-800:
            cr.goto(cx2,-270)
        if bt.xcor()<=-800:
            bt.goto(1750,140)
        if t.distance(bt)<=125:
            bty=bt.ycor()
            byt=t.ycor()
            t.sety(byt-60)
            bt.shape("bat3.gif")
            bt.sety(y-100)
            t.shape("collapse.gif")
            time.sleep(.3)
            lf=lf-1
            l.clear()
            l.write("LIFE : {} ".format(lf),font=("impact",25))
            bt.undo()
        if bt.distance(cl1)<=180 or bt.distance(cl2)<=180 or bt.distance(cl3)<=180:
            bt.fd(50)
        if b.distance(cl1)<=185 or b.distance(cl2)<=185 or b.distance(cl3)<=185:
            b.fd(70)
        if h.distance(cl)<=120 or h.distance(clo)<=120 or h.distance(cld)<=120:
            h.fd(30)
        if cr.distance(cl)<=120 or cr.distance(clo)<=120 or cr.distance(cld)<=120:
            cr.fd(40)
        if ps.distance(cl)<=180 or ps.distance(clo)<=180 or ps.distance(cld)<=180:
            ps.fd(70)
        if b.distance(bt)<=125:
            bt.shape("bat3.gif")
            b.shape("collapse.gif")
            time.sleep(.3)
            b.goto(1050,by1)
        if h.distance(cr)<=60:
            h.shape("collapse.gif")
            time.sleep(.3)
            h.goto(800,-230)
        if h.distance(a)<=40:
            a.goto(760,y2)
        if t.distance(cr)<=100:
            cry=cr.ycor()
            cyr=t.ycor()
            t.sety(cyr+60)
            cr.sety(y-100)
            t.shape("collapse.gif")
            time.sleep(.3)
            lf=lf-1
            l.clear()
            l.write("LIFE : {} ".format(lf),font=("impact",25))
        if cr.distance(ps)<=80:
            ps.shape("p1.gif")
            time.sleep(.1)
            cr.shape("collapse.gif")
            ps.shape("p2.gif")
            time.sleep(.2)
            ps.shape("p3.gif")
            time.sleep(.2)
            ps.goto(1000,-240)
            ps.shape("mpot.gif")
            cr.goto(cx2,-280)
        if h.distance(ps)<=80:
            ps.shape("p1.gif")
            time.sleep(.1)
            h.shape("collapse.gif")
            ps.shape("p2.gif")
            time.sleep(.2)
            ps.shape("p3.gif")
            time.sleep(.1)
            ps.goto(1000,-240)
            ps.shape("mpot.gif")
            h.goto(800,-230)
        if lf>5:
            lf=5
            l.clear()
            l.write("LIFE : {} ".format(lf),font=("impact",25))
        if lf>=4:
            ps.goto(1000,1000)
        if b.distance(a)<=50:
            a.goto(770,y2)
        if t.ycor()<=-600:
            lf=lf+1
            l.clear()
            l.write("LIFE : {} ".format(lf),font=("impact",25))
def close(x,y):
    t.bye()
cs.onclick(close)
t.onkey(fly,"Up")
s.onclick(down)
t.onkey(right,"Right")
t.onkey(left,"Left")
t.listen()
t.mainloop()
