def solve(s):
    vowels = {"a": 0, "e":0, "i": 0, "o": 0, "u": 0}
    largest = [0]
    
    for i in range(len(s)):
        char = s[i]
        
        if (char in vowels):
            largest[-1] += 1
        else:
            largest.append(0)
                    
    return max(largest)