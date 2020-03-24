def cg_content(strand):
    length = len(strand)
    countC = 0
    countG = 0
    for i in range(length):
        if strand[i] == "C":
            countC += 1
        if strand[i] == "G":
            countG += 1
    return countC+countG


def cg_content_BuiltIn(strand):
    return strand.count("C")+strand.count("G")

## Testing

# print(cg_content("CJGJSOGCQAOTHCGRID"))
# print(cg_content_BuiltIn("CJGJSOGCQAOTHCGRID"))