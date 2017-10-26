
left = 0
right = 0

def bindKeys(tk):
    #add key functions here
    def leftKey(event):
        left = 2
        print "Left key pressed"

    def rightKey(event):
        right = 2
        print "Right key pressed"
    
    tk.bind('<Left>', leftKey)
    tk.bind('<Right>', rightKey)

def tickKeys():
    #each tick subtract one from each key var if it is over 0
    if(left != 0):
        left = left - 1
    if(right != 0):
        right = right - 1

def getMovementPlayer1():
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
    return 0

def getMovementPlayer2():
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
    return 0

def getAttackPlayer1():
    #return a attack based on the attack key pressed and the direction keys that have been used resently
    return 0

def getAttackPlayer2():
    #return a attack based on the attack key pressed and the direction keys that have been used resently
    return 0
