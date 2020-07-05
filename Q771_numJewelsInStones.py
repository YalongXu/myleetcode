def numJewelsInStones(J: str, S: str) -> int:
    abcDict = {}
    for ch in J:
        abcDict[ch] = True
    numJewels = 0
    for ch in S:
        if abcDict.get(ch) is not None:
            numJewels += 1
    return numJewels


##############3
J = "aA"
S = "aAAbbbbb"
print(numJewelsInStones(J, S))
