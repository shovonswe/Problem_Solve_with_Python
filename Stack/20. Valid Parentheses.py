#optimal(stack)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for ch in s:
            if ch in mapping:  
                if stack:
                     top = stack.pop()
                else:
                    return False

                if mapping[ch] != top:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0
solution = Solution ()
s = "([])"
print(solution.isValid(s))  

#burte_force
class Solution:
    def isValid(self, s: str) -> bool:
        while  "()" in s or  "{}" in s or "[]" in s:
            s = s.replace("()","")
            s = s.replace("{}","")
            s = s.replace("[]","")
        return s ==""     
solution = Solution ()
s = "([])"
print(solution.isValid(s))    