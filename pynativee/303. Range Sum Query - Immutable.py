class NumArray:

    def __init__(self, nums):
        self.nums = nums
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])
    
if __name__ == "__main__":
    
    NumArray = NumArray( [-2, 0, 3, -5, 2, -1])
    print(NumArray.sumRange(0, 2))
    print(NumArray.sumRange(2, 5))
    print(NumArray.sumRange(0,5))
    
    

        