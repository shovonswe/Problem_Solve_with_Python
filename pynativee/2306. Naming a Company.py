from collections import defaultdict

class Solution:
    def distinctNames(self, ideas):
        groups = defaultdict(set)

     
        for word in ideas:
            groups[word[0]].add(word[1:])

        letters = list(groups.keys())
        count = 0

     
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                a, b = letters[i], letters[j]
                setA, setB = groups[a], groups[b]

             
                common = len(setA & setB)

                
                count += 2 * (len(setA) - common) * (len(setB) - common)

        return count

ideas = ["coffee", "donuts", "time", "toffee"]
sol = Solution()
print("Number of distinct names:", sol.distinctNames(ideas))
