import math

class Solution:
    def __init__(self):
        self.main()

    def main(self):
        n = int(input())
        while n:
            n -= 1
            string = list(input())
            string = sorted(string)
            target = int(input())
            current = list()
            while target:
                length = len(string)
                avg = math.factorial(length) // length
                count = 0
                while target - avg >= 0:
                    target -= avg
                    count += 1
                
                ch = string.pop(count)
                current.append(ch)
            current.extend(string)
            print("".join(current))


if __name__ == "__main__":
    Solution()
