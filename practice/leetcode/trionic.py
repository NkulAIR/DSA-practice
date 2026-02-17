
def trionic(nums):
    l,p,q = 0, 0, 0

    if nums[1] < nums[0]:
        return False
    elif len(nums) <= 3:
        return False

    i = 1
    for j in range(i, len(nums)):
        while nums[i] > nums[i-1]:
            i += 1
            l = nums[:i]
            p = nums[i:]
    
    r = 0
    if l == 0 or p == 0 or q == 0:
        return False

    for k in range(len(p)):
        while p[r] > p[r+1]:
            r += 1
            q = p[r:]


    if l == 0 or p == 0 or q == 0:
        return False
    else:
        return True
    
        


        


            
        
    # print(nums[:p])


print(trionic([1,1,1,9]))