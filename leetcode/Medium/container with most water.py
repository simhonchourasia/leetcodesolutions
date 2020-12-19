# leetcode.com/problems/container-with-most-water/

class Solution:
    # Brute force with time complexity O(n)
    # We do n passes for each value in height
    def bruteForce(self, height):
        mx = 0
        for j in range(1,len(height)):
            for i in range(j):
                water = min(height[i], height[j])*(j-i)
                mx = max(mx, water)
        return mx
    
    # Two pointer solution
    # O(n) space, as left can only increment up to n times, and right can only decrement up to n times
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        left = 0
        right = len(height)-1
        while left < right:
            water = min(height[left], height[right]) * (right-left)
            mx = max(mx, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return mx
