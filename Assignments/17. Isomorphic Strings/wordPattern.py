def wordPattern(pattern, s):
    charMap = {}
    wordMap = {}

    words = s.split(" ")

    if len(words) != len(pattern):
        return False


    for idx in range(len(words)):
        word = words[idx]

        charPattern = pattern[idx]

        if charPattern not in charMap:
            charMap[charPattern] = word

        if word not in wordMap:
            wordMap[word] = charPattern

        if charMap[charPattern] != word or wordMap[word] != charPattern:
            return False

    return True
