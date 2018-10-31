#Candy INFO
candy_pos = PVector(80, -90)
Cspeed = PVector(0, 5)
limit_speed = PVector(0, 10)
candy_size = 60
# Ghost INFO
ghost = PVector(180, 810)
ghost_speed = PVector(0, -2) 
ghost_size = 80
# Player INFO
player_size = 120
score = 0
x1 = 280
y1 = 600
# Image INFO
candy_img = requestImage("RedCandy.png")
pumking_img = requestImage("pumpkin.png")
fantasma_img = requestImage("fantasma.png")
background_img = requestImage("background.jpg")
bw_img = requestImage("bw.png")

def setup():
    size(700, 800)

def draw():
    
# Global Variables        
    global candy_pos
    global Cspeed
    global player_size
    global candy_size
    global limit_speed
    global x1,y1
    global score
    global ghost
    global ghost_speed
    global ghost_size
    global limit_ghost_speed
    global candy_img 
    global pumking_img 
    global fantasma_img
    global background_img
    global bw_img
    
# Background
    background_img.resize(width, height)
    image(background_img, 1, -1)
    fill(0)
    rect(0,700,800,800)
    
# Player Catches Candy
    radius = player_size/2
    candy_radius = candy_size/2

    a = candy_pos.x - x1
    b = candy_pos.y - y1
    distance = sqrt(a**2 + b**2) 
    
    if distance <= radius + candy_radius:
        candy_pos.x = random(width)
        score += 1
        candy_pos.y = (-10)
        
# Ghost
    tint(255, 126)
    image(fantasma_img, ghost.x, ghost.y, ghost_size, ghost_size)
    ghost.add(ghost_speed)
    
    if ghost.y <= (-20):
        ghost.y = 810
        ghost.x = random(width)

# Red Candy
    noTint()
    image(candy_img, candy_pos.x, candy_pos.y, candy_size, candy_size)
    candy_pos.add(Cspeed)
    if candy_pos.y > height:
        candy_pos.y = 0
        candy_pos.x = random(width)
        Cspeed += PVector(0, 1)
    if Cspeed >= limit_speed:
        Cspeed = PVector(0, 3)

# Player/Pumpkin
    noTint()
    noStroke()
    image(pumking_img,x1, y1, player_size+40, player_size)
    
# Border
    image(bw_img, 2, 2)

# Instructions
    fill(255)
    textSize(20)
    text("Move using the arrow keys", 240, 760)
            
# Score
    fill(255, 0, 0)
    font = loadFont("ACaslonPro-SemiboldItalic-48.vlw")
    textFont(font, 32)
    textSize(60)
    text(score, 110, 140)

def keyReleased():
    global x1, y1 
    if (key==CODED):
        if (keyCode == LEFT):
            x1 = x1 - 50 
        elif (keyCode== RIGHT):
            x1 = x1 + 50