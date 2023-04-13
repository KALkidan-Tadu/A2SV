class ThroneInheritance:
    inherit = defaultdict(list)
    dead = set()
    king = ""
    def __init__(self, kingName: str):
        self.inherit = defaultdict(list)
        self.inherit[kingName] = []
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.inherit[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        visited = set()
        order = []
        def dfs(person):
            if person in visited:
                return
            if person not in self.dead:
                order.append(person)
                visited.add(person)
            for child in self.inherit[person]:
                dfs(child)
        dfs(self.king)
        return order
        

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
