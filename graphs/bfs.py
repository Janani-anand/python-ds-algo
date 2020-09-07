from collections import defaultdict
from collections import deque

class graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,v):
        visited=[False]*(len(self.graph))
        s=deque()
        s.append(v)
        visited[v]=True
        while s:
            n=s.popleft()
            print(n,end=' ')

            for i in self.graph[n]:
                if(visited[i]==False):
                    s.append(i)
                    visited[i]=True
g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.bfs(2)
