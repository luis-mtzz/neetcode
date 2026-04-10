class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            cnt = [0] * 26
            for ch in word:
                cnt[ord(ch) - ord('a')] += 1
            res[tuple(cnt)].append(word)
        return list(res.values())