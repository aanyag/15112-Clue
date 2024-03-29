from cmu_112_graphics import *
import math, random
from clueAI import *

class MyApp(App):
    def appStarted(self):
        #sets rows, columns, margins, and cell specifications for the board grids
        self.rows = 25
        self.cols = 24
        self.leftMargin = 350
        self.rightMargin = 350
        self.topMargin = 75
        self.bottomMargin = 25
        self.gridWidth = self.width - self.rightMargin - self.leftMargin
        self.gridHeight = self.height - self.bottomMargin - self.topMargin
        self.cellWidth = self.gridWidth / self.cols
        self.cellHeight = self.gridHeight / self.rows

        #sets the rows for the notebook's grid
        self.suspectRows = 6
        self.weaponsRows = 6
        self.roomsRows = 9

        #sets booleans for the buttons as False, thus not appearing at the start of the game
        self.showInstructions = False
        self.showNotepad = False
        self.showAnswer = False
        self.showGuessScreen = False
        self.showAccusationScreen = False
        self.showTruth = False

        #The game board image is from https://i.pinimg.com/originals/76/a2/4f/76a24fda5952a89008dcb15ae71df4ef.jpg
        #(I edited the image a little myself before importing it)
        self.boardImage = self.loadImage('Images/gameboard.png')
        self.boardScaled = self.scaleImage(self.boardImage, 0.84)
        #The detective's notebook image from https://lh5.googleusercontent.com/proxy/iAVqoH9sg6jtlAKFF1b-N_HKaaRSX7VpmTtnLfDSs6wK6ri4NKuYYa7hdILXSQmisjjZ_uhyGhDwRK8Kp24YmlQTyLL02ij2Xctic2KrTSp8ViCYihYC=s0-d
        url2 = 'https://tinyurl.com/y53wvzq5'
        self.notepadImage = self.loadImage(url2)
        self.notepadScaled = self.scaleImage(self.notepadImage, 0.60)
        #All die side images were edited from https://image.shutterstock.com/image-vector/dice-cartoon-icons-set-traditional-260nw-1437137303.jpg
        self.die1 = self.scaleImage(self.loadImage('Images/Dice/die1.png'), 0.40)
        self.die2 = self.scaleImage(self.loadImage('Images/Dice/die2.png'), 0.40)
        self.die3 = self.scaleImage(self.loadImage('Images/Dice/die3.png'), 0.40)
        self.die4 = self.scaleImage(self.loadImage('Images/Dice/die4.png'), 0.40)
        self.die5 = self.scaleImage(self.loadImage('Images/Dice/die5.png'), 0.40)
        self.die6 = self.scaleImage(self.loadImage('Images/Dice/die6.png'), 0.40)
        self.dice = [self.die1, self.die2, self.die3, self.die4, self.die5, self.die6]
        self.currDice = self.die1
        #all images of the game cards were scanned from the physical game and then edited by me
        #room images
        self.library = self.scaleImage(self.loadImage('Images/Rooms/library.jpg'), 0.25)
        self.diningRoom = self.scaleImage(self.loadImage('Images/Rooms/diningRoom.jpg'), 0.25)
        self.lounge = self.scaleImage(self.loadImage('Images/Rooms/lounge.jpg'), 0.25)
        self.ballroom = self.scaleImage(self.loadImage('Images/Rooms/ballroom.jpg'), 0.25)
        self.billiardRoom = self.scaleImage(self.loadImage('Images/Rooms/billiardRoom.jpg'), 0.25)
        self.hall = self.scaleImage(self.loadImage('Images/Rooms/hall.jpg'), 0.25)
        self.kitchen = self.scaleImage(self.loadImage('Images/Rooms/kitchen.jpg'), 0.25)
        self.conservatory = self.scaleImage(self.loadImage('Images/Rooms/conservatory.jpg'), 0.25)
        self.study = self.scaleImage(self.loadImage('Images/Rooms/study.jpg'), 0.25)
        #weapons images
        self.candlestick = self.scaleImage(self.loadImage('Images/Weapons/candlestick.jpg'), 0.25)
        self.revolver = self.scaleImage(self.loadImage('Images/Weapons/revolver.jpg'), 0.25)
        self.leadPipe = self.scaleImage(self.loadImage('Images/Weapons/leadPipe.jpg'), 0.25)
        self.rope = self.scaleImage(self.loadImage('Images/Weapons/rope.jpg'), 0.25)
        self.knife = self.scaleImage(self.loadImage('Images/Weapons/knife.jpg'), 0.25)
        self.wrench = self.scaleImage(self.loadImage('Images/Weapons/wrench.jpg'), 0.25)
        #suspects images
        self.white = self.scaleImage(self.loadImage('Images/Suspects/white.jpg'), 0.25)
        self.green = self.scaleImage(self.loadImage('Images/Suspects/green.jpg'), 0.25)
        self.peacock = self.scaleImage(self.loadImage('Images/Suspects/peacock.jpg'), 0.25)
        self.scarlet = self.scaleImage(self.loadImage('Images/Suspects/scarlet.jpg'), 0.25)
        self.mustard = self.scaleImage(self.loadImage('Images/Suspects/mustard.jpg'), 0.25)
        self.plum = self.scaleImage(self.loadImage('Images/Suspects/plum.jpg'), 0.25)
        self.allCardsDict = {'suspects': [self.white, self.green, self.peacock, self.scarlet, self.mustard, self.plum],
                        'weapons': [self.candlestick, self.revolver, self.leadPipe, self.rope, self.knife, self.wrench],
                        'rooms': [self.library, self.diningRoom, self.lounge, self.ballroom, self.billiardRoom,
                                self.hall, self.kitchen, self.conservatory, self.study]}
        self.allCardsList = [self.white, self.green, self.peacock, self.scarlet, self.mustard, self.plum, 
                            self.candlestick, self.revolver, self.leadPipe, self.rope, self.knife, self.wrench,
                            self.library, self.diningRoom, self.lounge, self.ballroom, self.billiardRoom,
                            self.hall, self.kitchen, self.conservatory, self.study]
        self.playerCards = random.sample(self.allCardsList, 9)

        #setting initial board and player values
        self.playerColor = "black"
        self.choosePlayer = True
        self.notepadFillColor = "green"
        self.startingColor = "grey"
        self.player1 = (-1, -1)
        self.player1end = (-1, -1)
        self.moveList = []
        self.fillColor = ""
        #sets all rooms as grey on the grid
        self.roomColor = "grey"
        self.roomsList = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),
                (0,17),(0,18),(0,19),(0,20),(0,21),(0,22),(0,23),
                (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),
                (1,17),(1,18),(1,19),(1,20),(1,21),(1,22),(1,23),
                (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,9),(2,10),(2,11),(2,12),(2,13),(2,14),
                (2,17),(2,18),(2,19),(2,20),(2,21),(2,22),(2,23),
                (3,1),(3,2),(3,3),(3,4),(3,5),(3,9),(3,10),(3,11),(3,12),(3,13),(3,14),(3,17),(3,18),(3,19),(3,20),(3,21),(3,22),(3,23),
                (4,10),(4,11),(4,12),(4,13),(4,14),(4,17),(4,18),(4,19),(4,20),(4,21),(4,22),(4,23),
                (5,9),(5,10),(5,11),(5,12),(5,13),(5,14),(5,18),(5,19),(5,20),(5,21),(5,22),
                (6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,9),(6,10),(6,13),(6,14),
                (7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),
                (8,0),(8,1),(8,2),(8,3),(8,4),(8,5),
                (9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,16),(9,18),(9,19),(9,20),(9,21),(9,22),(9,23),
                (10,1),(10,2),(10,4),(10,5),(10,16),(10,17),(10,18),(10,19),(10,20),(10,21),(10,22),(10,23),
                (11,16),(11,17),(11,18),(11,19),(11,20),(11,21),(11,22),(11,23),
                (12,0),(12,2),(12,3),(12,4),(12,5),(12,17),(12,18),(12,19),(12,20),(12,21),(12,22),(12,23),
                (13,0),(13,1),(13,2),(13,3),(13,4),(13,5),(13,16),(13,17),(13,18),(13,19),(13,20),(13,21),(13,22),(13,23),
                (14,0),(14,1),(14,2),(14,3),(14,4),(14,5),(14,16),(14,17),(14,18),(14,19),(14,20),(14,21),(14,22),(14,23),
                (15,0),(15,1),(15,2),(15,3),(15,4),(15,19),(15,20),(15,21),(15,22),(15,23),
                (16,0),(16,1),(16,2),(16,3),(16,4),(16,5),
                (17,8),(17,10),(17,11),(17,12),(17,13),(17,15),
                (18,8),(18,9),(18,10),(18,11),(18,12),(18,13),(18,14),(18,15),(18,18),(18,20),(18,21),(18,22),(18,23),
                (19,2),(19,3),(19,9),(19,10),(19,11),(19,12),(19,13),(19,14),(19,18),(19,19),(19,20),(19,21),(19,22),(19,23),
                (20,0),(20,1),(20,2),(20,3),(20,4),(20,5),(20,8),(20,9),(20,10),(20,11),(20,12),(20,13),(20,14),(20,15),
                (20,18),(20,19),(20,20),(20,21),(20,22),(20,23),
                (21,0),(21,1),(21,2),(21,3),(21,4),(21,5),(21,8),(21,9),(21,10),(21,11),(21,12),(21,13),(21,14),(21,15),
                (21,18),(21,19),(21,20),(21,21),(21,22),(21,23),
                (22,0),(22,1),(22,2),(22,3),(22,4),(22,5),(22,8),(22,9),(22,10),(22,11),(22,12),(22,13),(22,14),(22,15),
                (22,18),(22,19),(22,20),(22,21),(22,22),(22,23),
                (23,0),(23,1),(23,2),(23,3),(23,4),(23,5),(23,10),(23,11),(23,12),(23,13),(23,19),(23,20),(23,21),(23,22),(23,23),
                (24,0),(24,1),(24,2),(24,3),(24,4),(24,5),(24,10),(24,11),(24,12),(24,13),(24,18),(24,19),(24,20),(24,21),(24,22),(24,23)]
        #sets all doors as pink on the grid
        self.doorColor = "pink"
        self.doorsList = [(3,6),(4,9),(5,17),(6,11),(6,12),(8,6),(9,17),(10,3),
                        (12,1),(12,16),(15,5),(17,9),(17,14),(18,19),(19,4),(19,8),(19,15)]
        #sets stairs as orange and cyan
        self.stair1color = "orange"
        self.stair1list = [(3,0),(23,18)]
        self.stair2color = "cyan"
        self.stair2list = [(5,23),(19,1)]
        #sets the center room as magenta
        self.centerRoomColor = "magenta"
        self.centerRoomList = [(8,9),(8,10),(8,11),(8,12),(8,13),
                            (9,9),(9,10),(9,11),(9,12),(9,13),
                            (10,9),(10,10),(10,11),(10,12),(10,13),
                            (11,9),(11,10),(11,11),(11,12),(11,13),
                            (12,9),(12,10),(12,11),(12,12),(12,13),
                            (13,9),(13,10),(13,11),(13,12),(13,13),
                            (14,9),(14,10),(14,11),(14,12),(14,13)]
        #sets the empty list for the path the player must take to reach its destination
        self.path = []
        #list containing the final answer
        self.answer = []
        self.guess = []
        self.playerTurn = True

        self.AI = ClueAI()

    #executes when mouse is clicked by the user
    def mousePressed(self, event):
        self.computerChoices()
        #stores clicks as cells on the board
        (boardRow, boardCol) = self.getBoardCell(event.x, event.y)
        #if the click is within the board, it appends that cells to the move list
        if 0 <= boardRow < self.rows and 0 <= boardCol < self.cols:
            self.player1 = (boardRow, boardCol)
            self.moveList.append((boardRow, boardCol))
        if len(self.moveList) == 2:
            self.path = self.pathfinding(self.moveList[0], self.moveList[1])
            self.moveList.pop(0)

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

        #click to make a guess or accusation
        if self.width - 80 <= event.x <= self.width - 10 and self.height - 470 <= event.y <= self.height - 400:
            self.showGuessScreen = not self.showGuessScreen
        if self.width - 200 <= event.x <= self.width - 50 and 50 <= event.y <= 100:
            self.showGuessScreen = False
            self.showTruth = not self.showTruth
        if self.width - 80 <= event.x <= self.width - 10 and self.height - 380 <= event.y <= self.height - 310:
            self.showAccusationScreen = not self.showAccusationScreen

        #clicking on a suspect when guessing


    #executes at the start of the game
    def timerFired(self):
        #displays an input box for the user to choose their player color and selects the game answer
        if self.choosePlayer == True:
            color = self.getUserInput("""Pick one of the following player colors: black, white, green, blue, red, purple.\n
            Then click on one of the gray boxes to choose your starting location""")
            while color != "black" and color != "white" and color != "green" and color != "blue" and color != "red" and color != "purple":
                color = self.getUserInput("""Pick one of the following player colors: black, white, green, blue, red, purple.\n
                Then click on one of the gray boxes to choose your starting location""")
            self.playerColor = color
            self.choosePlayer = False
            self.answer = self.setAnswer()
            
    #draws the title on the top of the screen
    def drawTitle(self, canvas):
        canvas.create_text(self.width / 2, self.topMargin / 2.5,
                        text = "CLUE!", font = "Arial 20 bold")

    #draws buttons on the screen for instructions, notepad, answer, reset, correct, and wrong
    def drawButtons(self, canvas):
        canvas.create_oval(25, self.height - 75, 75, self.height - 25, 
                                fill = "pink")
        canvas.create_text(50, self.height - 50, text = "HELP",
                                font = "Arial 15 bold")
        canvas.create_oval(100, self.height - 75, 150, self.height - 25, 
                                fill = "light blue")
        canvas.create_text(125, self.height - 50, text = "NOTEPAD",
                                font = "Arial 9 bold")
        canvas.create_oval(175, self.height - 75, 225, self.height - 25, 
                                fill = "light green")
        canvas.create_text(200, self.height - 50, text = "ANSWER",
                                font = "Arial 11 bold")
        canvas.create_oval(250, self.height - 75, 300, self.height - 25, 
                                fill = "purple")
        canvas.create_text(275, self.height - 50, text = "RESET",
                                font = "Arial 14 bold")

        canvas.create_oval(self.width - 80, self.height - 650, self.width - 10, self.height - 580, 
                                fill = "green")
        canvas.create_text(self.width - 45, self.height - 615, text = "CORRECT",
                                font = "Arial 13 bold")
        canvas.create_oval(self.width - 80, self.height - 560, self.width - 10, self.height - 490, 
                                fill = "red")
        canvas.create_text(self.width - 45, self.height - 525, text = "WRONG",
                                font = "Arial 14 bold")
        canvas.create_oval(self.width - 80, self.height - 470, self.width - 10, self.height - 400, 
                                fill = "orange")
        canvas.create_text(self.width - 45, self.height - 435, text = "GUESS",
                                font = "Arial 13 bold")
        canvas.create_oval(self.width - 80, self.height - 380, self.width - 10, self.height - 310, 
                                fill = "blue")
        canvas.create_text(self.width - 45, self.height - 345, text = "ACCUSE",
                                font = "Arial 14 bold")

    #this is the screen to make a guess after every turn
    def makeGuessScreen(self, canvas):
        if self.showGuessScreen:
            canvas.create_rectangle(25, 25, self.width - 25, self.height - 25,
                                            fill = "orange")
            canvas.create_text(self.width / 2, 75, text = "Make a Guess!",
                                            font = "Arial 30 bold")
            canvas.create_text(self.width / 2, 115, text = "Pick One Suspect!",
                                            font = "Arial 30 bold")
            canvas.create_text(self.width / 2, 450, text = "Pick One Weapon!",
                                            font = "Arial 30 bold")
            canvas.create_rectangle(self.width - 200, 50, self.width - 50, 100,
                                            fill = "red")
            canvas.create_text(self.width - 125, 75, text = "Submit Guess!",
                                            font = "Arial 18 bold")
            location = 200
            for suspect in self.allCardsDict['suspects']:
                canvas.create_image(location, 275, image = ImageTk.PhotoImage(suspect))
                location += 200
            location = 200
            for weapon in self.allCardsDict['weapons']:
                canvas.create_image(location, 615, image = ImageTk.PhotoImage(weapon))
                location += 200

    def drawAccusationScreen(self, canvas):
        if self.showAccusationScreen:
            canvas.create_rectangle(25, 25, self.width - 25, self.height - 25,
                                            fill = "blue")
            canvas.create_text(self.width / 2, 75, text = "Make Your Accusation!",
                                            font = "Arial 30 bold")

    #displays instructions when "HELP" button is clicked
    def instructions(self, canvas):
        if self.showInstructions:
            canvas.create_rectangle(100, 100, self.width - 100, self.height - 100,
                                        fill = "pink")
            canvas.create_text(self.width / 2, 125, text = "Instructions!",
                                        font = "Arial 30 bold")
            canvas.create_text(self.width/2, self.height/2, text = """\
                    The object of the game is to determine the killer, the murder weapon, and the room in which the murder occurred.\n
                    Step 1: Take turns rolling the die to choose who goes first- the highest number goes first and then you go 
                    counterclockwise from there.\n
                    Step 2: Roll the die to determine the number of spaces you can move. 
                    You may not move diagonally and can only enter a room through spaces that have doors.
                    Once you have entered a room, you cannot move any further on the same turn. 
                    If the room you are currently in has a secret passage, you may move through the secret passage to the next room instead of rolling the die on your turn.\n
                    Step 3: When you enter a room, you can, but do not have to, make a suggestion for who you think is the killer and their murder weapon. 
                    The room that you suggest must be the current room you are in.\n
                    Step 4: After a suggestion is made, each of the other players will try to prove your suggestion to be false. 
                    They will look at their cards for one of the three accusations you made and if they have one of them, they will tell you which card.\n
                    Step 5: If you believe that you have solved the killer, the murder weapon, and the room in which the murder occurred, you must enter the center room on the board.
                    There you will make an accusation and will be told if you were right or wrong. If you were right, you win the game but either way the game ends at this point.""",
                    font = "Arial 15 bold")

    #returns the row and column of a certain x,y coordinate
    def getBoardCell(self, x, y):
        row = int((y - self.topMargin) / self.cellHeight)
        col = int((x - self.leftMargin) / self.cellWidth)
        return (row, col)

    #returns the bounds for each singular cell
    #depends on margins, height and width of the canvas, and total rows and columns
    def getCellBounds(self, row, col):
        x1 = self.leftMargin + col * self.cellWidth
        y1 = self.topMargin + row * self.cellHeight
        x2 = x1 + self.cellWidth
        y2 = y1 + self.cellHeight
        return x1, y1, x2, y2

    #draws the board grid
    def drawBoardGrid(self, canvas):
        for row in range(self.rows):
            for col in range(self.cols):
                x1, y1, x2, y2 = self.getCellBounds(row, col)
                #the path taken by the user is displayed as green
                if (row, col) in self.path:
                    canvas.create_rectangle(x1, y1, x2, y2, fill = "green")
                elif self.player1 == (row, col) or self.player1end == (row, col):
                    self.fillColor = self.playerColor
                else:
                    self.fillColor = ""
                canvas.create_rectangle(x1, y1, x2, y2, fill = self.fillColor)

    #draws the algorithmic grid that displays the pathfinding
    def drawAlgorithmicBoard(self, canvas):
        for row in range(self.rows):
            for col in range(self.cols):
                x1, y1, x2, y2 = self.getCellBounds(row, col)
                #rooms, doors, stairs, and the center room must be their own colors
                if (row,col) in self.roomsList:
                    canvas.create_rectangle(x1, y1, x2, y2, fill = self.roomColor)
                elif (row,col) in self.doorsList:
                    canvas.create_rectangle(x1, y1, x2, y2, fill = self.doorColor)
                elif (row,col) in self.stair1list:
                    canvas.create_rectangle(x1, y1, x2, y2, fill = self.stair1color)
                elif (row,col) in self.stair2list:
                    canvas.create_rectangle(x1, y1, x2, y2, fill = self.stair2color)
                elif (row,col) in self.centerRoomList:
                    canvas.create_rectangle(x1, y1, x2, y2, fill = self.centerRoomColor)
                canvas.create_rectangle(x1, y1, x2, y2)

    #draws the notepad's grid so the user can fill in green and red
    def drawNotepadGrid(self, canvas):
        for row in range(self.suspectRows):
            canvas.create_rectangle(1275, 75 + 18.5 * row, 1290, 93.5 + 18.5 * row)
        for row in range(self.weaponsRows):
            canvas.create_rectangle(1274, 232 + 18.5 * row, 1289, 250.5 + 18.5 * row)
        for row in range(self.roomsRows):
            canvas.create_rectangle(1274, 479 + 18.75 * row, 1289, 497.75 + 18.75 * row)

    #choose an answer at random from all the given cards
    def setAnswer(self):
        suspect = random.choice(self.allCardsDict['suspects'])
        weapon = random.choice(self.allCardsDict['weapons'])
        room = random.choice(self.allCardsDict['rooms'])
        self.answer += [suspect, weapon, room]
        return self.answer
    
    def drawAnswer(self, canvas):
        if self.showAnswer:
            canvas.create_rectangle(100, 100, self.width - 100, self.height - 100,
                                        fill = "light green")
            canvas.create_text(self.width / 2, 200, text = "Answer!",
                                        font = "Arial 30 bold")
            location = 400
            for answer in self.answer:
                canvas.create_image(location, self.height/2, 
                            image = ImageTk.PhotoImage(answer))
                location += 320

    def drawPlayerCards(self, canvas):
        for card in self.playerCards:
            canvas.create_image(100, 150, image = ImageTk.PhotoImage(card))

    def computerCards(self):
        computerCards = self.allCardsList
        for card in self.playerCards:
            if card in computerCards:
                computerCards.remove(card)

    def computerChoices(self):
        self.AI.computerChoices = self.playerCards + self.answer
        self.AI.test()
        # computerChoices = self.playerCards
        # computerChoices += self.answer


    #draws the grid, title, buttons, instructions, notepad, dice, and board
    def redrawAll(self, canvas):
        self.drawAlgorithmicBoard(canvas)
        canvas.create_image(self.width / 2, self.height - 373,
                                image = ImageTk.PhotoImage(self.boardScaled))
        canvas.create_image(self.width - 200, self.height / 2,
                                image = ImageTk.PhotoImage(self.notepadScaled))
        canvas.create_image(self.width - 45, self.height - 700,
                                image = ImageTk.PhotoImage(self.currDice))
        self.drawPlayerCards(canvas)
        self.drawNotepadGrid(canvas)
        self.drawBoardGrid(canvas)
        self.drawTitle(canvas)
        self.drawButtons(canvas)
        self.instructions(canvas)
        self.makeGuessScreen(canvas)
        self.drawAnswer(canvas)
        self.drawAccusationScreen(canvas)

    #I used this website (https://www.raywenderlich.com/3016-introduction-to-a-pathfinding)
    #only to learn how the A* algorithm, however I wrote all of the following code myself
    def pathfinding(self, start, end):
        #finds the shortest path from the user's position to where they wish to go
        openList = [start]
        scoreList = [0]
        closedList = []
        gScore = 0
        parentDict = {}
        #will keep running until the end location is in the final path list or 
        #there are no more possible squares
        while True:
            #finds the square with the lowest f-score
            minScore = min(scoreList)
            minIndex = len(scoreList) - 1 - scoreList[::-1].index(minScore)
            currSquare = openList[minIndex]
            closedList += [currSquare]
            openList.pop(minIndex)
            scoreList.pop(minIndex)

            #break out of the loop if the end destination is in the closed list
            if end in closedList:
                break

            #find all eligible squares adjacent to the current location
            adjacentSquares = []
            (row, col) = currSquare
            for direction in [(-1,0), (0,-1), (1,0), (0,+1)]:
                (newRow, newCol) = (row + direction[0], col + direction[1])
                #square must be in the grid, and not a room, stair, or in the center room
                if (newRow >= self.rows or newRow < 0 or newCol >= self.cols or newCol < 0 or 
                    (newRow, newCol) in self.roomsList or (newRow, newCol) in self.stair1list or 
                    (newRow, newCol) in self.stair2list or (newRow, newCol) in self.centerRoomList):
                    pass
                else:
                    adjacentSquares.append((newRow, newCol))
                    
            gScore += 1
            
            #for all adjacent squares, find the f-score
            for item in adjacentSquares:
                if item in closedList:
                    continue
                hScore = abs(end[0] - item[0]) + abs(end[1] - item[1])
                fScore = gScore + hScore
                #add square to the open list
                if item not in openList:
                    parentDict[item] = currSquare
                    openList += [item]
                    scoreList += [fScore]
                #if already in the open list, update list if new f-score is lower than old f-score
                else:
                    itemIndex = openList.index(item)
                    oldFScore = scoreList[itemIndex]
                    if fScore < oldFScore:
                        openList.remove(item)
                        scoreList.pop(itemIndex)
                        parentDict[item] = currSquare
                        openList += [item]
                        scoreList += [fScore]

            #if the open list is empty, there is no path
            if (openList == []):
                break
        
        #determine the shortest path by traversing the parent dictionary backwards
        path = [end]
        currParent = parentDict[end]
        currPoint = end
        while currParent != start:
            path += [currParent]
            currPoint = currParent
            currParent = parentDict[currPoint]
        path += [start]
        return path

def main():
    MyApp(width=1440, height=801)

if __name__ == '__main__':
    main()