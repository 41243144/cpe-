import sys
sys.setrecursionlimit(10**6)
class Soultion():
    def __init__(self) -> None:
        self.main()
    
    def main(self):
        try:
            while True:
                c = int(input())
                graph = [[] for _ in range(c)]
                dp = [[0] *2 for _ in range(c)]

                for i in range(c):
                    node, line = input().split(':')
                    node = int(node)
                    _, line = line.split(')')
                    
                    l = list(map(int, line.split()))
                    
                    for n in l:
                        graph[n].append(node)
                        graph[node].append(n)
                self.dfs(0, -1, graph, dp)
            
                print(min(dp[0][0], dp[0][1]))


        except EOFError:
            exit()

    def dfs(self, node, parent, graph, dp):
        dp[node][0] = 0
        dp[node][1] = 1

        for neighbor in graph[node]:
            if neighbor != parent:
                self.dfs(neighbor, node, graph, dp)
                dp[node][0] += dp[neighbor][1]
                dp[node][1] += min(dp[neighbor][0], dp[neighbor][1])

if __name__ == "__main__":
    Soultion()