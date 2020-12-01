#draws the grid, title, buttons, instructions, notepad, dice, and board
def redrawAll(self, canvas):
    self.drawAlgorithmicBoard(canvas)
    canvas.create_image(self.width / 2, self.height - 373,
                            image = ImageTk.PhotoImage(self.boardScaled))
    canvas.create_image(self.width - 200, self.height / 2,
                            image = ImageTk.PhotoImage(self.notepadScaled))
    canvas.create_image(self.width - 45, self.height - 700,
                            image = ImageTk.PhotoImage(self.currDice))
    
    self.drawNotepadGrid(canvas)
    self.drawBoardGrid(canvas)
    self.drawTitle(canvas)
    self.drawButtons(canvas)
    self.instructions(canvas)