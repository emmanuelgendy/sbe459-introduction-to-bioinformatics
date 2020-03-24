def DNA_to_RNA(dnaStrand):
    length = len(dnaStrand)
    rnaStrand = list()
    for i in range(length):
        if dnaStrand[i] == 'T':
            rnaStrand.append('U')
        else:
            rnaStrand.append(dnaStrand[i])
    return ''.join(rnaStrand)


def DNA_to_RNA_BuiltIn(dnaStrand):
    return dnaStrand.replace('T', 'U')

## Testing

# print(DNA_to_RNA("ACTGRRTTTAGASEGTRAG"))
# print(DNA_to_RNA_BuiltIn("ACTGRRTTTAGASEGTRAG"))
