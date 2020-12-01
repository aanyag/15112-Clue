#executes when mouse is clicked by the user
def mousePressed(self, event):
    #stores clicks as cells on the board
    (boardRow, boardCol) = self.getBoardCell(event.x, event.y)
    #if the click is within the board, it appends that cells to the move list
    if 0 <= boardRow < self.rows and 0 <= boardCol < self.cols:
        self.player1 = (boardRow, boardCol)
        self.moveList.append((boardRow, boardCol))
    if len(self.moveList) == 2:
        self.path = self.pathfinding(self.moveList[0], self.moveList[1])
        self.moveList = []

    #if the player clicks on the buttons, the boolean for that button becomes the oppposite
    #(true to false or false to true)
    if 25 <= event.x <= 75 and (self.height - 75) <= event.y <= (self.height - 25):
        self.showInstructions = not self.showInstructions
    if 100 <= event.x <= 150 and (self.height - 75) <= event.y <= (self.height - 25):
        self.showNotepad = not self.showNotepad
    if 175 <= event.x <= 225 and (self.height - 75) <= event.y <= (self.height - 25):
        self.showAnswer = not self.showAnswer
    if 250 <= event.x <= 300 and (self.height - 75) <= event.y <= (self.height - 25):
        self.appStarted()

    #changes the dice image to a random die side when the user clicks on it
    if (self.width - 90) <= event.x <= self.width and self.height - 745 <= event.y <= self.height - 655:
        self.currDice = random.choice(self.dice)

    #changes the notebook fill colors when the user clicks on the buttons on the right-hand side
    if self.width - 80 <= event.x <= self.width - 10 and self.height - 650 <= event.y <= self.height - 580:
        self.notepadFillColor = "green"
    if self.width - 80 <= event.x <= self.width - 10 and self.height - 560 <= event.y <= self.height - 490:
        self.notepadFillColor = "red"
    
#executes at the start of the game
def timerFired(self):
    #displays an input box for the user to choose their player color
    if self.choosePlayer == True:
        color = self.getUserInput("""Pick one of the following player colors: black, white, green, blue, red, purple.\n
        Then click on one of the gray boxes to choose your starting location""")
        while color != "black" and color != "white" and color != "green" and color != "blue" and color != "red" and color != "purple":
            color = self.getUserInput("""Pick one of the following player colors: black, white, green, blue, red, purple.\n
            Then click on one of the gray boxes to choose your starting location""")
        self.playerColor = color
        self.choosePlayer = False