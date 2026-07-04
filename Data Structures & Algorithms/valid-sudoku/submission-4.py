from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(int)
        rows = defaultdict(int)
        boxes = defaultdict(int)

        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                box = (row//3 * 3) + col//3


                if value == ".": continue

                d = int(value)
                bit = 1 << (d - 1)

                if rows[row] & bit:
                    return False
                rows[row] |= bit


                if cols[col] & bit:
                    return False
                cols[col] |= bit

                if boxes[box] & bit:
                    return False
                boxes[box] |= bit
        return True
            

                    