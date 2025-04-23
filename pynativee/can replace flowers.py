class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        size = len(flowerbed)

        for i in range(size):
            if flowerbed[i] == 0:
                if i == 0:
                     prev = 0
                else:
                    prev = flowerbed[i - 1]
                if i == size - 1:
                    next = 0
                else:
                    next = flowerbed[i + 1]

                if prev == 0 and next == 0:
                    flowerbed[i] = 1
                    count += 1

        return count >= n
Solution = Solution()
flowerbed = [1,0,0,0,1]
n = 1
print(Solution.canPlaceFlowers(flowerbed,n))