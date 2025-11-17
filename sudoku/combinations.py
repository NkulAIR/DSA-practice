def main():
    print(combinations(3, 2))

def combinations(n, k):
    # res, sol = [],[]

    # def backtrack(i):
    #     nums = [i for i in range(1, n+1)]
    #     if i == len(nums):
    #         if len(sol) == k:
    #             res.append(sol[:])
    #         return

    #     backtrack(i+1)
        
    #     if len(sol) < k:
    #         sol.append(nums[i])
    #         backtrack(i+1)
    #         sol.pop()

        
        
    # backtrack(0)
    # return res



    # Actual solution
    res = []

    def backtrack(start, combo):
        if len(combo) == k:
            res.append(combo[:])
            return
        
        for i in range(start, n+1):
            combo.append(i)
            backtrack(i + 1, combo)
            combo.pop()




    backtrack(1, [])
    return res
    # Stop when the len of res == k:

main()