class Solution():
    def __init__(self) -> None:
        self.main()
        self.count = 0
        self.result = list()
    def main(self):

        while True:
            number = int(input())
            if number == 0:
                break
            self.count = 0
            self.result = list()
            self.unique_factorization(2, number, [])
            print(self.count)
            if self.count != 0:
                print("\n".join(self.result))

    def unique_factorization(self, start, number, current):
        if number == 1 and len(current) > 1:
            self.result.append(" ".join(map(str, current)))
            self.count += 1

        for i in range(start, number + 1):
            if number % i == 0:
                current.append(i)
                self.unique_factorization(i, number // i, current)
                current.pop()

if __name__ == "__main__":
    Solution()