# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        S = sorted(points, key=lambda point: point[0]**2 + point[1]**2)
        return S[:K]
