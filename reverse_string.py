class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = (len(s) - 1)
        mid = len(s) // 2
        for char in range(mid):
            front = s[i]
            s[i] = s[j]
            s[j] = front
            i += 1
            j -= 1
        return s


s = ["h","e","l","x","o", "s"]
S = Solution()
print(S.reverseString(s))