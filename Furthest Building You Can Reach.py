class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        builds = []
        index = 0
        while index < len(heights)-1:
            if heights[index+1] > heights[index]:
                jump = heights[index+1] - heights[index]
                if bricks >= jump:
                    bricks -= jump
                    heappush(builds, -1*jump)
                elif ladders > 0:
                    if builds and -1 * builds[0] > jump:
                        bricks += (-1 * heappop(builds))
                        heappush(builds, -1 * jump)
                        bricks -= jump
                    ladders -= 1
                else:
                    break
            index += 1
        return index

        
