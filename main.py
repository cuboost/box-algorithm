# Variables
# boxNumber = int(input("Number of boxes: "))
boxNumber = 3

column1 = []
column2 = []
column3 = []

for i in range(boxNumber):
    column1.append(i + 1)

lastBoxMoved = 0

# Checks
def getLastBoxInColumn(column):
    return column[-1]

def columnIsEmpty(column):
    if len(column) == 0:
        return True
    else:
        return False

def canBePlacedInColumn(number, column):
    if not columnIsEmpty(column) and getLastBoxInColumn(column) > number:
        return False
    else:
        return True

# Movement
def moveLastBoxfromColumn(initialColumn, finalColumn):
    if columnIsEmpty(initialColumn):
        print("The initial column contains no boxes! This step was skipped.\n")
        return
    if not canBePlacedInColumn(getLastBoxInColumn(initialColumn), finalColumn):
        print("The final column contains a smaller box than the one added! This step was skipped.\n")
        return
    
    global lastBoxMoved
    lastBoxMoved = initialColumn.pop()
    print("Box moved: ", lastBoxMoved)
    print("\n")
    finalColumn.append(lastBoxMoved)
    printColumns()

# Column Select
def column(number):
    if number == 1:
        return column1
    elif number == 2:
        return column2
    elif number == 3:
        return column3
    else:
        print("Invalid column number")

# Printing
def printColumns():
    for i in range(1,4):
        print(f"Column {i}:")
        print(*column(i), sep="\n")
    print("\n \n")

# Init
print("STEPS: \n")
printColumns()

# Algorithm
moveLastBoxfromColumn(column1,column3)

for i in range(5):
    possibleInitialColumns=[]
    possibleFinalColumn=None

    for i in range(1,4):
        currentColumn = column(i)
        if not columnIsEmpty(currentColumn) and getLastBoxInColumn(currentColumn) != lastBoxMoved:
            possibleInitialColumns.append(i)

    print("Possible columns from which you can move the last number:", possibleInitialColumns)


    for possibleInitialColumn in possibleInitialColumns.copy():
        found_final_column = False
        for i in range(1,4):
            currentColumn = column(i)
            if i != possibleInitialColumn and canBePlacedInColumn(getLastBoxInColumn(column(possibleInitialColumn)), currentColumn):
                if (columnIsEmpty(currentColumn) or(getLastBoxInColumn(column(possibleInitialColumn)) - getLastBoxInColumn(currentColumn)  == 1)):
                    possibleFinalColumn=i
                    found_final_column = True
                    break
        if found_final_column:
            break
        else:
            del possibleInitialColumns[0]

    print("Column from which you can move the last number:", possibleInitialColumns[0])
    print("Column to which you can move the last number:", possibleFinalColumn)

    moveLastBoxfromColumn(column(possibleInitialColumns[0]), column(possibleFinalColumn))