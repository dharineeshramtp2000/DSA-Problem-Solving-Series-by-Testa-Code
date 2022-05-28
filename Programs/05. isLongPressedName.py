def isLongPressedName(name, typed):
    i = j = 0

    while i < len(name) and j < len(typed):
        charName = name[i]
        charTyped = typed[j]

        if charName != charTyped:
            return False

        charNameCounter = 0

        while i < len(name) and name[i] == charName:
            i += 1
            charNameCounter += 1

        charTypedCounter = 0

        while j < len(typed) and typed[j] == charTyped:
            j += 1
            charTypedCounter += 1

        if charTypedCounter < charNameCounter:
            return False

    return i == len(name) and j == len(typed)
