def findDisappearedNumbers(nums):
    return list(set(range(1, len(nums) + 1)) ^ set(nums))


nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))  
