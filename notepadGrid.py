#draws the notepad's grid so the user can fill in green and red
def drawNotepadGrid(self, canvas):
    for row in range(self.suspectRows):
        canvas.create_rectangle(1275, 75 + 18.5 * row, 1290, 93.5 + 18.5 * row)
    for row in range(self.weaponsRows):
        canvas.create_rectangle(1274, 232 + 18.5 * row, 1289, 250.5 + 18.5 * row)
    for row in range(self.roomsRows):
        canvas.create_rectangle(1274, 479 + 18.75 * row, 1289, 497.75 + 18.75 * row)