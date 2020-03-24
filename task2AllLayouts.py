import numpy as np
import copy             ## This is used for when a cell has more than one arrow

def globalAlignment(strandA, strandB, matchScore, mismatchScore, gapScore):
    strandA = " " + strandA
    strandB = " " + strandB
    lengthA = len(strandA)
    lengthB = len(strandB)
    matrix = np.empty((lengthA, lengthB), int)
    ## Design 3D Array for arrows direction, First layer is diagonal, Second layer is Gap Up, Third layer is Gap Left
    arrowsDirection = np.zeros((lengthA, lengthB, 3), int)
    ## 2D Array to have number of arrows at each cell
    numberOfArrows = np.zeros((lengthA, lengthB))
    matrix[0][0] = 0

    # Matrix Initialization
    for i in range(1, lengthA):
        matrix[i][0] = i * gapScore
        arrowsDirection[i][0][2] = 1
    for j in range(1, lengthB):
        matrix[0][j] = j * gapScore
        arrowsDirection [0][j][1] = 1

    # Matrix Filling
    for i in range(1, lengthA):
        for j in range(1, lengthB):
            arrowsDirection[i][j], matrix[i][j] = maximumValue(matrix[i][j - 1], matrix[i - 1][j],
                                                            matrix[i - 1][j - 1], strandA[i] == strandB[j],
                                                            matchScore, mismatchScore, gapScore)
            numberOfArrows[i][j] = np.sum(arrowsDirection[i][j])
    print(matrix)
    print(arrowsDirection)
    print(numberOfArrows)
    alignmentA = list()
    alignmentB = list()
    alignmentA.append("")
    alignmentB.append("")
    alignmentA, alignmentB = backTracking(lengthA-1,lengthB-1,strandA, strandB, alignmentA, alignmentB, 0, arrowsDirection, numberOfArrows)

    for i in range(len(alignmentA)):
        if len(alignmentA) == 1:
            alignmentA[i] = reverse(alignmentA[i])
            alignmentB[i] = reverse(alignmentB[i])
            print("Layout:")
            print(alignmentA[i])
            print(alignmentB[i])
        else:
            alignmentA[i] = reverse(alignmentA[i])
            alignmentB[i] = reverse(alignmentB[i])
            print("Layout (" + str(i+1) + "):")
            print(alignmentA[i])
            print(alignmentB[i])

## To calculate the maximum value output from each cell

def maximumValue(gapleft, gapUp, diagonal, matchBool, matchScore, mismatchScore, gapScore):

    arrowsDirectionVector = np.zeros((3))
    if matchBool:
        s = diagonal+matchScore
    else:
        s = diagonal+mismatchScore
    wU = gapUp+gapScore
    wL = gapleft+gapScore

    if max(s, wU, wL) == s:
        arrowsDirectionVector[0] = 1

    if max(s, wU, wL) == wU:
        arrowsDirectionVector[2] = 1

    if max(s, wU, wL) == wL:
        arrowsDirectionVector[1] = 1

    return arrowsDirectionVector, max(s, wU, wL)

def backTracking(i, j, strandA, strandB, alignmentA, alignmentB, counter, arrowsDirection, numberOfArrows):
    while(i>0 and j>0):

        if numberOfArrows[i][j] == 1:       ## If there is only one arrow in this cell
            if arrowsDirection[i][j][0] == 1:   ## If direction is diagonal
                alignmentA[counter] = alignmentA[counter].__add__(strandA[i])
                alignmentB[counter] = alignmentB[counter].__add__(strandB[j])
                i = i-1
                j = j-1

            elif arrowsDirection[i][j][1] == 1: ## If direction is left
                alignmentA[counter] = alignmentA[counter].__add__("-")
                alignmentB[counter] = alignmentB[counter].__add__(strandB[j])
                j = j - 1

            elif arrowsDirection[i][j][2] == 1: ## If direction is up
                alignmentA[counter] = alignmentA[counter].__add__(strandA[i])
                alignmentB[counter] = alignmentB[counter].__add__("-")
                i = i - 1
        elif numberOfArrows[i][j] > 1:      ## If there was more than one arrow in this cell
            alignmentA.append(alignmentA[counter])
            alignmentB.append(alignmentB[counter])
            if arrowsDirection[i][j][0] == 1:   ## If direction is diagonal
                alignmentA[counter] = alignmentA[counter].__add__(strandA[i])
                alignmentB[counter] = alignmentB[counter].__add__(strandB[j])
                numberOfArrows[i][j] -= 1
                arrowsDirection[i][j][0] -= 1
                x,y = backTracking(i, j, strandA, strandB, alignmentA, alignmentB, len(alignmentA)-1, copy.deepcopy(arrowsDirection),
                             copy.deepcopy(numberOfArrows))
                i = i-1
                j = j-1

            elif arrowsDirection[i][j][1] == 1:  ## If direction is left
                alignmentA[counter] = alignmentA[counter].__add__("-")
                alignmentB[counter] = alignmentB[counter].__add__(strandB[j])
                numberOfArrows[i][j] -= 1
                arrowsDirection[i][j][1] -= 1
                x,y =backTracking(i, j, strandA, strandB, alignmentA, alignmentB, len(alignmentA)-1, copy.deepcopy(arrowsDirection),
                             copy.deepcopy(numberOfArrows))
                j = j - 1
            elif arrowsDirection[i][j][2] == 1: ## If direction is up
                alignmentA[counter] = alignmentA[counter].__add__(strandA[i])
                alignmentB[counter] = alignmentB[counter].__add__("-")
                numberOfArrows[i][j] -= 1
                arrowsDirection[i][j][2] -= 1
                x,y =backTracking(i, j, strandA, strandB, alignmentA, alignmentB, len(alignmentA)-1, copy.deepcopy(arrowsDirection),
                             copy.deepcopy(numberOfArrows))
                i = i - 1

    return alignmentA, alignmentB

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

globalAlignment("CTATTGAACAT", "CTATTGACGTAACAT", 4, -1, -3)