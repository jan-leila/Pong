# Import the good things
import Tkinter
import time
import math

# What direction the player should be moving
player1Vertical = 2
player2Vertical = 2

# Create the main window
root = Tkinter.Tk()
root.wm_title('')
# create canvas with black background
canvas = Tkinter.Canvas(root, height=500, width=1000, background='#000000')
canvas.grid(row=0, column=1, rowspan=3)

# Define a class for the player(s)
class player():
    # Create a player at a x and y cord with a height to be determentd
    def __init__(self,x,y,height):
        self.x = x
        self.y = y
        self.xVel = 0
        self.yVel = 0
        # vars that are constent for now but could be changed later for powerups
        self.height = height
        self.speed = 20
        self.color = '#ffffff'
        # create a colition box that is the same size as the player
        self.box = collitionBox(self.x,self.y,25, height)
        self.sprite = canvas.create_rectangle(self.x, self.y, (self.x + 25), (self.y + height), outline=self.color, fill=self.color)
        self.score = 0
    # Set the speed of the player
    def setVel(self,x,y):
        self.xVel = x
        self.yVel = y
    # Move player based on a vertical and horizontal speed then scale based on how long ago this function was last run
    def move(self,deltaTime):
        # Add the Vel to the position scaled by speed and time sence last run
        self.x = self.x + (self.xVel * deltaTime * self.speed)
        self.y = self.y + (self.yVel * deltaTime * self.speed)
        # Move the collition box and the sprite
        self.box.translate((self.xVel * deltaTime * self.speed), (self.yVel * deltaTime * self.speed))
        canvas.move(self.sprite, (self.xVel * deltaTime * self.speed), (self.yVel * deltaTime * self.speed))
    # Set postion of the player
    def setPos(self,x,y):
        canvas.move(self.sprite, (self.x - x) * -1, (self.y - y) * -1)
        self.box.translate((self.x - x) * -1, (self.y - y) * -1)
        self.x = x
        self.y = y
# Define a colition box object
class collitionBox():
    # Create box based on the top left and a width/height
    def __init__(self,topLeftX,topLeftY,width,height):
        self.topLeftX  = topLeftX
        self.topLeftY  = topLeftY
        self.bottomRightX  = topLeftX + width
        self.bottomRightY  = topLeftY + height
    # Test if a box is inside this box or if the box is inside another box
    def testCollition(self, box):
        return self.testBoxIn(box) or box.testBoxIn(self)
    # Test each corner on a box and see if it is in this box
    def testBoxIn(self,box):
        return self.testPointCollition(box.topLeftX,box.topLeftY) or self.testPointCollition(box.topLeftX,box.bottomRightY) or self.testPointCollition(box.bottomRightX,box.bottomRightY) or self.testPointCollition(box.bottomRightX,box.topLeftY)
    # For a point check that it is inbetween the x and y cord of top left and bottom right
    def testPointCollition(self,PointX,PointY):
        return (((PointX >= self.topLeftX)and(PointX <= self.bottomRightX))and((PointY >= self.topLeftY)and(PointY <= self.bottomRightY)))
    # Move the box by x and y
    def translate(self, x, y):
        self.topLeftX  = self.topLeftX + x
        self.topLeftY  = self.topLeftY + y
        self.bottomRightX  = self.bottomRightX + x
        self.bottomRightY  = self.bottomRightY + y
