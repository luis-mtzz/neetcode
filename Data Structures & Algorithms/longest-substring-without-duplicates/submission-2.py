class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, b = 0, 0, 0
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
                b = max(b, r - l)
            else:
                l += 1
                r = l + 1
        return b
        