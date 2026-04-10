class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l, r = 0, 0
        for ch in range(len(s)):
            if s[ch] in mp:
                l = max(mp[s[ch]] + 1, l)
            mp[s[ch]] = ch
            r = max(r, ch - l + 1)
        return r