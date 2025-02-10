class Solution:
    def removeElement(self, nums,value):
        
        k = 0
        
        num = []
        for i in range(len(nums)):
         if(value != nums[i]):
           nums[k] = nums[i]
           k +=1
        return k   
        