# Define a ball object
class Ball():
    # Create ball based on a position size speed and angle it is moveing at
    def __init__(self,x,y,size,speed,angle):
        # Vars for movement
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        # Makeing vars for a posible powerup
        self.size = size
        # Creating sprite and colition box
        self.box = collitionBox(self.x,self.y,size, size)
        self.sprite = canvas.create_rectangle(self.x, self.y, (self.x + size), (self.y + size), outline='#ffffff', fill='#ffffff')
    # Move ball based on its speed and rotaion that it is moveing at then scale by the delta time
    def move(self,deltaTime):
        #Colition detection for player 1 and 2
        global player1,player2
        if(self.box.testCollition(player1.box)):
            # if player 1 hit make angle into the reflex angle for angle
            self.angle = 3.14159265359 -(math.tan((self.y - (player1.y - (player1.height/2)))/(self.x - player1.x)))
        if(self.box.testCollition(player2.box)):
            # if player 2 hit make angle into the reflex angle for angle
            self.angle = 6.28318530718 - math.tan((self.y - (player2.y - (player2.height/2)))/(self.x - player2.x))
        # Cos is the x cord on a unit circle
        self.x = self.x + (math.cos(self.angle) * self.speed * deltaTime)
        # Sin is the y cord on a unit circle
        self.y = self.y + (math.sin(self.angle) * self.speed * deltaTime)
        # If ball hits top of screen reflect it
        if(self.y < 0):
            canvas.move(self.sprite, 0, self.y * -1)
            self.angle = 6.28318530718 - self.angle
            self.setPos(self.x,0)
        # If ball hits bottom of the screen reflect it
        elif(self.y > 475):
            canvas.move(self.sprite, 0, 475 - self.y )
            self.angle = 6.28318530718 - self.angle
            self.setPos(self.x,475)
        # If ball hits left side of the screen player 2 scores
        if(self.x < 0):
            player2.score = player2.score + 1
            canvas.itemconfig(player2Score, text=str(player2.score))
            self.setPos(500,250)
            self.angle = 3.1415
        # If ball hits left side of the screen player 1 scores
        elif(self.x > 1000):
            player1.score = player1.score + 1
            canvas.itemconfig(player1Score, text=str(player1.score))
            ball.setPos(500,250)
            self.angle = 0
        # Move ball sprite and collition box    
        canvas.move(self.sprite, (math.cos(self.angle) * self.speed * deltaTime), (math.sin(self.angle) * self.speed * deltaTime))
        self.box.translate((math.cos(self.angle) * self.speed * deltaTime), (math.sin(self.angle) * self.speed * deltaTime))
    # Set the postion of the ball
    def setPos(self,x,y):
        canvas.move(self.sprite, (self.x - x) * -1, (self.y - y) * -1)
        self.box.translate((self.x - x) * -1, (self.y - y) * -1)
        self.x = x
        self.y = y
# Create player and ball
player1 = player(800,250,100)
player2 = player(200,250,100)
ball = Ball(500,250,25,250,0)
# Create scoreboard
player1Score = canvas.create_text(50,250,text=str(0),fill='#ffffff')
player2Score = canvas.create_text(950,250,text=str(0),fill='#ffffff')
# Gets current time to we can get delta time in between each run
systemTime = time.time()
def tick():
    #calcualte delta time then set system time again
    global systemTime
    deltaTime = time.time() - systemTime
    systemTime = systemTime + deltaTime
    # Get key input for player1 and then move them based on time
    if(player1Vertical != 2):
        player1.setVel(0,player1Vertical * player1.speed)
        player1.move(deltaTime)
    else:
        #If player1's keys havent been touched they are a perfect AI
        player1.setPos(player1.x,ball.y - (player1.height/2))
    # Get key input for player2 and then move them based on time
    if(player2Vertical != 2):
        player2.setVel(0,player2Vertical * player2.speed)
        player2.move(deltaTime)
    else:
        #If player2's keys havent been touched they are a perfect AI
        player2.setPos(player2.x,ball.y - (player2.height/2))
    # Move ball based on time
    ball.move(deltaTime)
    # Run tick again
    canvas.after(1, tick)
# Starts tick for the first time
tick()

# Events for keys pressed (player1)
def UpPress(event):
    global player1Vertical
    player1Vertical = -1
##    print"Up pressed"
    
def UpRelease(event):
    global player1Vertical
    player1Vertical = 0
##    print"Up Released"

def DownPress(event):
    global player1Vertical
    player1Vertical = 1
##    print"Down pressed"
    
def DownRelease(event):
    global player1Vertical
    player1Vertical = 0
##    print"Down Released"

# Events for keys pressed (player2)
def WPress(event):
    global player2Vertical
    player2Vertical = -1
##    print"W pressed"
    
def WRelease(event):
    global player2Vertical
    player2Vertical = 0
##    print"W Released"

def SPress(event):
    global player2Vertical
    player2Vertical = 1
##    print"S pressed"
    
def SRelease(event):
    global player2Vertical
    player2Vertical = 0
##    print"S Released"
    
# Binding key events to the actual keys on the keyboard
root.bind('<KeyPress-Up>', UpPress)
root.bind('<KeyRelease-Up>', UpRelease)
root.bind('<KeyPress-Down>', DownPress)
root.bind('<KeyRelease-Down>', DownRelease)
root.bind('<KeyPress-w>', WPress)
root.bind('<KeyRelease-w>', WRelease)
root.bind('<KeyPress-s>', SPress)
root.bind('<KeyRelease-s>', SRelease)

# Enter event loop
root.mainloop()
