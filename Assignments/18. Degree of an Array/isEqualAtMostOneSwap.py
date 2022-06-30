def isEqualAtMostOneSwap(s1, s2):
    if len(s1) != len(s2):
        return False

    if s1 == s2:
        return True

    pairs = []

    for idx in range(len(s1)):

        charOne = s1[idx]
        charTwo  = s2[idx]


        if charOne != charTwo:
            pairs.append([charOne, charTwo])

        if len(pairs) > 2:
            return False

    return len(pairs) == 2 and pairs[0][0] == pairs[1][1] and pairs[0][1] == pairs[1][0]
