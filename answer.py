#choose an answer at random from all the given cards
def allCards():
    allCards = {suspects: {'Col. Mustard', 'Prof. Plum', 'Mr. Green', 
                            'Mrs. Peacock', 'Miss Scarlett', 'Mrs. White'},
                weapons: {'Knife', 'Candlestick', 'Revolver', 'Rope', 
                            'Lead Pipe', 'Wrench'},
                rooms: {'Hall', 'Lounge', 'Dining Room', 'Kitchen',
                            'Ball Room', 'Conservatory', 'Billiard Room',
                            'Library', 'Study'}}

    suspect = random.randint(0, 5)
    weapon = random.randint(0, 5)
    room = random.randint(0, 8)
    answer = {allCards[suspects][suspect], allCards[weapons][weapon], 
                allCards[rooms][room]}