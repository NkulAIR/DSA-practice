#Tools

import itertools



def find_smallest(nums):
    smallest  = nums[0]
    smallest_index = 0

    for i in range(1, len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
            smallest_index = i

    return smallest_index

def selection_sort(nums):
    new_arr = []
    for i in range(len(nums)):
        smallest = find_smallest(nums)
        new_arr.append(nums.pop(smallest))
    return new_arr

def div_conq(nums):
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return nums[0]
    
    else:
        return nums[0] + div_conq(nums[1:])

print(div_conq([2,4,6]))

def quick_sort(nums):
    l = 0
    # mid = l + len(nums) // 2
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums[1:] if i <= pivot]
        greater = [i for i in nums[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


# print(quick_sort([5,6,7,34,12,11,23]))

def binary_search(nums, t):
    l = 0
    r = len(nums)

    while l <= r:
        mid = l + r // 2
        if nums[mid] == t:
            return mid
        if nums[mid] > t:
            r = mid - 1
        else:
            l = mid + 1

    return None 



# print(binary_search([5,6,7,12,11,24,4], 4))


groups = []
nums  = [2,3,4,5]

#All posible combinations
pairs = list(itertools.combinations(nums, 2))
# print(pairs)



# Group by no of occurence
key = (lambda x:x )
data = ["a", "a", "b", "b", "c", "d", "e"]
for key, group in itertools.groupby(data): # Look up the things you can group by
    group_list = list(group)
    print(f'{key}: {group_list}')

pairs = [12,1,34,2,6]
# Sorting a list with lambda
print(pairs.sort(key=lambda x: x))


    
    

# print(selection_sort([2,5,6,4,5,7]))
# print(selection_sort([5,6,7,8,12,1]))


# def quicksort(nums):
