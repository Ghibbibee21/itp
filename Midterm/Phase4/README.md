# Phase 4
- For this phase, I started off with my code from phase 3.
``` python
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
```
- Then I changed the grid size from 150 x 150 to 400 x 400 and messed with the DrawObject parameters.
``` python
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

def draw():
    drawObject(1,9,1)
    drawObject(1,99,1)
```
- I got a repeat of one creature but I'm not exactly getting any tiling.
- So I read the hint about for loops and I looked up an example of for loops [here](https://wiki.python.org/moin/ForLoop)
- This is what I landed on.
``` python
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
```
- It yielded a repeat of the previous result.
