       # self.allCardsDict = {'suspects': [self.white, self.green, self.peacock, self.scarlet, self.mustard, self.plum],
        #                 'weapons': [self.candlestick, self.revolver, self.leadPipe, self.rope, self.knife, self.wrench],
        #                 'rooms': [self.library, self.diningRoom, self.lounge, self.ballroom, self.billiardRoom,
        #                         self.hall, self.kitchen, self.conservatory, self.study]}
        # self.allCardsList = [self.white, self.green, self.peacock, self.scarlet, self.mustard, self.plum, 
        #                     self.candlestick, self.revolver, self.leadPipe, self.rope, self.knife, self.wrench,
        #                     self.library, self.diningRoom, self.lounge, self.ballroom, self.billiardRoom,
        #                     self.hall, self.kitchen, self.conservatory, self.study]
        # self.playerCards = random.sample(self.allCardsList, 9)

       # self.roomImages = {'library': self.scaleImage(self.loadImage('Images/Rooms/library.jpg'), 0.25),
        #     'diningRoom': self.scaleImage(self.loadImage('Images/Rooms/diningRoom.jpg'), 0.25),
        #     'lounge': self.scaleImage(self.loadImage('Images/Rooms/lounge.jpg'), 0.25),
        #     'ballroom': self.scaleImage(self.loadImage('Images/Rooms/ballroom.jpg'), 0.25),
        #     'billiardRoom': self.scaleImage(self.loadImage('Images/Rooms/billiardRoom.jpg'), 0.25),
        #     'hall': self.scaleImage(self.loadImage('Images/Rooms/hall.jpg'), 0.25)
        #     'kitchen': self.scaleImage(self.loadImage('Images/Rooms/kitchen.jpg'), 0.25),
        #     'conservatory': self.scaleImage(self.loadImage('Images/Rooms/conservatory.jpg'), 0.25),
        #     'study': self.scaleImage(self.loadImage('Images/Rooms/study.jpg'), 0.25)}

       #  self.roomsList = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),
       #          (0,17),(0,18),(0,19),(0,20),(0,21),(0,22),(0,23),
       #          (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),
       #          (1,17),(1,18),(1,19),(1,20),(1,21),(1,22),(1,23),
       #          (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,9),(2,10),(2,11),(2,12),(2,13),(2,14),
       #          (2,17),(2,18),(2,19),(2,20),(2,21),(2,22),(2,23),
       #          (3,1),(3,2),(3,3),(3,4),(3,5),(3,9),(3,10),(3,11),(3,12),(3,13),(3,14),(3,17),(3,18),(3,19),(3,20),(3,21),(3,22),(3,23),
       #          (4,10),(4,11),(4,12),(4,13),(4,14),(4,17),(4,18),(4,19),(4,20),(4,21),(4,22),(4,23),
       #          (5,9),(5,10),(5,11),(5,12),(5,13),(5,14),(5,18),(5,19),(5,20),(5,21),(5,22),
       #          (6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,9),(6,10),(6,13),(6,14),
       #          (7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),
       #          (8,0),(8,1),(8,2),(8,3),(8,4),(8,5),
       #          (9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,16),(9,18),(9,19),(9,20),(9,21),(9,22),(9,23),
       #          (10,1),(10,2),(10,4),(10,5),(10,16),(10,17),(10,18),(10,19),(10,20),(10,21),(10,22),(10,23),
       #          (11,16),(11,17),(11,18),(11,19),(11,20),(11,21),(11,22),(11,23),
       #          (12,0),(12,2),(12,3),(12,4),(12,5),(12,17),(12,18),(12,19),(12,20),(12,21),(12,22),(12,23),
       #          (13,0),(13,1),(13,2),(13,3),(13,4),(13,5),(13,16),(13,17),(13,18),(13,19),(13,20),(13,21),(13,22),(13,23),
       #          (14,0),(14,1),(14,2),(14,3),(14,4),(14,5),(14,16),(14,17),(14,18),(14,19),(14,20),(14,21),(14,22),(14,23),
       #          (15,0),(15,1),(15,2),(15,3),(15,4),(15,19),(15,20),(15,21),(15,22),(15,23),
       #          (16,0),(16,1),(16,2),(16,3),(16,4),(16,5),
       #          (17,8),(17,10),(17,11),(17,12),(17,13),(17,15),
       #          (18,8),(18,9),(18,10),(18,11),(18,12),(18,13),(18,14),(18,15),(18,18),(18,20),(18,21),(18,22),(18,23),
       #          (19,2),(19,3),(19,9),(19,10),(19,11),(19,12),(19,13),(19,14),(19,18),(19,19),(19,20),(19,21),(19,22),(19,23),
       #          (20,0),(20,1),(20,2),(20,3),(20,4),(20,5),(20,8),(20,9),(20,10),(20,11),(20,12),(20,13),(20,14),(20,15),
       #          (20,18),(20,19),(20,20),(20,21),(20,22),(20,23),
       #          (21,0),(21,1),(21,2),(21,3),(21,4),(21,5),(21,8),(21,9),(21,10),(21,11),(21,12),(21,13),(21,14),(21,15),
       #          (21,18),(21,19),(21,20),(21,21),(21,22),(21,23),
       #          (22,0),(22,1),(22,2),(22,3),(22,4),(22,5),(22,8),(22,9),(22,10),(22,11),(22,12),(22,13),(22,14),(22,15),
       #          (22,18),(22,19),(22,20),(22,21),(22,22),(22,23),
       #          (23,0),(23,1),(23,2),(23,3),(23,4),(23,5),(23,10),(23,11),(23,12),(23,13),(23,19),(23,20),(23,21),(23,22),(23,23),
       #          (24,0),(24,1),(24,2),(24,3),(24,4),(24,5),(24,10),(24,11),(24,12),(24,13),(24,18),(24,19),(24,20),(24,21),(24,22),(24,23)]

               # self.die1 = [1, self.scaleImage(self.loadImage('Images/Dice/die1.png'), 0.40)]
        # self.die2 = [2, self.scaleImage(self.loadImage('Images/Dice/die2.png'), 0.40)]
        # self.die3 = [3, self.scaleImage(self.loadImage('Images/Dice/die3.png'), 0.40)]
        # self.die4 = [4, self.scaleImage(self.loadImage('Images/Dice/die4.png'), 0.40)]
        # self.die5 = [5, self.scaleImage(self.loadImage('Images/Dice/die5.png'), 0.40)]
        # self.die6 = [6, self.scaleImage(self.loadImage('Images/Dice/die6.png'), 0.40)]
        # self.dice = [self.die1[0], self.die2[0], self.die3[0], self.die4[0], self.die5[0], self.die6[0]]