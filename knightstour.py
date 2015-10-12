class KnightsTour:
    accessBoard = []
    availBoard = []
    moveBoard = []
    currentPos =[]
    nextPos = []
    moveCount = 1
    moveRow = (-2,-1,1,2,2,1,-1,-2)
    moveCol = (1,2,2,1,-1,-2,-2,-1)
    gameOver = False

    def __init__(self, coordinate = [0,0]):
        self.currentPos =  coordinate
        self.createBoard()
        self.moveBoard[coordinate[0]][coordinate[1]] = self.moveCount
        self.availBoard[coordinate[0]][coordinate[1]] = 1
        
    def createBoard(self):
        self.availBoard = [[0]*8 for x in range(1,9,1)]
        self.moveBoard = [[0]*8 for x in range(1,9,1)]
        self.accessBoard = [[2,3,4,4,4,4,3,2],
                            [3,4,6,6,6,6,4,3],
                            [4,6,8,8,8,8,6,4],
                            [4,6,8,8,8,8,6,4],
                            [4,6,8,8,8,8,6,4],
                            [4,6,8,8,8,8,6,4],
                            [3,4,6,6,6,6,4,3],
                            [2,3,4,4,4,4,3,2]]
        

    def updateAvail(self, coordinate):
        self.availBoard[coordinate[0]][coordinate[1]] = 1
        
    def updateMoveBoard(self, coordinate):
        self.moveCount += 1
        self.moveBoard[coordinate[0]][coordinate[1]] = self.moveCount

    def updateAccess(self, coordinate = None):
        if coordinate == None:
            coordinate =  self.currentPos
        else:
            pass
        
        validMoves = self.getValidMoves(coordinate)
        for move in validMoves:
            if self.accessBoard[move[0]][move[1]] > 0:
                self.accessBoard[move[0]][move[1]] -= 1
            else:
                pass



    def getValidMoves(self, coordinate = None):
        if coordinate == None:
            coordinate = self.currentPos
        else:
            pass
        
        validMoves = []
        for item in range(8):
            potentialRow = coordinate[0]+self.moveRow[item]
            potentialCol = coordinate[1]+self.moveCol[item]
            if potentialRow in range(0,8,1) and \
               potentialCol in range(0,8,1):
                    validMoves += [potentialRow,potentialCol],
            else:
                pass

        return validMoves
        
        
    def getNextMove(self, coordinate = None):
        if coordinate == None:
            coordinate =  self.currentPos
        else:
            pass
        
        nextMove = []
        access = 9
        
        validMoves = self.getValidMoves(coordinate)
        for move in validMoves:
            if self.accessBoard[move[0]][move[1]] < access and \
               self.accessBoard[move[0]][move[1]] != 0 and\
               self.availBoard[move[0]][move[1]] != 1:
                access = self.accessBoard[move[0]][move[1]]
                nextMove = [move[0],move[1]]
            else:
                pass

            
        if not nextMove:
            print("GAME OVER - No More Moves")
            self.gameOver = True
        
        return nextMove
                    
    def makeMove(self, coordinate):
        self.updateAccess(self.currentPos)
        self.currentPos = coordinate
        self.updateAvail(self.currentPos)
        self.updateMoveBoard(coordinate)
        

    
    def runGame(self):
        while self.gameOver == False:
            nextMove = self.getNextMove()       
            self.makeMove(nextMove)

            print("CURRENT POS")
            print(self.currentPos)
            print("POSSIBLE MOVES")
            print(self.getValidMoves(self.currentPos))
            print("NEXT MOVE")
            print(self.getNextMove()) 
            self.printDetails()
            wait = input("PRESS ENTER TO CONTINUE.")
            
        



    def printDetails(self):
        print ("MOVMENT BOARD")
        for x in range(8):
            print(self.moveBoard[x])
        
        print ("ACCESS BOARD")
        for x in range(8):
            print(self.accessBoard[x])
        
        print ("AVAILABILITY BOARD")
        for x in range(8):
            print(self.availBoard[x])

    
