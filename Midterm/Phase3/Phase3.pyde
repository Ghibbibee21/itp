def setup():
    size(150, 150) 
    noStroke() 

def drawObject(x,y,s):
    push()
    translate(x,y)
    fill(130)
    scale(s)
    rect(100, 60,  9, 50)
    rect(40, 60,  9, 50)
    rect(85, 60,  9, 50)
    rect(25, 60,  9, 50)
    rect(25, 45,  84, 30)
    ellipse(105, 45, 50, 50)
    fill(0)
    ellipse(95, 40, 5, 15)
    ellipse(115, 40, 5, 15)
    rect(97, 55, 15, 5)
    pop()

def draw():
    drawObject(0,0,1)
    drawObject(0,200,1)
