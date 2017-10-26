import Tkinter


def drawBackground(canvas):
    #draw what ever background we deside on
    canvas.create_rectangle(0,0,1920,500,fill="#ffffff")
    

def drawPlayer1(canvas,player):
    #change player one's sprite
    player.updateSprite({canvas.create_arc(player.x, player.y, player.x, player.y + 320)})
    print ""

def drawPlayer2(canvas,player):
    #draw player two's sprite
    canvas.create_arc(player.x, player.y, player.x, player.y + 320)

#def drawProjectiles(canvas,player1Projectile,player2Projectile):
    #draw projectiles
