class Solution:
    def rob(self, nums: List[int]) -> int:
        rob0 = rob1 = 0
        for num in nums:
            temp = max(num + rob0, rob1)
            rob0 = rob1
            rob1 = temp
        return rob1