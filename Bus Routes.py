class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        bus = defaultdict(list)
        queue = deque([source])
        totalBus = -1
        visited = set()

        for route in range(len(routes)):
            for i in range(len(routes[route])):
                bus[routes[route][i]].append(route)
        
        while queue:
            length = len(queue)
            totalBus += 1
            for i in range(length):
                node = queue.popleft()
                if node == target:
                    return totalBus
                
                for n in bus[node]:
                    if n not in visited:
                        visited.add(n)
                        queue.extend(routes[n])
        
        return -1
         
