class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we use a map for instant look up
        mp = {}
        l, r = 0, 0
        # iterate over the characters in the string
        for ch in range(len(s)):
            # if the character is already in my map
            if s[ch] in mp:
                # then set the left pointer equal the greater of
                # what index is in the map, or the current left
                l = max(mp[s[ch]] + 1, l)
            # insert or update the existing entry in the map for the character
            mp[s[ch]] = ch
            # calculate the new largest length and update our result
            r = max(r, len(s[l:ch]) + 1)
        # return the result once you've iterated through all the characters in the string
        return r