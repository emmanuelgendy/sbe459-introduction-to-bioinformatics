def RNA2AminoAcids(strand):
    length = len(strand)
    completeAminoAcids = int(length/3.0)
    aminoAcidsInStrand = []
    for i in range(0,completeAminoAcids*3,3):
        aminoAcid = strand[i]+strand[i+1]+strand[i+2]
        aminoAcidsInStrand.append(aminoAcid)
    if length%3 != 0:
        remainingPairs = length - completeAminoAcids*3
        print(remainingPairs)
        if remainingPairs == 1:
            incompleteSequence = strand[completeAminoAcids*3]
        else:
            incompleteSequence = strand[completeAminoAcids*3]+strand[completeAminoAcids*3+1]
        return aminoAcidsInStrand, incompleteSequence
    return aminoAcidsInStrand


# def importSequenceFromTextFile(path):
#     with open(path, 'r') as file:
#         data = file.read().replace('\n', '')
#     return data


def DNA2RNA(dnaStrand):
    length = len(dnaStrand)
    rnaStrand = list()
    for i in range(length):
        if dnaStrand[i] == 'T':
            rnaStrand.append('U')
        else:
            rnaStrand.append(dnaStrand[i])
    return rnaStrand


def DNA2RNABuiltIn(dnaStrand):
    return dnaStrand.replace('T', 'U')
