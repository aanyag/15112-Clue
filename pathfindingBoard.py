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
            #the path taken by the user is displayed as green
            elif (row,col) in self.path:
                canvas.create_rectangle(x1, y1, x2, y2, fill = "green")
            canvas.create_rectangle(x1, y1, x2, y2)