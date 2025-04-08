def balancedString(s):
    n = len(s)
    target = n // 4

    
    count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
    for ch in s:
        count[ch] += 1

    
    if all(count[c] == target for c in "QWER"):
        return 0

    min_len = n
    left = 0

    for right in range(n):
        count[s[right]] -= 1

        
        while left < n and all(count[c] <= target for c in "QWER"):
            min_len = min(min_len, right - left + 1)
            count[s[left]] += 1
            left += 1

    return min_len
