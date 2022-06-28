def isIsomorphic(s, t):

    if len(s) != len(t):
        return False

    mapS = {}
    mapT = {}

    for idx in range(len(s)):
        charS = s[idx]
        charT = t[idx]

        if charS not in mapS:
            mapS[charS] = charT

        if charT not in mapT:
            mapT[charT] = charS

        if mapS[charS] != charT or mapT[charT] != charS:
            return False

    return True
