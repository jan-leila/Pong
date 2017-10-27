left = 0
right = 0
up = 0
down = 0

a = 0
w = 0
s = 0
d = 0

def bindKeys(tk):
    #add key functions here
    def leftKey(event):
        global left
        left = 1
        print "Left key pressed"

    def rightKey(event):
        global right
        right = 1
        print "Right key pressed"
        
    def upKey(event):
        global up
        up = 1
        print "Up Key pressed"
        
    def downKey(event):
        global down
        down = 1
        print "Down Key pressed"

    def leftKeyR(event):
        global left
        left = 0
        print "Left key Release"

    def rightKeyR(event):
        global right
        right = 0
        print "Right key Release"
        
    def upKeyR(event):
        global up
        up = 0
        print "Up Key Release"
        
    def downKeyR(event):
        global down
        down = 0
        print "Down Key Release"
    
    
    
    def aKey(event):
        global a
        a = 1
        print "A key pressed"

    def dKey(event):
        global d
        d = 1
        print "D key pressed"
        
    def wKey(event):
        global w
        w = 1
        print "W Key pressed"
        
    def sKey(event):
        global s
        s = 1
        print "S Key pressed"
        
    def aKeyR(event):
        global a
        a = 0
        print "A key Release"

    def dKeyR(event):
        global d
        d = 0
        print "D key Release"
        
    def wKeyR(event):
        global w
        w = 0
        print "W Key Release"
        
    def sKeyR(event):
        global s
        s = 0
        print "S Key Release"
        
    tk.bind('<KeyPress-Left>', leftKey)
    tk.bind('<KeyPress-Right>', rightKey)
    tk.bind('<KeyPress-Up>', upKey)
    tk.bind('<KeyPress-Down>', downKey)
    tk.bind('<KeyRelease-Left>', leftKeyR)
    tk.bind('<KeyRelease-Right>', rightKeyR)
    tk.bind('<KeyRelease-Up>', upKeyR)
    tk.bind('<KeyRelease-Down>', downKeyR)
    
    tk.bind('<KeyPress-w>', wKey)
    tk.bind('<KeyPress-a>', aKey)
    tk.bind('<KeyPress-s>', sKey)
    tk.bind('<KeyPress-d>', dKey)
    tk.bind('<KeyRelease-w>', wKeyR)
    tk.bind('<KeyRelease-a>', aKeyR)
    tk.bind('<KeyRelease-s>', sKeyR)
    tk.bind('<KeyRelease-d>', dKeyR)

def getMovementPlayer1(player):
    global left
    global right
    global down
    global up
    # Chart of numbers
    #
    #     4    3    2
    #
    #       \  |  /
    #
    #   5   -  0  - 1
    #
    #       /  |  \
    #
    #     6    7    8
    
    # Make this return the direction the player will be moving based on the left, right, up and down key values
    horizontal = 0
    vertical = 0
    if (left != 0 and right == 0):
        horizontal = -1
    elif (left == 0 and right !=0):
        horizontal = 1
    if (up != 0 and down == 0):
        vertical = -1
    elif (up ==0 and down !=0):
        vertical = 1
    player.move(horizontal,vertical)
    return player

def getMovementPlayer2(player):
    global w
    global a
    global s
    global d
    # Chart of numbers
    #
    #     4    3    2
    #
    #       \  |  /
    #
    #   5   -  0  - 1
    #
    #       /  |  \
    #
    #     6    7    8
    
    # Make this return the direction the player will be moving based on the a, d, w and s key values
    horizontal = 0
    vertical = 0
    print s
    if a != 0 and d == 0:
        horizontal = -1
    elif a == 0 and d !=0:
        horizontal = 1
    if w != 0 and s == 0:
        vertical = -1
    elif w ==0 and s !=0:
        vertical = 1
    player.move(horizontal,vertical)
    return player  

def getAttackPlayer1():
    #return a attack based on the attack key pressed and the direction keys that have been used resently
    return 0

def getAttackPlayer2():
    #return a attack based on the attack key pressed and the direction keys that have been used resently
    return 0
