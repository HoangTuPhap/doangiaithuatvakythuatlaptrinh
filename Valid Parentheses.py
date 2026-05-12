class Solution:
    def isValid(self, s):
        stack = []
        mp = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in mp:
                if not stack or stack[-1] != mp[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack
