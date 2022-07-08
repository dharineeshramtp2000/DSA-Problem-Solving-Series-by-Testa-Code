def mostCommonWord(para, banned):
    bannedWords = set(banned)
    counter = {}

    i = 0

    maxFrequency = 0
    commonWord = None

    while i < len(para):

        j = i

        while j < len(para) and para[j].isalpha():
            j += 1

        currentWord = para[i : j].lower()
        i = i + 1 if i == j else j

        if len(currentWord) > 0:

            if currentWord in bannedWords:
                continue

            if currentWord not in counter:
                counter[currentWord] = 0

            counter[currentWord] += 1

            if counter[currentWord] > maxFrequency:
                commonWord = currentWord
                maxFrequency = counter[currentWord]

    return commonWord
