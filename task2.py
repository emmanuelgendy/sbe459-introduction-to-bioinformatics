import numpy as np

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

def maximumValue(gapleft, gapUp, diagonal, matchBool, matchScore, mismatchScore, gapScore):

    if matchBool:
        s = diagonal+matchScore
    else:
        s = diagonal+mismatchScore
    wU = gapUp+gapScore
    wL = gapleft+gapScore

    if max(s, wU, wL) == s:
        highestValue = "s"

    elif max(s, wU, wL) == wU:
        highestValue = "wU"

    elif max(s, wU, wL) == wL:
        highestValue = "wL"

    return highestValue, max(s, wU, wL)


def globalAlignment(strandA,strandB, matchScore, mismatchScore, gapScore):
    strandA = " " + strandA
    strandB = " " + strandB
    lengthA = len(strandA)
    lengthB = len(strandB)
    matrix = np.empty((lengthA, lengthB), int)
    matrixArrows = np.empty((lengthA, lengthB), dtype="<U10")
    matrix[0][0] = 0

    # Matrix Initialization
    for i in range(1, lengthA):
        matrix[i][0] = i*gapScore
        matrixArrows[i][0] = "wU"
    for j in range(1, lengthB):
        matrix[0][j] = j*gapScore
        matrixArrows[0][j] = "wL"

    # Matrix Filling
    for i in range(1, lengthA):
        for j in range(1, lengthB):
            matrixArrows[i][j], matrix[i][j] = maximumValue(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1], strandA[i] == strandB[j], matchScore, mismatchScore, gapScore)
    print(matrix)
    print(matrixArrows)
    backTracking(strandA, strandB, matrix, matrixArrows)


def backTracking(strandA, strandB, matrix, matrixArrows):
    lengthA = len(strandA)
    lengthB = len(strandB)
    alignmentA = ""
    alignmentB = ""
    i = lengthA-1
    j = lengthB-1

    while(i>0 or j>0):

        if matrixArrows[i][j] == "s":
            alignmentA = alignmentA.__add__(strandA[i])
            alignmentB = alignmentB.__add__(strandB[j])
            i = i-1
            j = j-1
            if (i == -1) or (j == -1):
                break

        elif matrixArrows[i][j] == "wU":
            alignmentA = alignmentA.__add__(strandA[i])
            alignmentB = alignmentB.__add__("-")
            i = i-1
            if i == -1:
                break

        elif matrixArrows[i][j] == "wL":
            alignmentA = alignmentA.__add__("-")
            alignmentB = alignmentB.__add__(strandB[j])
            j = j-1
            if j == -1:
                break

    alignmentA = alignmentA.__add__(strandA[0])
    alignmentB = alignmentB.__add__(strandB[0])

    alignmentA = reverse(alignmentA)
    alignmentB = reverse(alignmentB)

    print("Best score = " + str(matrix[lengthA-1][lengthB-1]))
    print(alignmentA)
    print(alignmentB)



globalAlignment("CTATTGAACAT","CTATTGACGTAACAT",4,-1,-3)