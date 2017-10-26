
def Player(player1,player2,Projectile):
    if(player1.collitionBox.testCollition(player2.hitBox)):
        player1.health = player1.health - 3
    return player1

def Projectile(projectile):
    return projectile
