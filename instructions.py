#displays instructions when "HELP" button is clicked
def instructions(self, canvas):
    if self.showInstructions == True:
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