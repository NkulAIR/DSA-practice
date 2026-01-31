
def combinations(cand, target)
    res, combo = [], []

    def backtrack(start, combo):
        if sum(combo) == target:
            res.append(combo[:])
            return
        
    
        backtrack(i + 1, combo)
        combo.pop()
    
    backtrack(0, [])
    return res