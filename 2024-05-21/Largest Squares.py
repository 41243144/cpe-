class Solution():
    def __init__(self):
        self.main()

    def main(self):
        n = int(input())
        while n:
            h, w, data_case = map(int, input().split())
            if h == 0 or w == 0:
                n -= 1
                continue

            matrix = []
            for _ in range(h):
                matrix.append(input())

            print(f"{h} {w} {data_case}")
            
            while data_case:
                data_case -= 1
                height, width = map(int, input().split())
                if height < 0 or height >= h or width < 0 or width >= w:
                    continue
                print(self.largest_square(matrix, height, width))

            n -= 1
        
    def largest_square(self, matrix: list, height: int, width: int) -> int:
        ch = matrix[height][width]
        count = 1
        h_len = len(matrix)
        w_len = len(matrix[0])

        while True:
            if height - count < 0 or height + count >= h_len or width - count < 0 or width + count >= w_len:
                return 1 + ((count - 1) * 2)
            for i in range(height - count, height + count + 1):
                for j in range(width - count, width + count + 1):
                    if matrix[i][j] != ch:
                        return 1 + ((count - 1) * 2)
            count += 1
        

if __name__ == "__main__":
    Solution()
