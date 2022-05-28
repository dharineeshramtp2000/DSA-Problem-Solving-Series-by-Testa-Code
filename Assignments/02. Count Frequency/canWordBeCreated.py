def canWordBeCreated(language, word):
    characterCount = getCharacterCount(language)

    for char in word:
        if char not in characterCount:
            return False

        characterCount[char] -= 1

        if characterCount[char] < 0:
            return False

    return True



def getCharacterCount(language):
    counter = {}

    for char in language:
        if char not in counter:
            counter[char] = 0

        counter[char] += 1

    return counter
