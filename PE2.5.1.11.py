rowOne = input("Enter 9 digits for row one of the sudoko puzzle: ")
while len(rowOne) != 9:
    rowOne = input("Invalid Input: Enter 9 digits for row one of the sudoko puzzle: ")

rowTwo = input("Enter 9 digits for row two of the sudoko puzzle: ")
while len(rowTwo) != 9:
    rowTwo = input("Invalid Input: Enter 9 digits for row two of the sudoko puzzle: ")

rowThree = input("Enter 9 digits for row three of the sudoko puzzle: ")
while len(rowThree) != 9:
    rowThree = input("Invalid Input: Enter 9 digits for row three of the sudoko puzzle: ")

rowFour = input("Enter 9 digits for row four of the sudoko puzzle: ")
while len(rowFour) != 9:
    rowFour = input("Invalid Input: Enter 9 digits for row four of the sudoko puzzle: ")

rowFive = input("Enter 9 digits for row five of the sudoko puzzle: ")
while len(rowFive) != 9:
    rowFive = input("Invalid Input: Enter 9 digits for row five of the sudoko puzzle: ")

rowSix = input("Enter 9 digits for row six of the sudoko puzzle: ")
while len(rowSix) != 9:
    rowSix = input("Invalid Input: Enter 9 digits for row six of the sudoko puzzle: ")

rowSeven = input("Enter 9 digits for row seven of the sudoko puzzle: ")
while len(rowSeven) != 9:
    rowSeven = input("Invalid Input: Enter 9 digits for row seven of the sudoko puzzle: ")

rowEight = input("Enter 9 digits for row eight of the sudoko puzzle: ")
while len(rowEight) != 9:
    rowEight = input("Invalid Input: Enter 9 digits for row eight of the sudoko puzzle: ")

rowNine = input("Enter 9 digits for row eight of the sudoko puzzle: ")
while len(rowNine) != 9:
    rowNine = input("Invalid Input: Enter 9 digits for row nine of the sudoko puzzle: ")

sudokoBoard = [rowOne,rowTwo,rowThree,rowFour,rowFive,rowSix,rowSeven,rowEight,rowNine]

def validRow(sudokoBoard):

    for row in sudokoBoard:
        rowTotal = 0
        for digit in row:
            rowTotal += int(digit)
        if rowTotal != 45:
            return 0
    return 1
    
def validColumn(sudokoBoard):
    i = 0
    while i < 9:
        columnTotal = int(rowOne[i]) + int(rowTwo[i]) + int(rowThree[i]) + int(rowFour[i]) + int(rowFive[i]) + int(
            rowSix[i]) + int(rowSeven[i]) + int(rowEight[i]) + int(rowNine[i])
        if columnTotal != 45:
            return 0
        i += 1
    return 1

def validTile(sudukoBoard,start,rowEnd,firstIndex,secondIndex,thirdIndex):
    tileTotal = 0
    while start < rowEnd:
        tileTotal = tileTotal + int(sudukoBoard[start][firstIndex]) + int(sudukoBoard[start][secondIndex]) + int(
            sudukoBoard[start][thirdIndex])
        start += 1
    if tileTotal != 45:
        return 0
    return 1

if validRow(sudokoBoard) + validColumn(sudokoBoard) + validTile(sudokoBoard,0,3,0,1,2) + validTile(\
        sudokoBoard,3,6,0,1,2) + validTile(sudokoBoard,6,9,0,1,2) + validTile(sudokoBoard,0,3,3,4,5) + validTile(\
        sudokoBoard,3,6,3,4,5) + validTile(sudokoBoard,6,9,3,4,5) + validTile(\
        sudokoBoard,0,3,6,7,8) + validTile(sudokoBoard,3,6,6,7,8) + validTile(sudokoBoard,6,9,6,7,8) == 11:
    print("Yes")
else:
    print("No")