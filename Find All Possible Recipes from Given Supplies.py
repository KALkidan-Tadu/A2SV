class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        depend = defaultdict(list)
        queue = deque()
        order = []

        for i in range(len(recipes)):
            for r in ingredients[i]:
                depend[r].append(recipes[i])
                indegree[recipes[i]] += 1
        
        for supp in supplies:
            queue.append(supp)
        
        while queue:
            food = queue.popleft()
            for f in depend[food]:
                indegree[f] -= 1
                if indegree[f] == 0:
                    order.append(f)
                    queue.append(f)
        return order
