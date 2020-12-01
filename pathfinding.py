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