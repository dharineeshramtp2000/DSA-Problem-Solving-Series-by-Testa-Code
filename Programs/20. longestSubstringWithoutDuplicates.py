def longestSubstringWithoutDuplicates(string):
    bounds = [0,0]

    startIdx = 0

    positions = {}

    for idx, char in enumerate(string):

        if char in positions:
            startIdx = max(startIdx, positions[char] + 1)

        if idx - startIdx > bounds[1] - bounds[0]:
            bounds = [startIdx, idx]

        positions[char] = idx


    return string[bounds[0] : bounds[1] + 1]

    
