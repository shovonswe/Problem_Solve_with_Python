class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            if r[0] <= target <= r[-1]:
                left, right = 0, len(r) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if r[mid] == target:
                        return True
                    elif r[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

        return False
Solution = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution.searchMatrix(matrix, target))

         