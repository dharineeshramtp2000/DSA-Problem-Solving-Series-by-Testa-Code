def findAllAnagrams(s, p):

    targetFrequency = getFrequency(p)

    targetLength = len(p)

    currentFrequency = [0] * 26

    startPositions = []

    for idx, char in enumerate(s):

        currentFrequency[ord(char) - ord("a")] += 1

        if idx - targetLength >= 0:

            currentFrequency[ord(s[idx - targetLength]) - ord("a")] -= 1

        if currentFrequency == targetFrequency:
            startPositions.append(idx - targetLength + 1)

    return startPositions    




def getFrequency(string):
    counter = [0] * 26

    for char in string:
        counter[ord(char) - ord("a")] += 1

    return counter
