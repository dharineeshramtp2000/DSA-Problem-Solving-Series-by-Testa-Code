def firstUniqueCharacter(s):
    memory = {}
    
    for char in s:
        if char not in memory:
            memory[char] = False
            continue


        memory[char] = True


    for idx, char in enumerate(s):
        if memory[char] == False:
            return idx

    return -1
