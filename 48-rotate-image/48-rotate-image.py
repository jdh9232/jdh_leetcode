"""
Solution Note

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

# Leet Code Solution
from copy import deepcopy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        sqr_len = len(matrix)
        sqr_end = sqr_len - 1
        div = sqr_len - 2
        is_odd = True
        if sqr_len % 2 == 0:
            is_odd = False

        n = 0
        m = 0

        # 0 1 = 1 0
        # 1 2 = 2 1

        # while n != div or m != div:
        while True:
            print(n, m)
            tmp = matrix[n][m]
            # 0 1
            # 0 0
            matrix[n][m] = matrix[sqr_end-m][n]
            # 0 1 = 1 0
            # 0 0 = 2 0
            matrix[sqr_end-m][n] = matrix[sqr_end-n][sqr_end-m]
            # 1 0 = 2 1
            # 2 0 = 2 2
            matrix[sqr_end-n][sqr_end-m] = matrix[m][sqr_end-n]
            # 2 1 = 1 2
            # 2 2 = 0 2
            matrix[m][sqr_end-n] = tmp
            # 1 2 = 0 1
            # 0 2 = 0 0

            if m >= div:
                if n >= div:
                    # 5,5 사각형인데 2,2 이면 끝
                    break
                n += 1
                m = n
                div -= 1
            else:
                m += 1