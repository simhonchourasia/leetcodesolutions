# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        M = len(A)
        N = len(B)
        a = 0
        b = 0
        ret = []
        while a < M and b < N:
            if A[a][1] == B[b][0]:
                ret.append([A[a][1], B[b][0]])
                a += 1
            elif A[a][0] == B[b][1]:
                ret.append([A[a][0], B[b][1]])
                b += 1
            elif A[a][1] <= B[b][0]:
                a += 1
            elif A[a][0] >= B[b][1]:
                b += 1
            elif A[a][1] >= B[b][1]:
                ret.append([max(A[a][0], B[b][0]), B[b][1]])
                b += 1
            else:
                ret.append([max(A[a][0], B[b][0]), A[a][1]])
                a += 1
        return ret
