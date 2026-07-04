from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                value = board[row][col]
                box = (row//3 * 3) + col//3

                if value == ".": continue

                if value in rows[row]:
                    return False
                else:
                    rows[row].add(value)
                
                if value in cols[col]:
                    return False
                else:
                    cols[col].add(value)

                if value in boxes[box]:
                    return False
                else:
                    boxes[box].add(value)
        return True