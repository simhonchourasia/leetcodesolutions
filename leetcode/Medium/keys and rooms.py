# https://leetcode.com/problems/keys-and-rooms/

class Solution(object):

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        N = len(rooms)
        # Keep track of rooms which have been visited
        visited = [0 for i in range(N)]
        visited[0] = 1
        s = [0]
        
        while len(s)>0:
            node = s.pop(len(s)-1)
            # Check the keys for each room
            for key in rooms[node]:
                if not visited[key]:
                    visited[key] = 1
                    s.append(key)
        return (sum(visited)==N)
