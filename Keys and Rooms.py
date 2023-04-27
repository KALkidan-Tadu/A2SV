class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = defaultdict(list)
        length = len(rooms)
        visited = set([0])
        queue = deque([0])

        for i in range(length):
            for key in rooms[i]:
                keys[i].append(key)
        
        while queue:
            room = queue.popleft()
            for node in keys[room]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
        
        if len(visited) == length:
            return True
        return False
