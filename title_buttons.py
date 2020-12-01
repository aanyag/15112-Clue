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