from typing import List


class DiagonalTraverse:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        results = []
        row = len(mat)
        col = len(mat[0])

        cur_col = 0
        cur_row = 0
        going_up = True

        while len(results) != row * col:
            if going_up:
                while cur_row >= 0 and cur_col < col:
                    results.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1

                if cur_col == col:
                    cur_col -= 1
                    cur_row += 2
                else:
                    cur_row += 1
                going_up = False
            else:
                while cur_row < row and cur_col >= 0:
                    results.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1
                
                if cur_row == row:
                    cur_col += 2
                    cur_row -= 1
                else: 
                    cur_col += 1
                going_up = True
        
        return results