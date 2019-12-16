######################################################################################
#######------------------------G A M E   E N G I N E--------------------------########
def check_winner():
    row=col=3
    for r in range(row):
        if mat[r][0]==mat[r][1]==mat[r][2]:
            return mat[r][0]
    for c in range(col):
        if mat[0][c]==mat[1][c]==mat[2][c]:
            return mat[0][c]
        
    if mat[0][0]==mat[1][1]==mat[2][2]:
        return mat[0][0]
    if mat[0][2]==mat[1][1]==mat[2][0]:
        return mat[0][2]
    return -1 #for Tie
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
def check_fill(r,c): #heck if the current position is already filled or not
    global mat
    if mat[r-1][c-1]=='_': return True
    return False
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#    
def check_valid(r,c):  #check if the current position exist or not
    if 1<=r<=3 and 1<=c<=3: return True
    return False
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
def playerX(): #controls the changes made by player X
    global mat
    r,c=getMove('X')
    while not check_valid(r,c):
        print('Invalid Coordinate! try again')
        r,c=getMove('X')
    while not check_fill(r,c):
        print("Already Filled, choose another")
        r,c=getMove('X')
        while not check_valid(r,c):
            print('Invalid Coordinate! try again')
            r,c=getMove('X')
    mat[r-1][c-1:c]=p1   # update the matrix
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
def playerO(): #controls the changes made by player O
    global mat
    r,c=getMove('O')
    while not check_valid(r,c): 
        print('Invalid Coordinate! try again')
        r,c=map(int,input("Chance: Player O -> ").split(','))
    while not check_fill(r,c):
        print("Already Filled, choose another")
        r,c=getMove('O')
        while not check_valid(r,c):
            print('Invalid Coordinate! try again')
            r,c=getMove('O')
    mat[r-1][c-1:c]=p2  # update the matrix
    
def getMove(player):
    n=int(input(f"Chance: Player {player} -> "))
    if n== 7:return 1,1
    if n== 8:return 1,2
    if n== 9:return 1,3
    if n== 4:return 2,1
    if n== 5:return 2,2
    if n== 6:return 2,3
    if n== 1:return 3,1
    if n== 2:return 3,2
    if n== 3:return 3,3
    
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
def Result(result):    ##check if someone wins or a Tie happens
    global breaker
    if result=='X':  
        print("\nPlayer X win the game\nGame End")
        breaker=1
    elif result=='O':
        print("\nPlayer O win the game\nGame End")
        breaker=1
    elif result =='_':
        return True
    elif result==-1 and ('_' not in mat[0] and '_' not in mat[1] and '_' not in mat[2]):
        print("GAME TIE")
        breaker=1
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
def PRINT(mat):
    print(*mat[0]),print(*mat[1]),print(*mat[2])
#########--------------------GAME ENGINE ENDS-------------------------############
##################################################################################
q='_'
mat=[[q,q,q],
     [q,q,q],
     [q,q,q]]
breaker=0 #To stop the game
p1='X';p2='O'
print("NOTE: The gamepad positions mimics the standard calculator mumeric keypad.")
start=input("Who will play first 'X' or 'O' ?: ")
while True:
    if start in {p1,p1.lower()} or start in {p2,p2.lower()}:
        break
    else:
        print("Invalid Character, Please choose again")
        start=input("Who will play first 'X' or 'O' ?: ")        
while True:
    if start==p1:
        PRINT(mat)
        playerX()
        PRINT(mat)
        Result(check_winner())
        if breaker==1:  #check winner will modify 'breaker'
            break
        playerO()
        Result(check_winner())   #check winner will modify 'breaker'
        if breaker==1:
            break
    else:
        PRINT(mat)
        playerO()
        PRINT(mat)
        Result(check_winner())  #check winner will modify 'breaker'
        if breaker==1:
            break
        playerX()
        Result(check_winner())  #check winner will modify 'breaker'
        if breaker==1:
            break