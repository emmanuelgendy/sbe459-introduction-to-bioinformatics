def RNA2AminoAcids(strand):
    length = len(strand)
    completeAminoAcids = int(length/3.0)
    if length%3 != 0:
        remainingBases = length - (3*completeAminoAcids)
    return completeAminoAcids, remainingBases

## Extra adds to the function in case I wanted to print out the Amino Acids in the sequence
## or the remaining Bases

    # aminoAcidsInStrand = []
    # for i in range(0,completeAminoAcids*3,3):
    #     aminoAcid = strand[i]+strand[i+1]+strand[i+2]
    #     aminoAcidsInStrand.append(aminoAcid)
    # if length%3 != 0:
    #     remainingPairs = length - completeAminoAcids*3
    #     print(remainingPairs)
    #     if remainingPairs == 1:
    #         incompleteSequence = strand[completeAminoAcids*3]
    #     else:
    #         incompleteSequence = strand[completeAminoAcids*3]+strand[completeAminoAcids*3+1]
    #     return len(aminoAcidsInStrand), incompleteSequence
    # return len(aminoAcidsInStrand), 0


## Testing
# print(RNA2AminoAcids("AAASJFJBEVJSOTANGNEIGNA"))