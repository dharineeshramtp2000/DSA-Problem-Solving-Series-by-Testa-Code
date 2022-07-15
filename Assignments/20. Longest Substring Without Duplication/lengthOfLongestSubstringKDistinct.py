def lengthOfLongestSubstringKDistinct(s, k):
    maxLength = 0

    startIdx = 0

    counter = {}

    for endIdx in range(len(s)):

        endChar = s[endIdx]

        insertIntoHashTable(endChar, counter)

        while startIdx <= endIdx and len(counter) > k:

            startChar = s[startIdx]

            deleteFromHashTable(startChar, counter)


            startIdx += 1

        maxLength = max(maxLength, endIdx - startIdx + 1)

    return maxLength






def insertIntoHashTable(char, table):

    if char not in table:
        table[char] = 0

    table[char] += 1



def deleteFromHashTable(char, table):
    if char not in table:
        return

    table[char] -= 1

    if table[char] == 0:
        del table[char]
