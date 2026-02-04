def biggest_l(letters, target):
    biggest = letters[0]

# else:
#     if biggest <= target:
#         return biggest
    
#     l = 0
#     r = len(letters)
#     mid = l + r // 2
#     biggest = letters[0]

#     while l < r and len(letters) > 0:
#         # if ord(letters[mid]) < ord(target):
#         if ord(letters[l]) >= ord(target):
#             biggest = letters[l]
#             return biggest
#         elif ord(letters[mid]) < ord(target):
#             r = mid
#         elif ord(letters[mid]) > ord(target):
#             l = mid
        
#         print(letters)
#         l += 1
#         # if ord(letters[mid]) > ord(target):
#         #     letters = letters[:mid]
#         # if ord(letters[mid]) == ord(target):
#         #     return letters[mid]

#     return biggest

# print(biggest_l(["c", "f", "j"], "x"))

def two_sum(nums, target):
    l = 0
    r = len(nums)-1
    indices = []

    while l < len(nums):
        if nums[l] + nums[r] == target:
            indices.append(l)
            indices.append(r)
        l += 1
        r -= 1
    
    return indices

print(two_sum([1,2,3,4,5], 7))