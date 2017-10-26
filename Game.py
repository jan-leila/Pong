import Tkinter
import time
import Animation
import ComboManager
#import Physics
import GUI

devMode = True

# Create the main window
root = Tkinter.Tk()
root.wm_title('')
# create canvas
canvas = Tkinter.Canvas(root, height=500, width=1920, background='#FFFFFF')
canvas.grid(row=0, column=1, rowspan=3)

class collitionBox:
    def __init__(self,topLeftX,topLeftY,width,height):
        self.topLeftX  = topLeftX
        self.topLeftY  = topLeftY
        self.BottomRightX  = topLeftX + width
        self.BottomRightY  = topLeftY + height

    def getTestCollition(self, box):
        return ((self.topLeftX < box.BottomRightX and self.topLeftX > box.topLeftX) and (self.topLeftY > box.BottomRightY and self.topLeftY < box.topLeftY) or (self.BottomRightX < box.BottomRightX and self.BottomRightX > box.topLeftX) and (self.topLeftY > box.BottomRightY and self.topLeftY < box.topLeftY) or (self.BottomRightX < box.BottomRightX and self.BottomRightX > box.topLeftX) and (self.BottomRightX > box.BottomRightY or self.BottomRightX < box.topLeftY) or (self.topLeftX < box.BottomRightX and self.topLeftX > box.topLeftX) and (self.BottomRightX > box.BottomRightY and self.BottomRightX < box.topLeftY) or (box.topLeftX < self.BottomRightX and box.topLeftX > self.topLeftX) and (box.topLeftY > self.BottomRightY and box.topLeftY < self.topLeftY) or (box.BottomRightX < self.BottomRightX and box.BottomRightX > self.topLeftX) and (box.topLeftY > self.BottomRightY and box.topLeftY < self.topLeftY) or (box.BottomRightX < self.BottomRightX and box.BottomRightX > self.topLeftX) and (box.BottomRightX > self.BottomRightY and box.BottomRightX < self.topLeftY) or (box.topLeftX < self.BottomRightX and box.topLeftX > self.topLeftX) and (box.BottomRightX > self.BottomRightY and box.BottomRightX < self.topLeftY))
    def translate(self, x, y):
        self.topLeftX  = self.topLeftX + x
        self.topLeftY  = self.topLeftY + x
        self.BottomRightX  = self.BottomRightX + x5
        self.BottomRightY  = self.BottomRightY + x
    def draw(self,color):
        global canvas
        box = canvas.create_rectangle(self.topLeftX, self.topLeftY, self.BottomRightX, self.BottomRightY,outline=color, fill=color)
        

class player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.health = 100
        self.combo = 100
        self.animation = 0
        self.collitionBox = collitionBox(x,y,128,320)
        self.hitBox = collitionBox(x - 128,y + 32,128,32)

class projectile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hitBox = collitionBox(x,y,64,64)

player1 = player(1000,200)
player1Projectile = projectile(800,200)
player2 = player(200,200)
player2Projectile = projectile(800,200)


timeLeft = 90

systemTime = time.time()
def tick():
    Animation.drawBackground(canvas)

    global devMode
    if(devMode):
        player1Projectile.hitBox.draw('#ff0000')
        player2Projectile.hitBox.draw('#ff0000')
        player1.collitionBox.draw('#00ff55')
        player1.hitBox.draw('#ff0000')
        player2.collitionBox.draw('#00ff55')
        player2.hitBox.draw('#ff0000')
        
    Animation.drawPlayer1(canvas,player1)
    Animation.drawPlayer2(canvas,player2)
    #Animation.drawProjectiles(canvas,projectiles)

    #GUI.drawPlayer1Health(canvas,player1)
    #GUI.drawPlayer1ComboBar(canvas,player1)
    #GUI.drawPlayer2Health(canvas,player2)
    #GUI.drawPlayer2ComboBar(canvas,player2)
    
    global systemTime
    deltaTime = time.time() - systemTime
    systemTime = systemTime + deltaTime
    
    global timeLeft
    GUI.drawTimer(canvas,round(timeLeft))
    timeLeft = timeLeft - (deltaTime)
    
    
    
    canvas.after(1, tick)
tick()

ComboManager.bindKeys(root)

# Enter event loop
root.mainloop()
