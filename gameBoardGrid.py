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
            if self.player1 == (row, col) or self.player1end == (row, col):
                self.fillColor = self.playerColor
            else:
                self.fillColor = ""
            canvas.create_rectangle(x1, y1, x2, y2, fill = self.fillColor)