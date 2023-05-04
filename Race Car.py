class Solution:
    def racecar(self, target: int) -> int:
        distance = 0
        queue = deque([(0, 1)])
        visited = set([(0, 1)])

        while queue:
            length = len(queue)
            for i in range(length):
                pos, speed = queue.popleft()
                if pos == target:
                    return distance
                if (pos + speed , speed * 2) not in visited:
                    visited.add((pos + speed , speed * 2))
                    queue.append((pos + speed , speed * 2))
                if speed > 0:
                    new_speed = -1
                else:
                    new_speed = 1
                if (pos, new_speed) not in visited:
                    visited.add((pos, new_speed))
                    queue.append((pos, new_speed))
            distance += 1
        return -1
