def main():
    numbers = [1,2,3,4,5]
    print(subsets(numbers))

def subsets(nums):
    res, sol = [],[]


    def backtrack(i):
        if i == len(nums):
            res.append(sol[:])
            return
        
        # Dont pick nums[i]
        backtrack(i+1)

        # Pick the nums[i]
        sol.append(nums[i])
        backtrack(i + 1)
        sol.pop() # Reversing the decision of picking the number
    
    backtrack(0)
    return res


main()