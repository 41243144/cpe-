class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        while True:
            number = int(input())
            counter = 0
            record = set()
            if number == 0:
                break

            while True:
                if number in record:
                    break
                counter += 1
                record.add(number)
                number = (number * number // 100) % 10000
            
            print(counter)
if __name__ == "__main__":
    Solution()