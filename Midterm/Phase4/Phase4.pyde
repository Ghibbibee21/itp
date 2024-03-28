def setup():
    size(400, 400) 
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

for x in range(0, 400):
    for y in range(0, 400):
def draw():
    drawObject(1,9,1)
    drawObject(1,99,1)
    
