def drawSection(x, y):
    stallWidth = 82.5
    stallHeight = 65
    strokeWeight(2)
    fill(0, 255, 0)
    for i in range (2):
        for j in range (10):
            rect(x, y, stallWidth, stallHeight)
            x += stallWidth
        x -= (10*stallWidth)
        y += stallHeight

def setup():
    size(1900, 1000)
    background(0,150,0)
    fill(50, 50, 50)
    stroke(255, 255, 255)
    strokeWeight(5)
    lotWidth = 1800
    lotHeight = 600
    streetWidth = 75
    rect(50, 250, lotWidth, lotHeight)
    rect(-5, 150, 1910, streetWidth)
    rect(-5, 875, 1910, streetWidth)
    noStroke()
    rect(925, 175, streetWidth, lotHeight + 150)
    stroke(255, 255, 255)
    x = 100
    y = 275
    for i in range(2):
        for j in range (3):
            drawSection(x, y)
            y += 205
        x += 900
        y = 275

# def draw():
    # if  mousePressed:
    #     fill(0)
    # else:
    #     fill(255)
    # ellipse(mouseX, mouseY, 80, 80)
