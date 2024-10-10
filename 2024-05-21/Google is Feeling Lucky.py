class Solution():
    def __init__(self) -> None:
        self.main()
    def main(self):
        case_number = int(input())
        count = 0
        while count < case_number:
            hash_map = dict(list())
            for _ in range(10):
                url, number = input().split()
                number = int(number)
                if number in hash_map:
                    hash_map[number].append(url)
                else:
                    hash_map[number] = [url]
            count += 1
            i = max(hash_map)
            print(f"Case #{count}:")
            for url in hash_map[i]:
                print(url)

if __name__ == "__main__":
    Solution()