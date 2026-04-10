class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            pairs = self.two_sum(nums, i + 1, -nums[i])
            for pair in pairs:
                trips.append([nums[i]] + pair)
        return trips

            
    
    def two_sum(self, nums, start, target):
        pairs = []
        left, right = start, len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                pairs.append([nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif sum < target:
                left += 1
            else:
                right -= 1
        return pairs