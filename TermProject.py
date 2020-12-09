from cmu_112_graphics import *
import math, random, copy

#OVERALL CITATIONS:
#cmu_112_graphics and its methods were used for this program, learned from the animations notes on the 112 website
#downloaded the cmu_112_graphics file from https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#ioMethods
#learned the App Class from https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#ioMethods
#the font "Arial", font sizes, and fill colors were learned from https://www.cs.cmu.edu/~112/notes/notes-graphics.html
#all random functions were learned from https://docs.python.org/3/library/random.html

class MyApp(App):
    def appStarted(self):
        #sets rows, columns, margins, and cell specifications for the board grids
        self.rows = 25
        self.cols = 24
        self.leftMargin = 345
        self.rightMargin = 345
        self.topMargin = 62
        self.bottomMargin = 23
        self.gridWidth = self.width - self.rightMargin - self.leftMargin
        self.gridHeight = self.height - self.bottomMargin - self.topMargin
        self.cellWidth = self.gridWidth / self.cols
        self.cellHeight = self.gridHeight / self.rows

        #sets the rows, cols, and margins for the notebook's grid
        self.notebookCols = 1
        self.suspectRows = 6
        self.weaponRows = 6
        self.roomRows = 9
        self.nbLeftMargin = 1264
        self.nbRightMargin = 104
        self.suspectTopMargin = 68
        self.suspectBottomMargin = 610
        self.weaponTopMargin = 226
        self.weaponBottomMargin = 452
        self.roomTopMargin = 473
        self.roomBottomMargin = 149
        self.nbSuspectDict = {}
        self.nbWeaponDict = {}
        self.nbRoomDict = {}
        self.nbGridWidth = self.width - self.nbRightMargin - self.nbLeftMargin
        self.nbCellWidth = self.nbGridWidth / self.notebookCols
        self.suspectGridHeight = self.height - self.suspectBottomMargin - self.suspectTopMargin
        self.suspectCellHeight = self.suspectGridHeight / self.suspectRows
        self.weaponGridHeight = self.height - self.weaponBottomMargin - self.weaponTopMargin
        self.weaponCellHeight = self.weaponGridHeight / self.weaponRows
        self.roomGridHeight = self.height - self.roomBottomMargin - self.roomTopMargin
        self.roomCellHeight = self.roomGridHeight / self.roomRows

        #sets booleans for the buttons and game states at the beginning of the game
        self.showInstructions = False
        self.showPlayerCards = False
        self.showAnswer = False
        self.showGuessScreen = False
        self.showAccusationScreen1 = False
        self.showAccusationScreen2 = False
        self.showTruth = False
        self.showRoomLayoutScreen = True
        self.gameStart = False
        self.gameOver = False

        #CITATIONS: all image functions were learned during the optional lecture notes "Optional: Images with PIL + Using the App Class"
        #the clue logo image is from https://i.pinimg.com/originals/64/98/8e/64988ea34c1135dec17c0780e5434caa.jpg
        self.clueLogo = self.loadImage('Images/clueLogo.png')
        self.clueLogoScale = self.scaleImage(self.clueLogo, 0.45)
        #The game board image is from https://i.pinimg.com/originals/76/a2/4f/76a24fda5952a89008dcb15ae71df4ef.jpg
        #(I edited the image a little myself before importing it)
        self.boardImage = self.loadImage('Images/gameboard without names.png')
        self.boardScaled = self.scaleImage(self.boardImage, 0.84)
        self.changeBoardScaled = self.scaleImage(self.boardImage, 0.6)
        #The detective's notebook image from https://lh5.googleusercontent.com/proxy/iAVqoH9sg6jtlAKFF1b-N_HKaaRSX7VpmTtnLfDSs6wK6ri4NKuYYa7hdILXSQmisjjZ_uhyGhDwRK8Kp24YmlQTyLL02ij2Xctic2KrTSp8ViCYihYC=s0-d
        url2 = 'https://tinyurl.com/y53wvzq5'
        self.notebookImage = self.loadImage(url2)
        self.notebookScaled = self.scaleImage(self.notebookImage, 0.60)
        #All die side images were edited from https://image.shutterstock.com/image-vector/dice-cartoon-icons-set-traditional-260nw-1437137303.jpg
        self.diceDict = {1: self.scaleImage(self.loadImage('Images/Dice/die1.png'), 0.40),
                        2: self.scaleImage(self.loadImage('Images/Dice/die2.png'), 0.40),
                        3: self.scaleImage(self.loadImage('Images/Dice/die3.png'), 0.40),
                        4: self.scaleImage(self.loadImage('Images/Dice/die4.png'), 0.40),
                        5: self.scaleImage(self.loadImage('Images/Dice/die5.png'), 0.40),
                        6: self.scaleImage(self.loadImage('Images/Dice/die6.png'), 0.40)}
        self.currDice = self.diceDict[1]
        self.currDiceValue = 1
        self.playerRollDice = 0
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
        self.roomImages = {'library': self.library, 'dining room': self.diningRoom, 'lounge': self.lounge,
            'ballroom': self.ballroom, 'billiard room': self.billiardRoom, 'hall': self.hall,
            'kitchen': self.kitchen, 'conservatory': self.conservatory, 'study': self.study}
        self.rooms = {'library', 'dining room', 'lounge', 'ballroom', 'billiard room', 'hall', 
            'kitchen', 'conservatory', 'study'}
        #weapons images
        self.candlestick = self.scaleImage(self.loadImage('Images/Weapons/candlestick.jpg'), 0.25)
        self.revolver = self.scaleImage(self.loadImage('Images/Weapons/revolver.jpg'), 0.25)
        self.leadPipe = self.scaleImage(self.loadImage('Images/Weapons/leadPipe.jpg'), 0.25)
        self.rope = self.scaleImage(self.loadImage('Images/Weapons/rope.jpg'), 0.25)
        self.knife = self.scaleImage(self.loadImage('Images/Weapons/knife.jpg'), 0.25)
        self.wrench = self.scaleImage(self.loadImage('Images/Weapons/wrench.jpg'), 0.25)
        self.weaponImages = {'candlestick': self.candlestick, 'revolver': self.revolver, 
            'leadpipe': self.leadPipe, 'rope': self.rope, 'knife': self.knife, 'wrench': self.wrench}
        self.weapons = {'candlestick', 'revolver', 'leadpipe', 'rope', 'knife', 'wrench'}
        #suspects images
        self.white = self.scaleImage(self.loadImage('Images/Suspects/white.jpg'), 0.25)
        self.green = self.scaleImage(self.loadImage('Images/Suspects/green.jpg'), 0.25)
        self.peacock = self.scaleImage(self.loadImage('Images/Suspects/peacock.jpg'), 0.25)
        self.scarlet = self.scaleImage(self.loadImage('Images/Suspects/scarlet.jpg'), 0.25)
        self.mustard = self.scaleImage(self.loadImage('Images/Suspects/mustard.jpg'), 0.25)
        self.plum = self.scaleImage(self.loadImage('Images/Suspects/plum.jpg'), 0.25)
        self.suspectImages = {'white': self.white, 'green': self.green, 'peacock': self.peacock,
            'scarlet': self.scarlet, 'mustard': self.mustard, 'plum': self.plum}
        self.allImages = {'library': self.library, 'dining room': self.diningRoom, 'lounge': self.lounge,
            'ballroom': self.ballroom, 'billiard room': self.billiardRoom, 'hall': self.hall,
            'kitchen': self.kitchen, 'conservatory': self.conservatory, 'study': self.study,
            'candlestick': self.candlestick, 'revolver': self.revolver, 
            'leadpipe': self.leadPipe, 'rope': self.rope, 'knife': self.knife, 'wrench': self.wrench,
            'white': self.white, 'green': self.green, 'peacock': self.peacock,
            'scarlet': self.scarlet, 'mustard': self.mustard, 'plum': self.plum}
        self.suspects = {'white', 'green', 'peacock', 'scarlet', 'mustard', 'plum'}
        self.allCards = (self.rooms | self.weapons) | self.suspects
        self.allCardsDict = {'suspects': [self.white, self.green, self.peacock, self.scarlet, self.mustard, self.plum],
                        'weapons': [self.candlestick, self.revolver, self.leadPipe, self.rope, self.knife, self.wrench],
                        'rooms': [self.library, self.diningRoom, self.lounge, self.ballroom, self.billiardRoom,
                                self.hall, self.kitchen, self.conservatory, self.study]}

        #booleans to make the rooms show up and disappear when changing room layout
        self.showHall = True
        self.showLounge = True
        self.showDiningRoom = True
        self.showKitchen = True
        self.showBallRoom = True
        self.showConservatory = True
        self.showBilliardRoom = True
        self.showLibrary = True
        self.showStudy = True

        #list containing the order of the new room layout
        self.roomLayoutList = []

        #list containing the final answer
        self.answer = []
        
        #player values
        self.choosePlayer = True
        self.playerColor = "black"
        self.playerPosition = (-1, -1)
        self.playerCards = set()
        self.playerGuess = []
        self.allowPlayerGuess = False
        self.allowPlayerResponse = False
        self.playerRoom = ""
        self.playerTurn = False
        self.playerResponse = ""
        self.suspectBox = (115, 140, 285, 410)
        self.weaponBox = (115, 480, 285, 750)
        self.roomBox = (115, 140, 285, 410)
        self.playerAccusation = []
        self.playerReadyToAccuse = False
        self.playerWon = False
        self.playerFirstTurn = True

        #computer values
        self.computerColor = "brown"
        self.computerPosition = (-1, -1)
        self.computerCards = set()
        self.computerChoices = {'suspects': set(), 'weapons': set(), 'rooms': set()}
        self.computerGuess = []
        self.allowComputerGuess = False
        self.computerRoom = ''
        self.computerAnswer = ['','','']
        self.computerReadyToAnswer = False
        self.computerResponse = ''
        self.computerWon = False

        #setting initial board values
        self.fillColor = ""
        self.startingSquares = [(5,0),(18,0),(24,9),(24,14),(0,16),(7,23)]
        #sets all rooms as grey on the algorithmic grid
        self.roomColor = "grey"
        #dictionary mapping room numbers to a list of room names, room grid coordinates, and the room doors
        self.roomsDict = {1 : ["", [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),
                            (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),
                            (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),
                            (3,1),(3,2),(3,3),(3,4),(3,5)], [(3,6)]],
                        2 : ["", [(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),
                            (1,9),(1,10),(1,11),(1,12),(1,13),(1,14),
                            (2,9),(2,10),(2,11),(2,12),(2,13),(2,14),
                            (3,9),(3,10),(3,11),(3,12),(3,13),(3,14),
                            (4,10),(4,11),(4,12),(4,13),(4,14),
                            (5,9),(5,10),(5,11),(5,12),(5,13),(5,14),
                            (6,9),(6,10),(6,13),(6,14)], [(4,9),(6,11),(6,12)]],
                        3 : ["", [(0,17),(0,18),(0,19),(0,20),(0,21),(0,22),(0,23),
                            (1,17),(1,18),(1,19),(1,20),(1,21),(1,22),(1,23),
                            (2,17),(2,18),(2,19),(2,20),(2,21),(2,22),(2,23),
                            (3,17),(3,18),(3,19),(3,20),(3,21),(3,22),(3,23),
                            (4,17),(4,18),(4,19),(4,20),(4,21),(4,22),(4,23),
                            (5,18),(5,19),(5,20),(5,21),(5,22)], [(5,17)]],
                        4 : ["", [(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),
                            (7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),
                            (8,0),(8,1),(8,2),(8,3),(8,4),(8,5),
                            (9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),
                            (10,1),(10,2),(10,4),(10,5)], [(8,6),(10,3)]],
                        5 : ["", [(12,0),(12,2),(12,3),(12,4),(12,5),
                            (13,0),(13,1),(13,2),(13,3),(13,4),(13,5),
                            (14,0),(14,1),(14,2),(14,3),(14,4),(14,5),
                            (15,0),(15,1),(15,2),(15,3),(15,4),
                            (16,0),(16,1),(16,2),(16,3),(16,4),(16,5)], [(12,1),(15,5)]],
                        6 : ["", [(9,16),(9,18),(9,19),(9,20),(9,21),(9,22),(9,23),
                            (10,16),(10,17),(10,18),(10,19),(10,20),(10,21),(10,22),(10,23),
                            (11,16),(11,17),(11,18),(11,19),(11,20),(11,21),(11,22),(11,23),
                            (12,17),(12,18),(12,19),(12,20),(12,21),(12,22),(12,23),
                            (13,16),(13,17),(13,18),(13,19),(13,20),(13,21),(13,22),(13,23),
                            (14,16),(14,17),(14,18),(14,19),(14,20),(14,21),(14,22),(14,23),
                            (15,19),(15,20),(15,21),(15,22),(15,23)], [(9,17),(12,16)]],
                        7 : ["", [(19,2),(19,3),
                            (20,0),(20,1),(20,2),(20,3),(20,4),(20,5),
                            (21,0),(21,1),(21,2),(21,3),(21,4),(21,5),
                            (22,0),(22,1),(22,2),(22,3),(22,4),(22,5),
                            (23,0),(23,1),(23,2),(23,3),(23,4),(23,5),
                            (24,0),(24,1),(24,2),(24,3),(24,4),(24,5)], [(19,4)]],
                        8 : ["", [(17,8),(17,10),(17,11),(17,12),(17,13),(17,15),
                            (18,8),(18,9),(18,10),(18,11),(18,12),(18,13),(18,14),(18,15),
                            (19,9),(19,10),(19,11),(19,12),(19,13),(19,14),
                            (20,8),(20,9),(20,10),(20,11),(20,12),(20,13),(20,14),(20,15),
                            (21,8),(21,9),(21,10),(21,11),(21,12),(21,13),(21,14),(21,15),
                            (22,8),(22,9),(22,10),(22,11),(22,12),(22,13),(22,14),(22,15),
                            (23,10),(23,11),(23,12),(23,13),(24,10),(24,11),(24,12),(24,13)], [(17,9),(17,14),(19,8),(19,15)]],
                        9 : ["", [(18,18),(18,20),(18,21),(18,22),(18,23),
                            (19,18),(19,19),(19,20),(19,21),(19,22),(19,23),
                            (20,18),(20,19),(20,20),(20,21),(20,22),(20,23),
                            (21,18),(21,19),(21,20),(21,21),(21,22),(21,23),
                            (22,18),(22,19),(22,20),(22,21),(22,22),(22,23),
                            (23,19),(23,20),(23,21),(23,22),(23,23),
                            (24,18),(24,19),(24,20),(24,21),(24,22),(24,23)], [(18,19)]]}
        self.roomsList = []
        #sets all doors as pink on the grid
        self.doorColor = "pink"
        self.doorsList = [(3,6),(4,9),(5,17),(6,11),(6,12),(8,6),(9,17),(10,3),
                        (12,1),(12,16),(15,5),(17,9),(17,14),(18,19),(19,4),(19,8),(19,15)]
        self.centerDoor = (8,11)
        #sets stairs as orange and cyan
        self.stair1color = "orange"
        self.stair1list = [(3,0),(23,18)]
        self.stair2color = "cyan"
        self.stair2list = [(5,23),(19,1)]
        #sets the center room as magenta
        self.centerRoomColor = "magenta"
        self.centerRoomList = [(8,9),(8,10),(8,12),(8,13),
                            (9,9),(9,10),(9,11),(9,12),(9,13),
                            (10,9),(10,10),(10,11),(10,12),(10,13),
                            (11,9),(11,10),(11,11),(11,12),(11,13),
                            (12,9),(12,10),(12,11),(12,12),(12,13),
                            (13,9),(13,10),(13,11),(13,12),(13,13),
                            (14,9),(14,10),(14,11),(14,12),(14,13)]
        self.extraSquaresList = [(4,0),(10,0),(11,0),(17,0),(19,0),(0,8),(24,6),(24,7),(24,8),(23,6),
                                    (0,15),(6,23),(8,23),(16,23),(24,15),(24,16),(24,17),(23,17)]

    #executes when mouse is clicked by the user
    def mousePressed(self, event):
        #if the click is within the game board, the coordinates are stored as a row and col
        if (self.leftMargin <= event.x < self.width - self.rightMargin and 
                self.topMargin <= event.y < self.height - self.bottomMargin):
            (boardRow, boardCol) = self.getBoardCell(event.x, event.y)
            #at the beginning of the game, the player must click on a starting square
            #the computer randomly picks one of the other starting squares
            if self.gameStart:
                if (boardRow, boardCol) in self.startingSquares:
                    self.playerPosition = (boardRow, boardCol)
                    self.startingSquares.remove((boardRow, boardCol))
                    self.computerPosition = random.choice(self.startingSquares)
                    self.playerTurn = True
                    self.playerRollDice = 0
                    self.gameStart = False
            #if it's the player's turn, it moves the players towards the room they clicked on
            if self.playerTurn and self.playerRollDice == 2:
                if (boardRow, boardCol) in self.roomsList:
                    self.playerRoom = self.getRoom(boardRow, boardCol)
                    self.playerMove(self.getDoor(self.playerRoom, self.playerPosition))
                #if the player is ready to make a final accusation, it moves the player automatically to the center room
                if self.playerReadyToAccuse:
                    self.playerMove(self.centerDoor)

        #allows the player to fill out the detective's notebook            
        if (self.nbLeftMargin <= event.x <= self.width - self.nbRightMargin and self.showGuessScreen == False and
                self.showAccusationScreen1 == False and self.showAccusationScreen2 == False and self.showRoomLayoutScreen == False):
            if self.suspectTopMargin <= event.y <= self.height - self.suspectBottomMargin:
                (suspectRow, suspectCol) = self.getSuspectCell(event.x, event.y)
                color = self.nbSuspectDict.get((suspectRow, suspectCol), "")
                self.nbSuspectDict[(suspectRow, suspectCol)] = self.setnbColor(color)
            if self.weaponTopMargin <= event.y <= self.height - self.weaponBottomMargin:
                (weaponRow, weaponCol) = self.getWeaponCell(event.x, event.y)
                color = self.nbWeaponDict.get((weaponRow, weaponCol), "")
                self.nbWeaponDict[(weaponRow, weaponCol)] = self.setnbColor(color)
            if self.roomTopMargin <= event.y <= self.height - self.roomBottomMargin:
                (roomRow, roomCol) = self.getRoomCell(event.x, event.y)
                color = self.nbRoomDict.get((roomRow, roomCol), "")
                self.nbRoomDict[(roomRow, roomCol)] = self.setnbColor(color)
        
        #if the player clicks on the buttons, the boolean for that button becomes the opposite
        #to show and hide the screens
        if 25 <= event.x <= 75 and (self.height - 75) <= event.y <= (self.height - 25):
            self.showInstructions = not self.showInstructions
        if 100 <= event.x <= 150 and (self.height - 75) <= event.y <= (self.height - 25) and self.showGuessScreen == False:
            self.showPlayerCards = not self.showPlayerCards
        if 175 <= event.x <= 225 and (self.height - 75) <= event.y <= (self.height - 25) and self.showGuessScreen == False:
            self.showAnswer = not self.showAnswer
        if 250 <= event.x <= 300 and (self.height - 75) <= event.y <= (self.height - 25):
            self.appStarted()

        #changes the dice image to a random die side when the user clicks on it
        if ((self.width - 90) <= event.x <= self.width and self.height - 745 <= event.y <= self.height - 655 and
                self.showGuessScreen == False and self.showAccusationScreen1 == False and 
                self.showAccusationScreen2 == False and self.playerTurn and self.playerRollDice < 2):
            self.playerRollDice += 1

        #allows the user to change the room layout
        if 750 <= event.x <= 900 and 350 <= event.y <= 400:
            self.showHall = False
            self.roomLayoutList.append("hall")
        if 950 <= event.x <= 1100 and 350 <= event.y <= 400:
            self.showLounge = False
            self.roomLayoutList.append("lounge")
        if 1150 <= event.x <= 1300 and 350 <= event.y <= 400:
            self.showDiningRoom = False
            self.roomLayoutList.append("dining room")
        if 750 <= event.x <= 900 and 450 <= event.y <= 500:
            self.showKitchen = False
            self.roomLayoutList.append("kitchen")
        if 950 <= event.x <= 1100 and 450 <= event.y <= 500:
            self.showBallRoom = False
            self.roomLayoutList.append("ballroom")
        if 1150 <= event.x <= 1300 and 450 <= event.y <= 500:
            self.showConservatory = False
            self.roomLayoutList.append("conservatory")
        if 750 <= event.x <= 900 and 550 <= event.y <= 600:
            self.showBilliardRoom = False
            self.roomLayoutList.append("billiard room")
        if 950 <= event.x <= 1100 and 550 <= event.y <= 600:
            self.showLibrary = False
            self.roomLayoutList.append("library")
        if 1150 <= event.x <= 1300 and 550 <= event.y <= 600:
            self.showStudy = False
            self.roomLayoutList.append("study")
        #sets the room layout when the player clicks the done button after clicking all 9 rooms
        if (self.width - 200 <= event.x <= self.width - 100 and self.height - 150 <= event.y <= self.height - 100 and
                len(self.roomLayoutList) == 9):
            self.showRoomLayoutScreen = False
            self.setRoomLayout()

        #click to make a guess or accusation
        if self.width - 80 <= event.x <= self.width - 10 and self.height - 560 <= event.y <= self.height - 490 and self.allowPlayerGuess:
            self.showGuessScreen = True
            self.showTruth = False
        #pressing the 'submit guess' button shows the computer's response to the guess
        if self.width - 200 <= event.x <= self.width - 50 and 50 <= event.y <= 100 and self.showGuessScreen:
            self.setPlayerGuess()
            self.showGuessScreen = False
            self.showTruth = True
            self.setComputerResponse()
        #closes the computer's response screen
        if self.width - 300 <= event.x <= self.width - 200 and 200 <= event.y <= 250 and self.showTruth:
            self.showTruth = False
            self.allowPlayerGuess = False
        #player clicks when they are ready to accuse
        if self.width - 80 <= event.x <= self.width - 10 and self.height - 470 <= event.y <= self.height - 400:
            self.playerReadyToAccuse = True
        #shows the final accusation screen with rooms
        if (self.width - 200 <= event.x <= self.width - 50 and 50 <= event.y <= 100 and 
            self.showAccusationScreen1 and self.showAccusationScreen2 == False):
            self.setPlayerAccusation()
            self.showAccusationScreen1 = False
            self.showAccusationScreen2 = True
        #closes the final accusation screen
        if (self.width - 200 <= event.x <= self.width - 100 and self.height - 150 <= event.y <= self.height - 100 and 
            self.showAccusationScreen2 and self.showAccusationScreen1 == False):
            self.setPlayerAccusation()
            self.checkPlayerAccusation()
            self.showAccusationScreen2 = False
        #allows the user to respond to the computer's guess
        if 25 <= event.x <= 275 and 25 <= event.y <= 225 and self.allowPlayerResponse:
            self.createPlayerResponse()

        #clicking on a suspect when guessing or accusing
        if self.showGuessScreen or self.showAccusationScreen1:
            if 115 <= event.x <= 285 and 140 <= event.y <= 410:
                self.suspectBox = (115, 140, 285, 410)
            elif 315 <= event.x <= 485 and 140 <= event.y <= 410:
                self.suspectBox = (315, 140, 485, 410)
            elif 515 <= event.x <= 685 and 140 <= event.y <= 410:
                self.suspectBox = (515, 140, 685, 410)
            elif 715 <= event.x <= 885 and 140 <= event.y <= 410:
                self.suspectBox = (715, 140, 885, 410)
            elif 915 <= event.x <= 1085 and 140 <= event.y <= 410:
                self.suspectBox = (915, 140, 1085, 410)
            elif 1115 <= event.x <= 1285 and 140 <= event.y <= 410:
                self.suspectBox = (1115, 140, 1285, 410)
        #clicking on a weapon when guessing or accusing
            if 115 <= event.x <= 285 and 480 <= event.y <= 750:
                self.weaponBox = (115, 480, 285, 750)
            elif 315 <= event.x <= 485 and 480 <= event.y <= 750:
                self.weaponBox = (315, 480, 485, 750)
            elif 515 <= event.x <= 685 and 480 <= event.y <= 750:
                self.weaponBox = (515, 480, 685, 750)
            elif 715 <= event.x <= 885 and 480 <= event.y <= 750:
                self.weaponBox = (715, 480, 885, 750)
            elif 915 <= event.x <= 1085 and 480 <= event.y <= 750:
                self.weaponBox = (915, 480, 1085, 750)
            elif 1115 <= event.x <= 1285 and 480 <= event.y <= 750:
                self.weaponBox = (1115, 480, 1285, 750)

        #clicking on a room when accusing
        if self.showAccusationScreen2:
            if 115 <= event.x <= 285 and 140 <= event.y <= 410:
                self.roomBox = (115, 140, 285, 410)
            elif 315 <= event.x <= 485 and 140 <= event.y <= 410:
                self.roomBox = (315, 140, 485, 410)
            elif 515 <= event.x <= 685 and 140 <= event.y <= 410:
                self.roomBox = (515, 140, 685, 410)
            elif 715 <= event.x <= 885 and 140 <= event.y <= 410:
                self.roomBox = (715, 140, 885, 410)
            elif 915 <= event.x <= 1085 and 140 <= event.y <= 410:
                self.roomBox = (915, 140, 1085, 410)
            elif 1115 <= event.x <= 1285 and 140 <= event.y <= 410:
                self.roomBox = (1115, 140, 1285, 410)
            elif 115 <= event.x <= 285 and 480 <= event.y <= 750:
                self.roomBox = (115, 480, 285, 750)
            elif 315 <= event.x <= 485 and 480 <= event.y <= 750:
                self.roomBox = (315, 480, 485, 750)
            elif 515 <= event.x <= 685 and 480 <= event.y <= 750:
                self.roomBox = (515, 480, 685, 750)

    #executes at the start of the game
    def timerFired(self):
        if self.showRoomLayoutScreen == False:
            #displays an input box for the user to choose their player color
            #citation: the input box method was learned during the optional lecture "Optional: Images with PIL + Using the App Class"
            if self.choosePlayer == True:
                color = ""
                while color != "black" and color != "white" and color != "green" and color != "blue" and color != "red" and color != "purple":
                    color = self.getUserInput("""\
                        Pick one of the following player colors: black, white, green, blue, red, purple.\n
                        Then click on one of the six starting squares to choose your beginning location""")
                    color = color.lower()
                self.playerColor = color
                self.choosePlayer = False
                #sets the answer, the player's cards, the computer's card, the computer's choices to guess from
                self.setAnswer()
                self.playerCards = self.getPlayerCards()
                self.computerCards = self.getComputerCards()
                self.setComputerChoices()
                self.setRoomsList()
                self.gameStart = True
            #allows the computer to roll the die and move if the player has moved and guessed
            if (self.gameStart == False and self.playerTurn == False 
                and self.allowPlayerGuess == False and self.allowPlayerResponse == False):
                self.rollDice()
                self.computerMove()
            #die keeps rolling until player stops it
            #player can only roll once
            if self.playerRollDice == 1:
                self.rollDice()

    #draws the title on the top of the screen
    def drawTitle(self, canvas):
        canvas.create_text(self.width / 2, self.topMargin / 2.5,
                        text = "CLUE!", font = "Arial 30 bold")

    #draws buttons for instructions, player's cards, answer, reset, 
    #correct, wrong, guessing, accusing, and changing room layout
    def drawButtons(self, canvas):
        #bottom left buttons
        canvas.create_oval(25, self.height - 75, 75, self.height - 25, 
                                fill = "pink")
        canvas.create_text(50, self.height - 50, text = "HELP",
                                font = "Arial 15 bold")
        canvas.create_oval(100, self.height - 75, 150, self.height - 25, 
                                fill = "light yellow")
        canvas.create_text(125, self.height - 50, text = "CARDS",
                                font = "Arial 13 bold")
        canvas.create_oval(175, self.height - 75, 225, self.height - 25, 
                                fill = "light green")
        canvas.create_text(200, self.height - 50, text = "ANSWER",
                                font = "Arial 11 bold")
        canvas.create_oval(250, self.height - 75, 300, self.height - 25, 
                                fill = "purple")
        canvas.create_text(275, self.height - 50, text = "RESET",
                                font = "Arial 14 bold")
        #right side buttons
        canvas.create_oval(self.width - 80, self.height - 560, self.width - 10, self.height - 490, 
                                fill = "orange")
        canvas.create_text(self.width - 45, self.height - 525, text = "GUESS",
                                font = "Arial 14 bold")
        canvas.create_oval(self.width - 80, self.height - 470, self.width - 10, self.height - 400, 
                                fill = "magenta")
        canvas.create_text(self.width - 45, self.height - 435, text = "READY\nTO\nACCUSE",
                                font = "Arial 12 bold")

    #displays instructions when "HELP" button is clicked
    #citation: instructions adapted from https://www.fgbradleys.com/rules/Clue.pdf
    def instructions(self, canvas):
        if self.showInstructions:
            canvas.create_rectangle(200, 100, self.width - 200, self.height - 100,
                                        fill = "pink")
            canvas.create_text(self.width / 2, 125, text = "Instructions!",
                                        font = "Arial 30 bold")
            canvas.create_text(self.width/2, self.height/2, text = """ \n

                    Mr. John Boddy, the owner of Tudor Mansion has been found murdered inside his home.
                    The object of the game is to determine the killer, the murder weapon, and the room in which the murder occurred.\n
                    You and the computer will each receive 9 cards. 3 cards will be placed in the answer button, and so neither 
                    you nor the computer have those 3 cards. Those 3 cards will hold the answer to the suspect, weapon, and 
                    room of the murder. Through guesses and process of elimination, you must guess these three cards.
                
                    Step 1: Roll the dice to move. You may not move diagonally and can only enter a room through the doors.
                            After rolling, click on the room you wish to go to, and you will automatically be moved
                            along the shortest path to that room's doors. \n
                    Step 2: Once you have entered a room, you may not move any more spaces. You will then make a guess
                            as to the suspect, weapon, and room were chosen as the answer. Keep in mind that your current room
                            will automatically be stored as the room for your guess. \n
                    Step 3: When leaving a room, if your room has a secret passage you may use that to go to the
                            diagonally opposite room on the board.\n
                    Step 4: When the computer has entered a room and has made a guess, you must respond to the guess by
                            revealing if you hold any of the cards the computer has guessed. You only have to reveal one
                            card on each turn.\n
                    Step 5: If you believe you know the correct answer, you may click the "Ready to Accuse" button.
                            You will then be moved towards the center room automatically. Once in the center room, you
                            will be able to enter your accusation. The last screen will reveal if you got the correct answer
                            or not. You may only make one guess in the game, so the game will end whether or not you are correct.
                            Remember the aim of the game is to get the correct accusation for suspect, weapon, and room
                            before the computer is able to figure it out! \n
                                                                        GOOD LUCK AND HAVE FUN! """,
                    font = "Arial 16 bold", anchor = "center")

    #writes out instructions for the player as they play each step of the game
    def drawSideInstructions(self, canvas):
        if self.gameStart:
            canvas.create_text(100, 400, text = """\
                        Click on one of the six labeled
                        starting locations on the board""", font = "Arial 20 bold")
        elif (self.gameStart == False and self.playerRollDice == 0 and self.playerTurn and 
            self.playerReadyToAccuse == False and self.playerFirstTurn):
            canvas.create_text(100, 400, text = """\
                        Click on the die to start rolling it.
                        Click again to stop the die.
                        The die face to see is how
                        many steps you may move.""", font = "Arial 20 bold")
        elif (self.gameStart == False and self.playerRollDice == 0 and self.playerTurn and 
            self.playerReadyToAccuse == False and self.playerFirstTurn == False):
            canvas.create_text(100, 400, text = """\
                        The computer has finished its turn.
                        Click on the die to start rolling it.
                        Click again to stop the die.
                        The die face to see is how
                        many steps you may move.
                        If you are ready to accuse,
                        click the magenta "Ready to 
                        Accuse" button.""", font = "Arial 18 bold")
        elif (self.playerRollDice == 2 and self.allowPlayerGuess == False and 
            self.allowComputerGuess == False and self.playerReadyToAccuse == False):
            canvas.create_text(100, 400, text = """\
                        Click on one of the nine labeled
                        rooms that you wish to enter.
                        You will automatically move
                        towards its door.""", font = "Arial 20 bold")
        elif self.allowPlayerGuess and self.playerReadyToAccuse == False:
            canvas.create_text(100, 400, text = """\
                        You have entered a room!
                        Click on the orange "GUESS"
                        button on the right side of 
                        the screen. Then, click on the 
                        suspect and weapon you would 
                        like to guess. Your current
                        room will be automatically used 
                        as your guess's room.""", font = "Arial 20 bold")
        elif self.allowPlayerResponse:
            canvas.create_text(100, 400, text = """\
                        The computer is in a room 
                        and has made a guess! Click 
                        on the "Answer the Computer's
                        Guess" button to respond to 
                        the computer's guess.""", font = "Arial 20 bold")
        elif self.playerReadyToAccuse:
            canvas.create_text(100, 400, text = """\
                        You are ready to accuse!
                        Continue rolling the die
                        as before! Click on the center
                        room and you will be
                        automatically moved there.
                        Once in the center room,
                        enter your accusation for
                        suspect, weapon, and room.
                        Let's see if you are correct!""", font = "Arial 20 bold")

    #citation: I learned about grid functions from (https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids)
    #returns the row and column of a certain x,y coordinate of the game board
    def getBoardCell(self, x, y):
        row = int((y - self.topMargin) / self.cellHeight)
        col = int((x - self.leftMargin) / self.cellWidth)
        return (row, col)

    #citation: I learned about grid functions from (https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids)
    #returns the bounds for each singular cell on the game board
    #depends on board margins, height and width of the canvas, and total rows and columns
    def getBoardCellBounds(self, row, col):
        x1 = self.leftMargin + col * self.cellWidth
        y1 = self.topMargin + row * self.cellHeight
        x2 = x1 + self.cellWidth
        y2 = y1 + self.cellHeight
        return x1, y1, x2, y2

    #citation: I learned about grid functions from (https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids)
    #draws the board grid
    def drawBoardGrid(self, canvas):
        for row in range(self.rows):
            for col in range(self.cols):
                x1, y1, x2, y2 = self.getBoardCellBounds(row, col)
                if self.playerPosition == (row, col):
                    self.fillColor = self.playerColor
                elif self.computerPosition == (row, col):
                    self.fillColor = self.computerColor
                else:
                    self.fillColor = ""
                canvas.create_rectangle(x1, y1, x2, y2, fill = self.fillColor, outline = '')

    #citation: I learned about grid functions from (https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids)
    #returns the row and column of the suspects grid of the notebook
    def getSuspectCell(self, x, y):
        row = int((y - self.suspectTopMargin) / self.suspectCellHeight)
        return (row, 0)

    #citation: I learned about grid functions from (https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids)
    #returns the row and column of the weapons grid of the notebook
    def getWeaponCell(self, x, y):
        row = int((y - self.weaponTopMargin) / self.weaponCellHeight)
        return (row, 0)
    
    #citation: I learned about grid functions from (https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids)
    #returns the row and column of the rooms grid of the notebook
    def getRoomCell(self, x, y):
        row = int((y - self.roomTopMargin) / self.roomCellHeight)
        return (row, 0)

    #citation: I learned about grid functions from (https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids)
    #returns the bounds for each singular cell on the suspects grid of the notebook
    def getSuspectCellBounds(self, row, col):
        x1 = self.nbLeftMargin + col * self.nbCellWidth
        y1 = self.suspectTopMargin + row * self.suspectCellHeight
        x2 = x1 + self.nbCellWidth
        y2 = y1 + self.suspectCellHeight
        return x1, y1, x2, y2

    #citation: I learned about grid functions from (https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids)
    #returns the bounds for each singular cell on the weapons grid of the notebook
    def getWeaponCellBounds(self, row, col):
        x1 = self.nbLeftMargin + col * self.nbCellWidth
        y1 = self.weaponTopMargin + row * self.weaponCellHeight
        x2 = x1 + self.nbCellWidth
        y2 = y1 + self.weaponCellHeight
        return x1, y1, x2, y2

    #citation: I learned about grid functions from (https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids)
    #returns the bounds for each singular cell on the rooms grid of the notebook
    def getRoomCellBounds(self, row, col):
        x1 = self.nbLeftMargin + col * self.nbCellWidth
        y1 = self.roomTopMargin + row * self.roomCellHeight
        x2 = x1 + self.nbCellWidth
        y2 = y1 + self.roomCellHeight
        return x1, y1, x2, y2

    #citation: I learned about grid functions from (https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids)
    #draws the notebooks's 3 grids so the user can fill in green and red
    def drawNotebookGrid(self, canvas):
        for col in range(self.notebookCols):
            for row in range(self.suspectRows):
                fill = ""
                x1, y1, x2, y2 = self.getSuspectCellBounds(row, col)
                if (row, col) in self.nbSuspectDict:
                    fill = self.nbSuspectDict[(row, col)]
                canvas.create_rectangle(x1, y1, x2, y2, fill = fill, outline = '')
            for row in range(self.weaponRows):
                fill = ""
                x1, y1, x2, y2 = self.getWeaponCellBounds(row, col)
                if (row, col) in self.nbWeaponDict:
                    fill = self.nbWeaponDict[(row, col)]
                canvas.create_rectangle(x1, y1, x2, y2, fill = fill, outline = '')
            for row in range(self.roomRows):
                fill = ""
                x1, y1, x2, y2 = self.getRoomCellBounds(row, col)
                if (row, col) in self.nbRoomDict:
                    fill = self.nbRoomDict[(row, col)]
                canvas.create_rectangle(x1, y1, x2, y2, fill = fill, outline = '')

    #sets the notebook's fill color to clear, green, or red
    def setnbColor(self, color):
        if color == "":
            return "green"
        elif color == "green":
            return "red"
        else:
            return ""

    #draws the screen that allows the player to change the room layout
    def drawChangeRoomLayoutScreen(self, canvas):
        if self.showRoomLayoutScreen:
            canvas.create_rectangle(0, 0, self.width, self.height, fill = "gold")
            canvas.create_image(1000, 115, image = ImageTk.PhotoImage(self.clueLogoScale))
            canvas.create_rectangle(self.width - 200, self.height - 150, self.width - 100, self.height - 100,
                                fill = "black")
            canvas.create_text(self.width - 150, self.height - 125, text = "START", fill = "white")
            canvas.create_image(400, self.height / 2 + 25, image = ImageTk.PhotoImage(self.changeBoardScaled))
            canvas.create_text(210, 205, text = "1", font = "Arial 30 bold", fill = "red")
            canvas.create_text(400, 240, text = "2", font = "Arial 30 bold", fill = "red")
            canvas.create_text(580, 230, text = "3", font = "Arial 30 bold", fill = "red")
            canvas.create_text(210, 330, text = "4", font = "Arial 30 bold", fill = "red")
            canvas.create_text(200, 460, text = "5", font = "Arial 30 bold", fill = "red")
            canvas.create_text(575, 410, text = "6", font = "Arial 30 bold", fill = "red")
            canvas.create_text(200, 600, text = "7", font = "Arial 30 bold", fill = "red")
            canvas.create_text(400, 575, text = "8", font = "Arial 30 bold", fill = "red")
            canvas.create_text(600, 590, text = "9", font = "Arial 30 bold", fill = "red")
            canvas.create_text(950, 275, text = """\
                                Welcome to CLUE!!
                                Before we begin, please select your room layout.
                                Following the order of the rooms to the left,
                                click on the rooms below in the order you would like them to appear
                                (first click the room you want room 1 to be and click room 9 last).""",
                                font = "Arial 20 bold")
            if self.showHall:
                canvas.create_rectangle(750, 350, 900, 400, fill = "black")
                canvas.create_text(825, 375, text = "HALL", fill = "white")
            if self.showLounge:
                canvas.create_rectangle(950, 350, 1100, 400, fill = "black")
                canvas.create_text(1025, 375, text = "LOUNGE", fill = "white")
            if self.showDiningRoom:
                canvas.create_rectangle(1150, 350, 1300, 400, fill = "black")
                canvas.create_text(1225, 375, text = "DINING ROOM", fill = "white")
            if self.showKitchen:
                canvas.create_rectangle(750, 450, 900, 500, fill = "black")
                canvas.create_text(825, 475, text = "KITCHEN", fill = "white")
            if self.showBallRoom:
                canvas.create_rectangle(950, 450, 1100, 500, fill = "black")
                canvas.create_text(1025, 475, text = "BALLROOM", fill = "white")
            if self.showConservatory:
                canvas.create_rectangle(1150, 450, 1300, 500, fill = "black")
                canvas.create_text(1225, 475, text = "CONSERVATORY", fill = "white")
            if self.showBilliardRoom:
                canvas.create_rectangle(750, 550, 900, 600, fill = "black")
                canvas.create_text(825, 575, text = "BILLIARD ROOM", fill = "white")
            if self.showLibrary:
                canvas.create_rectangle(950, 550, 1100, 600, fill = "black")
                canvas.create_text(1025, 575, text = "LIBRARY", fill = "white")
            if self.showStudy:
                canvas.create_rectangle(1150, 550, 1300, 600, fill = "black")
                canvas.create_text(1225, 575, text = "STUDY", fill = "white")

    #sets the new room layout inputed by the player as the final layout for the game
    def setRoomLayout(self):
        key = 1
        for room in self.roomLayoutList:
            self.roomsDict[key][0] = room
            key += 1

    #draws the new room names onto the board
    def drawNewRooms(self, canvas):
        if self.showRoomLayoutScreen == False:
            canvas.create_text(450, 125, text = self.roomLayoutList[0], font = "Arial 25 bold", fill = "red")
            canvas.create_text(715, 160, text = self.roomLayoutList[1], font = "Arial 25 bold", fill = "red")
            canvas.create_text(980, 150, text = self.roomLayoutList[2], font = "Arial 25 bold", fill = "red")
            canvas.create_text(450, 300, text = self.roomLayoutList[3], font = "Arial 25 bold", fill = "red")
            canvas.create_text(425, 470, text = self.roomLayoutList[4], font = "Arial 25 bold", fill = "red")
            canvas.create_text(975, 400, text = self.roomLayoutList[5], font = "Arial 25 bold", fill = "red")
            canvas.create_text(425, 675, text = self.roomLayoutList[6], font = "Arial 25 bold", fill = "red")
            canvas.create_text(715, 630, text = self.roomLayoutList[7], font = "Arial 25 bold", fill = "red")
            canvas.create_text(1000, 660, text = self.roomLayoutList[8], font = "Arial 25 bold", fill = "red")

    #choose an answer at random from all the given cards
    #citation for random at top of file
    def setAnswer(self):
        suspect = random.sample(self.suspects, 1)
        weapon = random.sample(self.weapons, 1)
        room = random.sample(self.rooms, 1)
        self.answer += (suspect + weapon + room)

    #draws the answer when the green "answer" button is clicked
    def drawAnswer(self, canvas):
        if self.showAnswer and self.showGuessScreen == False:
            canvas.create_rectangle(100, 100, self.width - 100, self.height - 100,
                                        fill = "light green")
            canvas.create_text(self.width / 2, 200, text = "Answer!",
                                        font = "Arial 30 bold")
            location = 400
            for answer in self.answer:
                canvas.create_image(location, self.height/2, 
                            image = ImageTk.PhotoImage(self.allImages[answer]))
                location += 320

    #deals 9 random cards to the player
    #learned about the difference method from https://www.geeksforgeeks.org/python-set-difference/
    def getPlayerCards(self):
        elligibleCards = self.allCards.difference(self.answer)
        return set(random.sample(elligibleCards, int(len(elligibleCards)/2)))

    #draws the player's cards when the blue "cards" button is clicked
    def drawPlayerCards(self, canvas):
        if self.showPlayerCards and self.showGuessScreen == False:
            canvas.create_rectangle(100, 50, self.width - 100, self.height - 100,
                                        fill = "light blue")
            canvas.create_text(self.width / 2, 75, text = "My Cards!",
                                        font = "Arial 30 bold")
            location = 250
            playerCards = list(self.playerCards)
            for i in range(0,5):
                canvas.create_image(location, 240, image = ImageTk.PhotoImage(self.allImages[playerCards[i]]))
                location += 230
            location = 350
            for i in range(5,9):
                canvas.create_image(location, 535, image = ImageTk.PhotoImage(self.allImages[playerCards[i]]))
                location += 250

    #gives the computer the cards the player and the answer do not have
    #learned about the difference method from https://www.geeksforgeeks.org/python-set-difference/
    def getComputerCards(self):
        self.computerCards = self.allCards.difference(self.playerCards)
        return self.computerCards.difference(self.answer)

    #the die picks a random side when called
    def rollDice(self):
        self.currDiceValue = random.randint(1, 6)
        self.currDice = self.diceDict[self.currDiceValue]

    #finds the room the player clicked on
    def getRoom(self, clickRow, clickCol):
        for key in self.roomsDict:
            if (clickRow, clickCol) in self.roomsDict[key][1]:
                return self.roomsDict[key][0]
    
    #returns the door that gives the shortest path between the player/computer's
    #current position and the room they want to go to
    def getDoor(self, room, currentPosition):
        for key in self.roomsDict:
            if self.roomsDict[key][0] == room:
                doors = self.roomsDict[key][2]
                break
        #if the room only has one door, it automatically makes that the closest door
        if len(doors) == 1:
            closestDoor = doors[0]
        #or it find the closest door using pathfinding
        else:
            shortestPath = self.pathfinding(currentPosition, doors[0])
            for door in doors:
                currPath = self.pathfinding(currentPosition, door)
                if currPath == []:
                    return currentPosition
                elif len(currPath) <= len(shortestPath):
                    shortestPath = currPath
            closestDoor = shortestPath[0]
        return closestDoor

    #checks to see if the player and computer can use the staircases
    def useStaircase(self, position, destination):
        return ((position in self.roomsDict[1][2] and destination in self.roomsDict[9][2])
            or (position in self.roomsDict[9][2] and destination in self.roomsDict[1][2])
            or (position in self.roomsDict[3][2] and destination in self.roomsDict[7][2])
            or (position in self.roomsDict[7][2] and destination in self.roomsDict[3][2]))

    #moves the player towards a room depending on their die roll value
    def playerMove(self, destination):
        #if the player is in a room with a staircase, it can go to the diagonally opposite room
        if self.useStaircase(self.playerPosition, destination):
            self.playerPosition = destination
            self.playerTurn = False
            self.allowPlayerGuess = True
        else:
            path = self.pathfinding(self.playerPosition, destination)
            #if they are already in the room, nothing happens
            if path == []:
                pass
            #if the die value is greater than the steps it takes to get to the room,
            #the player is in the room and they can make a guess
            elif len(path) - 1 <= self.currDiceValue:
                self.playerPosition = path[0]
                self.playerTurn = False
                self.allowPlayerGuess = True
                #if the player is in the center room, the accusation screen comes up instead of the guess screen
                if self.playerPosition == self.centerDoor:
                    self.showAccusationScreen1 = True
            #if the die value is less than the steps it takes to get to the room,
            #the player moves the number of steps the die shows
            else:
                self.playerPosition = path[(self.currDiceValue + 1) * -1]
                self.playerTurn = False
        self.playerFirstTurn = False

    #draws the screen to make a guess when player is in a room
    def drawGuessScreen(self, canvas):
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

    #draws a red box around the suspect and weapon the player wants to guess or accuse
    def drawRedBoxes(self, canvas):
        (x1, y1, x2, y2) = self.suspectBox
        if self.showGuessScreen or self.showAccusationScreen1:
            canvas.create_rectangle(x1, y1, x2, y2, outline = "red", width = 3)
        (x3, y3, x4, y4) = self.weaponBox
        if self.showGuessScreen or self.showAccusationScreen1:
            canvas.create_rectangle(x3, y3, x4, y4, outline = "red", width = 3)
        (x5, y5, x6, y6) = self.roomBox
        if self.showAccusationScreen2:
            canvas.create_rectangle(x5, y5, x6, y6, outline = "red", width = 3)

    #sets the player's guess depending on what suspect and weapon they chose/drew the red box around
    def setPlayerGuess(self):
        self.playerGuess = ['white','candlestick']
        if self.showGuessScreen:
            if self.suspectBox == (115, 140, 285, 410):
                self.playerGuess[0] = ('white')
            elif self.suspectBox == (315, 140, 485, 410):
                self.playerGuess[0] = ('green')
            elif self.suspectBox == (515, 140, 685, 410):
                self.playerGuess[0] = ('peacock')
            elif self.suspectBox == (715, 140, 885, 410):
                self.playerGuess[0] = ('scarlet')
            elif self.suspectBox == (915, 140, 1085, 410):
                self.playerGuess[0] = ('mustard')
            elif self.suspectBox == (1115, 140, 1285, 410):
                self.playerGuess[0] = ('plum')

            if self.weaponBox == (115, 480, 285, 750):
                self.playerGuess[1] = ('candlestick')
            elif self.weaponBox == (315, 480, 485, 750):
                self.playerGuess[1] = ('revolver')
            elif self.weaponBox == (515, 480, 685, 750):
                self.playerGuess[1] = ('leadpipe')
            elif self.weaponBox == (715, 480, 885, 750):
                self.playerGuess[1] = ('rope')
            elif self.weaponBox == (915, 480, 1085, 750):
                self.playerGuess[1] = ('knife')
            elif self.weaponBox == (1115, 480, 1285, 750):
                self.playerGuess[1] = ('wrench')

            self.playerGuess.append(self.playerRoom)

    #sets the computer's response to the player's guess
    def setComputerResponse(self):
        #if the player's guess is also in the computer's cards, it sets the computer's response as that card
        #else, the computer's response is "None of the Cards"
        self.computerResponse = "None of the Cards"
        for guess in self.playerGuess:
            if guess in self.computerCards:
                self.computerResponse = guess
                break

    #draws the screen that shows the computer's response to the player making a guess
    def drawComputerResponseScreen(self, canvas):
        if self.showTruth:
            canvas.create_rectangle(150, 150, self.width - 150, self.height - 150,
                                            fill = "red")
            canvas.create_text(self.width/2, 250, text = "The Computer Has ...",
                                            font = "Arial 30 bold")
            if self.computerResponse == "None of the Cards":
                canvas.create_text(self.width/2, 450, text = self.computerResponse)
            else:
                canvas.create_image(self.width/2, 450, image = ImageTk.PhotoImage(self.allImages[self.computerResponse]))
            canvas.create_rectangle(self.width - 300, 200, self.width - 200, 250, fill = "black")
            canvas.create_text(self.width - 250, 225, text = "CLOSE", fill = "white")

    #this is the screen the player goes to when making their final accusation at the end of the game
    #this screen only has suspects and weapons
    def drawAccusationScreen1(self, canvas):
        if self.showAccusationScreen1:
            canvas.create_rectangle(25, 25, self.width - 25, self.height - 25,
                                            fill = "blue")
            canvas.create_text(self.width / 2, 75, text = "Make Your Accusation!",
                                            font = "Arial 30 bold")
            canvas.create_text(self.width / 2, 115, text = "Pick One Suspect!",
                                            font = "Arial 30 bold")
            canvas.create_text(self.width / 2, 450, text = "Pick One Weapon!",
                                            font = "Arial 30 bold")
            canvas.create_rectangle(self.width - 200, 50, self.width - 50, 100,
                                            fill = "red")
            canvas.create_text(self.width - 125, 75, text = "NEXT",
                                            font = "Arial 18 bold")
            location = 200
            for suspect in self.allCardsDict['suspects']:
                canvas.create_image(location, 275, image = ImageTk.PhotoImage(suspect))
                location += 200
            location = 200
            for weapon in self.allCardsDict['weapons']:
                canvas.create_image(location, 615, image = ImageTk.PhotoImage(weapon))
                location += 200

    #this is the screen the player goes to to continue making their final accusation
    #this screen has rooms
    def drawAccusationScreen2(self, canvas):
        if self.showAccusationScreen2:
            canvas.create_rectangle(25, 25, self.width - 25, self.height - 25,
                                            fill = "blue")
            canvas.create_text(self.width / 2, 75, text = "Make Your Accusation!",
                                            font = "Arial 30 bold")
            canvas.create_text(self.width / 2, 115, text = "Pick One Room!",
                                            font = "Arial 30 bold")
            canvas.create_rectangle(self.width - 225, self.height - 150, self.width - 75, self.height - 100,
                                fill = "red")
            canvas.create_text(self.width - 150, self.height - 125, text = "Submit Accusation")

            location = 200
            for index in range(0,6):
                canvas.create_image(location, 275, image = ImageTk.PhotoImage(self.allCardsDict['rooms'][index]))
                location += 200
            location = 200
            for index in range(6,9):
                canvas.create_image(location, 615, image = ImageTk.PhotoImage(self.allCardsDict['rooms'][index]))
                location += 200

    #sets the player's final accusation depending on the suspect, weapon, and room they click
    def setPlayerAccusation(self):
        if self.showAccusationScreen1:
            if self.suspectBox == (115, 140, 285, 410):
                self.playerAccusation.append('white')
            elif self.suspectBox == (315, 140, 485, 410):
                self.playerAccusation.append('green')
            elif self.suspectBox == (515, 140, 685, 410):
                self.playerAccusation.append('peacock')
            elif self.suspectBox == (715, 140, 885, 410):
                self.playerAccusation.append('scarlet')
            elif self.suspectBox == (915, 140, 1085, 410):
                self.playerAccusation.append('mustard')
            elif self.suspectBox == (1115, 140, 1285, 410):
                self.playerAccusation.append('plum')

            if self.weaponBox == (115, 480, 285, 750):
                self.playerAccusation.append('candlestick')
            elif self.weaponBox == (315, 480, 485, 750):
                self.playerAccusation.append('revolver')
            elif self.weaponBox == (515, 480, 685, 750):
                self.playerAccusation.append('leadpipe')
            elif self.weaponBox == (715, 480, 885, 750):
                self.playerAccusation.append('rope')
            elif self.weaponBox == (915, 480, 1085, 750):
                self.playerAccusation.append('knife')
            elif self.weaponBox == (1115, 480, 1285, 750):
                self.playerAccusation.append('wrench')

        if self.showAccusationScreen2:
            if self.roomBox == (115, 140, 285, 410):
                self.playerAccusation.append('library')
            elif self.roomBox == (315, 140, 485, 410):
                self.playerAccusation.append('dining room')
            elif self.roomBox == (515, 140, 685, 410):
                self.playerAccusation.append('lounge')
            elif self.roomBox == (715, 140, 885, 410):
                self.playerAccusation.append('ballroom')
            elif self.roomBox == (915, 140, 1085, 410):
                self.playerAccusation.append('billiard room')
            elif self.roomBox == (1115, 140, 1285, 410):
                self.playerAccusation.append('hall')
            elif self.roomBox == (115, 480, 285, 750):
                self.playerAccusation.append('kitchen')
            elif self.roomBox == (315, 480, 485, 750):
                self.playerAccusation.append('conservatory')
            elif self.roomBox == (515, 480, 685, 750):
                self.playerAccusation.append('study')

    #checks if the player's accusation is the correct answer
    #player has won if it is, lost if it isn't as the game is now over
    def checkPlayerAccusation(self):
        self.gameOver = True
        if self.playerAccusation == self.answer:
            self.playerWon = True

    #moves the computer towards a certain room depending on its die roll value
    def computerMove(self):
        #if the computer knows the answer, it automatically sets the center room as the destination
        if self.computerReadyToAnswer:
            destination = self.centerDoor
        #or it picks a random room from its choices to set as the destination
        else:
            if self.computerRoom == "":
                self.computerRoom = random.sample(self.computerChoices['rooms'], 1)[0]
            destination = self.getDoor(self.computerRoom, self.computerPosition)
        #finds the path from the computer's position to the room it set as its destination
        path = self.pathfinding(self.computerPosition, destination)
        if path == []:
            self.computerRoom = ""
        #checks if computer can use a staircase to move diagonally across the board
        elif self.useStaircase(self.computerPosition, destination):
            self.computerPosition = destination
            self.allowComputerGuess = True
            self.setComputerGuess()
        #if the die value is greater than the steps it takes to get to the room,
        #the computer is in the room and they can make a guess
        elif len(path) - 1 <= self.currDiceValue:
            self.computerPosition = path[0]
            self.allowComputerGuess = True
            self.setComputerGuess()
            #if the computer is in the center room, the game is over
            if self.computerPosition == self.centerDoor:
                self.gameOver = True
                self.checkComputerAccusation()
        #if the die value is less than the steps it takes to get to the room,
        #the computers moves the number of steps the die shows
        else:
            self.computerPosition = path[(self.currDiceValue + 1) * -1]
            self.playerTurn = True
            self.playerRollDice = 0
            self.allowComputerGuess = False

    #sets the computer choices as all the cards the computer does not already have
    def setComputerChoices(self):
        #learned copy.deepcopy from https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#copying
        rooms = copy.deepcopy(self.rooms)
        suspects = copy.deepcopy(self.suspects)
        weapons = copy.deepcopy(self.weapons)
        for card in self.computerCards:
            #learned discard method from https://www.programiz.com/python-programming/methods/set/discard
            rooms.discard(card)
            suspects.discard(card)
            weapons.discard(card)
        
        self.computerChoices['rooms'] = rooms
        self.computerChoices['suspects'] = suspects
        self.computerChoices['weapons'] = weapons

    #sets the computer guess when it is in a room
    def setComputerGuess(self):
        #picks a random suspect and weapon from the computer's choices
        suspect = random.sample(self.computerChoices['suspects'], 1)
        weapon = random.sample(self.computerChoices['weapons'], 1)
        self.computerGuess += (suspect + weapon)
        self.computerGuess.append(self.computerRoom)
        self.computerRoom = ""
        self.allowPlayerResponse = True

    #draws the computer's guess when the computer enters a room
    def drawComputerGuess(self, canvas):
        canvas.create_rectangle(25, 50, 275, 150, fill = "black")
        canvas.create_text(150, 75, text = "The computer guesses ... ", fill = "white")
        if self.allowComputerGuess:
            guess = repr(self.computerGuess)
            canvas.create_text(150, 125, text = guess[1:-1], fill = "white")

    #button the player clicks to respond to the computer's guess
    def drawPlayerResponseButton(self, canvas):
        canvas.create_rectangle(25, 175, 275, 225, fill = "white")
        canvas.create_text(150, 200, text = "Answer the Computer's Guess")

    #an input box to receive the player's response to the computer's guess
    def createPlayerResponse(self):
        #the input must be a card in both the computer's guess and and the player's cards
        #if there is no such card, the player responds 'none'
        #the input box method was learned during the optional lecture "Optional: Images with PIL + Using the App Class"
        #while the topic was learned in the lecture, the following code is my own
        while ((self.playerResponse not in self.playerCards 
            or self.playerResponse not in self.computerGuess) 
            and self.playerResponse != 'none'):
            self.playerResponse = self.getUserInput(f'''The computer has guessed {self.computerGuess}.\n
                            Your cards are {self.playerCards}.\n
                            Choose one of your cards that matches the computer's guess to show the computer.\n
                            If none of your cards match the computer's guess, type 'none'.''')
            self.playerResponse = self.playerResponse.lower()
        self.allowPlayerResponse = False
        self.processPlayerResponse()
        self.computerGuess = []
        self.playerTurn = True
        self.playerRollDice = 0

    #creates a new rooms set for the computer to choose from
    #this is implemented when there is only 1 room left in the computer's choices
    #makes the AI smarter by not allowing it to repeatedly guess the same room and give away the answer to the player
    def getNewComputerRooms(self):
        rooms = set()
        for card in self.computerCards:
            if card in self.rooms:
                rooms.add(card)
        return rooms

    #creates a new suspects set for the computer to choose from
    #same implementation and reasoning as above function
    def getNewComputerSuspects(self):
        suspects = set()
        for card in self.computerCards:
            if card in self.suspects:
                suspects.add(card)
        return suspects

    #creates a new weapons set for the computer to choose from
    #same implementation and reasoning as above function
    def getNewComputerWeapons(self):
        weapons = set()
        for card in self.computerCards:
            if card in self.weapons:
                weapons.add(card)
        return weapons

    #processes the player's answer and updates the computer's choices as necessary
    def processPlayerResponse(self):
        #if the player responded 'none', the computer knows that is the correct answer
        if self.playerResponse == "none":
            for index in range(0,3):
                if self.computerAnswer[index] == '':
                    self.computerAnswer[index] = self.computerGuess[index]
            self.computerReadyToAnswer = True
        #otherwise, it removes the player's response from the computer's choices since the answer cannot be that card
        else:
            #learned discard method from https://www.programiz.com/python-programming/methods/set/discard
            self.computerChoices['suspects'].discard(self.playerResponse)
            self.computerChoices['weapons'].discard(self.playerResponse)
            self.computerChoices['rooms'].discard(self.playerResponse)
            #if there is only one suspect, weapon, or room left in the computer's choices,
            #that suspect/weapon/room is part of the answer
            if len(self.computerChoices['suspects']) == 1:
                self.computerAnswer[0] = list(self.computerChoices['suspects'])[0]
                #after storing that one suspect in the computer's answer,
                #the computer's suspects choices are updated to the new list of suspects
                self.computerChoices['suspects'] = self.getNewComputerSuspects()
            if len(self.computerChoices['weapons']) == 1:
                self.computerAnswer[1] = list(self.computerChoices['weapons'])[0]
                #after storing that one weapon in the computer's answer,
                #the computer's weapons choices are updated to the new list of weapons
                self.computerChoices['weapons'] = self.getNewComputerWeapons()
            if len(self.computerChoices['rooms']) == 1:
                self.computerAnswer[2] = list(self.computerChoices['rooms'])[0]
                #after storing that one room in the computer's answer,
                #the computer's rooms choices are updated to the new list of rooms
                self.computerChoices['rooms'] = self.getNewComputerRooms()
        self.computerCheckIfReady()

    #the computer is ready to accuse if it's answer has all three (suspect, weapon, and room)
    def computerCheckIfReady(self):
        if '' not in self.computerAnswer:
            self.computerReadyToAnswer = True

    #checks if the computer's accusation is the correct answer
    #computer has won if it is, lost if it isn't as the game is now over
    def checkComputerAccusation(self):
        self.gameOver = True
        if self.computerAnswer == self.answer:
            self.computerWon = True

    #displays the final answer and who won!!!
    def drawFinalScreen(self, canvas):
        if self.gameOver:
            canvas.create_rectangle(100, 100, self.width - 100, self.height - 100,
                                        fill = "white")
            canvas.create_text(self.width / 2, 225, text = "Answer!",
                                        font = "Arial 16 bold")
            location = 400
            #displays the correct answer
            for answer in self.answer:
                canvas.create_image(location, self.height/2, 
                            image = ImageTk.PhotoImage(self.allImages[answer]))
                location += 320
            #displays who won and the accusation made
            if self.playerWon:
                canvas.create_text(self.width/2, 150, text = "You Won!", font = "Arial 30 bold")
                canvas.create_text(self.width/2, self.height - 150, text = f'You guessed {self.playerAccusation}')
            elif self.computerWon:
                canvas.create_text(self.width/2, 150, text = "Computer Won!", font = "Arial 30 bold")
                canvas.create_text(self.width/2, self.height - 150, text = f'Computer guessed {self.computerAnswer}')
            elif self.computerWon == False and self.playerAccusation == []:
                canvas.create_text(self.width/2, 150, text = "Computer lost!", font = "Arial 30 bold")
                canvas.create_text(self.width/2, self.height - 150, text = f'Computer guessed {self.computerAnswer}')
            else:
                canvas.create_text(self.width/2, 150, text = "You lost!", font = "Arial 30 bold")
                canvas.create_text(self.width/2, self.height - 150, text = f'You guessed {self.playerAccusation}')

    #draws the grids, title, buttons, all the screens, notebook, dice, and board
    def redrawAll(self, canvas):
        #background of the game
        canvas.create_rectangle(0, 0, self.width, self.height, fill = "light blue")
        #draws the board, notebook, and die
        canvas.create_image(self.width / 2, self.height - 373,
                                image = ImageTk.PhotoImage(self.boardScaled))
        canvas.create_image(self.width - 200, self.height / 2,
                                image = ImageTk.PhotoImage(self.notebookScaled))
        canvas.create_image(self.width - 45, self.height - 700,
                                image = ImageTk.PhotoImage(self.currDice))
        self.drawNewRooms(canvas)
        self.drawComputerGuess(canvas)
        self.drawPlayerResponseButton(canvas)
        self.drawSideInstructions(canvas)
        self.drawNotebookGrid(canvas)
        self.drawBoardGrid(canvas)
        self.drawTitle(canvas)
        self.drawButtons(canvas)
        self.instructions(canvas)
        self.drawGuessScreen(canvas)
        self.drawComputerResponseScreen(canvas)
        self.drawPlayerCards(canvas)
        self.drawAnswer(canvas)
        self.drawAccusationScreen1(canvas)
        self.drawAccusationScreen2(canvas)
        self.drawFinalScreen(canvas)
        self.drawChangeRoomLayoutScreen(canvas)
        self.drawRedBoxes(canvas)

    #sets a list of all grid coordinates that fall in a room
    def setRoomsList(self):
        for key in self.roomsDict:
            self.roomsList += self.roomsDict[key][1]

    #returns a list of the order the pathfinding algorithm should find the adjacent squares in
    #ensures the algorithm will find the shortest path
    def getDirection(self, start, end):
        directions = []
        difference = (end[0] - start[0], end[1] - start[1])
        if abs(difference[0]) >= abs(difference[1]):
            if end[0] >= start[0]:
                directions.append((+1, 0))
            else:
                directions.append((-1, 0))
            if end[1] >= start[1]:
                directions.append((0, +1))
            else:
                directions.append((0, -1))
        else:
            if end[1] >= start[1]:
                directions.append((0, +1))
            else:
                directions.append((0, -1))
            if end[0] >= start[0]:
                directions.append((+1, 0))
            else:
                directions.append((-1, 0))
        directions.append((directions[0][0] * -1, directions[0][1] * -1))
        directions.append((directions[1][0] * -1, directions[1][1] * -1))
        return directions[::-1]
                
    #I used this website (https://www.raywenderlich.com/3016-introduction-to-a-pathfinding)
    #only to learn how the A* algorithm, however I wrote all of the following code myself
    def pathfinding(self, start, end):
        if start == end:
            return []
        #finds the shortest path from the user's position to where they wish to go
        openList = [start]
        scoreList = [0]
        closedList = []
        gScore = 0
        parentDict = {}
        directions = self.getDirection(start, end)
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
            for direction in directions:
                (newRow, newCol) = (row + direction[0], col + direction[1])
                #square must be in the grid, and not a room, stair, or in the center room
                if (newRow >= self.rows or newRow < 0 or newCol >= self.cols or newCol < 0 or 
                    (newRow, newCol) in self.stair1list or (newRow, newCol) in self.roomsList or
                    (newRow, newCol) in self.stair2list or (newRow, newCol) in self.centerRoomList or
                    (newRow, newCol) in self.extraSquaresList):
                    pass
                elif (newRow, newCol) != end and (newRow, newCol) in self.doorsList:
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
    MyApp(width=1430, height=790)

if __name__ == '__main__':
    main()