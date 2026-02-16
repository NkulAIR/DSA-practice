def longestBalanced(nums): # -> int
    even = len([i for i in set(nums) if i % 2 == 0])
    odd = len([i for i in set(nums) if i % 2 != 0])
    l = 0
    r = len(nums)-1
    subsets = {i for i in range(len(nums))}

    if even == 0 or odd == 0:
        return 0
    if even == odd:
        return len(nums)
    else:
        while l <= len(nums):
            even = len([i for i in set(nums[:mid]) if i % 2 == 0])
            odd = len([i for i in set(nums[:mid]) if i % 2 != 0])
            mid = l + r // 2
            
            # if even == odd count, add subsets to dictionary
            return len(nums[mid:])


print(longestBalanced([1,2,3,2]))
print(longestBalanced([4,2,5,3,6,8,9,10]))

