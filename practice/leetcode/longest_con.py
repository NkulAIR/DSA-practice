numbers = [1,2,3,4,2,3,4,5,6,1]

l = 0
max_len = 0

best_l = 0
best_r = 0



numbers = [1, 2, 3, 4, 2, 3, 4, 5, 6, 1]

# Start our "frame" with the first number
current_streak = [numbers[0]]
longest_streak = [numbers[0]]

# Loop through the rest of the numbers (starting from the 2nd one)
for number in numbers[1:]:
    last_number = current_streak[-1]

    if number > last_number:
        print(number, last_number)
        current_streak.append(number)
        
    else:
        current_streak = [number]
    
    if len(current_streak) > len(longest_streak):
        longest_streak = list(current_streak)

print("Longest Increasing Subset:", longest_streak)

# def selection_sort(nums):
#     smallest = nums[0]
#     smallest_index = 0
#     for i in range(1,len(nums)):
#         if nums[i] < smallest:
#             smallest = nums[i]
#             smallest_index = i
#     return smallest_index






# def smallest(nums):
#     sorted_a = []
#     for i in range(len(nums)):
#         smallest = selection_sort(nums)
#         sorted_a.append(smallest)
#         if len(nums) >= 1:
#             sorted_a.pop(smallest)

#     return sorted_a

# nums = [43,5,3,4,12,89,155]
# print(smallest(nums))