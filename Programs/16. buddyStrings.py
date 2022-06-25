def buddyStrings(s, goal):

    if len(s) != len(goal):
        return False

    n = len(s)

    if s == goal:
        seen = set()

        for char in s:
            if char in seen:
                return True
            seen.add(char)
        return False

    pairs = []

    for idx in range(n):
        charS = s[idx]
        charGoal = goal[idx]

        if charS != charGoal:
            pairs.append([charS, charGoal])

        if len(pairs) >= 3:
            return False


    return len(pairs) == 2 and pairs[0][0] == pairs[1][1] and pairs[0][1] == pairs[1][0]
