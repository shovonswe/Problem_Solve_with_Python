#Brute force(n)
class solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        else:
            return -1
        
Solution = solution()
nums = [-1,0,3,5,9,12]
target = 9
print(Solution.search(nums,target))        



#Optimal(logn)
class solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        
        while l <= r:
        
            if nums[l] == target:
                return l
            else:
                l += 1
            if nums[r] == target:
                return r
            else:
                r -= 1
        return -1     
    
    
Solution = solution()
nums = [-1,0,3,5,9,12]
target = 9
print(Solution.search(nums,target))


