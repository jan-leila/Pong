import Tkinter


def drawBackground(canvas):
    #draw what ever background we deside on
    canvas.create_rectangle(0,0,1920,500,fill="#ffffff")
    

def drawPlayer1(canvas,player):
    r = 128/2
    #change player one's sprite
    return{canvas.create_oval(player.x, player.y, player.x + (r*2), player.y + (r*2)),canvas.create_line(player.x + r, player.y + 128, player.x + 64, player.y + 240),canvas.create_line(player.x + 64, player.y + 240, player.x, player.y + 320),canvas.create_line(player.x + 64, player.y + 240, player.x + 128, player.y + 320),canvas.create_line(player.x + 64, player.y + 180, player.x, player.y + 120),canvas.create_line(player.x + 64, player.y + 180, player.x + 128, player.y + 120)}

def drawPlayer2(canvas,player):
    r = 128/2
    #draw player two's sprite
    return{canvas.create_oval(player.x, player.y, player.x + (r*2), player.y + (r*2)),canvas.create_line(player.x + r, player.y + 128, player.x + 64, player.y + 240),canvas.create_line(player.x + 64, player.y + 240, player.x, player.y + 320),canvas.create_line(player.x + 64, player.y + 240, player.x + 128, player.y + 320),canvas.create_line(player.x + 64, player.y + 180, player.x, player.y + 120),canvas.create_line(player.x + 64, player.y + 180, player.x + 128, player.y + 120)}

#def drawProjectiles(canvas,player1Projectile,player2Projectile):
    #draw projectiles
