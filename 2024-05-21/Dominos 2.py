class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        case_count = int(input())
        while case_count:
            n, link, push = map(int, input().split())
            domino = [False for _ in range(n + 1)]

            hash_map = dict()

            for _ in range(link):
                a, b = map(int, input().split())
                if a in hash_map:
                    hash_map[a].append(b)
                else:
                    hash_map[a] = [b]
            
            for _ in range(push):
                p = int(input())
                domino[p] = True
                self.dfs(hash_map, domino, p)
            print(domino.count(True))
            case_count -= 1

    def dfs(self, hash_map, domino, number):
        if number in hash_map:
            while hash_map[number]:
                num = hash_map[number].pop(0)
                domino[num] = True
                self.dfs(hash_map, domino, num)

if __name__ == "__main__":
    Solution()