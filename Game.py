import Tkinter
import time
import Animation
import ComboManager
import Physics
import GUI

devMode = True

# Create the main window
root = Tkinter.Tk()
root.wm_title('')
# create canvas
canvas = Tkinter.Canvas(root, height=500, width=1920, background='#FFFFFF')
canvas.grid(row=0, column=1, rowspan=3)

class collitionBox:
    def __init__(self,topLeftX,topLeftY,width,height,color):
        self.topLeftX  = topLeftX
        self.topLeftY  = topLeftY
        self.BottomRightX  = topLeftX + width
        self.BottomRightY  = topLeftY + height
        global devMode
        if(devMode):
            self.box = canvas.create_rectangle(self.topLeftX, self.topLeftY, self.BottomRightX, self.BottomRightY,outline=color, fill=color)
    def testCollition(self, box):
        return ((self.topLeftX < box.BottomRightX and self.topLeftX > box.topLeftX) and (self.topLeftY > box.BottomRightY and self.topLeftY < box.topLeftY) or (self.BottomRightX < box.BottomRightX and self.BottomRightX > box.topLeftX) and (self.topLeftY > box.BottomRightY and self.topLeftY < box.topLeftY) or (self.BottomRightX < box.BottomRightX and self.BottomRightX > box.topLeftX) and (self.BottomRightX > box.BottomRightY or self.BottomRightX < box.topLeftY) or (self.topLeftX < box.BottomRightX and self.topLeftX > box.topLeftX) and (self.BottomRightX > box.BottomRightY and self.BottomRightX < box.topLeftY) or (box.topLeftX < self.BottomRightX and box.topLeftX > self.topLeftX) and (box.topLeftY > self.BottomRightY and box.topLeftY < self.topLeftY) or (box.BottomRightX < self.BottomRightX and box.BottomRightX > self.topLeftX) and (box.topLeftY > self.BottomRightY and box.topLeftY < self.topLeftY) or (box.BottomRightX < self.BottomRightX and box.BottomRightX > self.topLeftX) and (box.BottomRightX > self.BottomRightY and box.BottomRightX < self.topLeftY) or (box.topLeftX < self.BottomRightX and box.topLeftX > self.topLeftX) and (box.BottomRightX > self.BottomRightY and box.BottomRightX < self.topLeftY))
    def translate(self, x, y):
        self.topLeftX  = self.topLeftX + x
        self.topLeftY  = self.topLeftY + y
        self.BottomRightX  = self.BottomRightX + x
        self.BottomRightY  = self.BottomRightY + y
        global devMode
        if(devMode):
            canvas.move(self.box, x,y)

class player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.health = 100
        self.combo = 100
        self.animation = 0
        self.collitionBox = collitionBox(x,y,128,320,'#00ff55')
        self.hitBox = collitionBox(x - 128,y + 32,128,32,'#ff0000')
        self.sprite = [11]
        for line in self.sprite:
            line = self.sprite[0] = canvas.create_arc(self.x, self.y, self.x, self.y + 320)
    def move(self,x,y):
        self.x = self.x + x
        self.y = self.y + y
        self.collitionBox.translate(x,y)
        self.hitBox.translate(x,y)
        for line in self.sprite:
            canvas.move(line, x,y)
    def updateSprite(self,newSprite):
        global canvas
        for line in self.sprite:
            canvas.delete(line)
        self.sprite = newSprite

class projectile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hitBox = collitionBox(x,y,64,64,'#ff0000')

Animation.drawBackground(canvas)

player1 = player(200,200)
player1Projectile = projectile(800,200)
player2 = player(1000,200)
player2Projectile = projectile(800,200)

player1HealthBar = canvas.create_rectangle(500 - player1.health * 5, 0, 500, 25,outline='#ff0000', fill='#ff0000')
player2HealthBar = canvas.create_rectangle(500 - player2.health * 5, 0, 500, 25,outline='#ff0000', fill='#ff0000')


timeLeft = 90

timmer = canvas.create_text(640,15,text=str(timeLeft))

systemTime = time.time()
def tick():
    global player1, player2, player1Projectile, player2Projectile
        
    player1.updateSprite(Animation.drawPlayer1(canvas,player1))
    player2.updateSprite(Animation.drawPlayer2(canvas,player2))
    #Animation.drawProjectiles(canvas,projectiles)

    player1 = ComboManager.getMovementPlayer1(player1)
    player2 = ComboManager.getMovementPlayer2(player2)
    
    player1 = Physics.Player(player1,player2,player2Projectile)
    player2 = Physics.Player(player2,player1,player1Projectile)
    
    canvas.coords(player1HealthBar, 625 - player1.health * 5, 0, 625, 25)
    canvas.coords(player2HealthBar, 655 + player2.health * 5, 0, 655, 25)
    
    global systemTime
    deltaTime = time.time() - systemTime
    systemTime = systemTime + deltaTime
    
    global timeLeft
    canvas.itemconfig(timmer, text=str(round(timeLeft)))
    #GUI.drawTimer(canvas,round(timeLeft))
    timeLeft = timeLeft - (deltaTime)

    if(player1.health > 0 and player2.health > 0 ):
        canvas.after(1, tick)
    else:
        if(player1.health > 0):
            canvas.create_text(640,250,text="Player1 Won")
        else:
            canvas.create_text(640,250,text="Player2 Won")
tick()

ComboManager.bindKeys(root)

# Enter event loop
root.mainloop()
