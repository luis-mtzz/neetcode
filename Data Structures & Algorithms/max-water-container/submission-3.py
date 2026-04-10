class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_agua = 0
        left, right = 0, len(heights) - 1
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            max_agua = max(max_agua, area)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_agua

        