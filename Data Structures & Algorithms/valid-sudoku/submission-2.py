class Solution:

    '''
    board=
    [[".",".","4",".",".",".","6","3","."]
    ,[".",".",".",".",".",".",".",".","."]
    ,["5",".",".",".",".",".",".","9","."]
    ,[".",".",".","5","6",".",".",".","."]
    ,["4",".","3",".",".",".",".",".","1"]
    ,[".",".",".","7",".",".",".",".","."]
    ,[".",".",".","5",".",".",".",".","."]
    ,[".",".",".",".",".",".",".",".","."]
    ,[".",".",".",".",".",".",".",".","."]]
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R, C = 9, 9
        # R_sub, C_sub = 3, 3
        # def board_duplicates_exist(rc: List[str]):
        #     count_set = set()
        #     count = 0
        #     for n in rc:
        #         if n == ".":
        #             continue
        #         count += 1
        #         count_set.add(n)
        #     if count == len(count_set):
        #         return False
        #     return True
        
        # def sub_duplicates_exist(r_sub, c_sub):
        #     rc = []
        #     for r in range(r_sub, r_sub + R_sub):
        #         for c in range(c_sub, c_sub + C_sub):
        #             rc.append(board[r][c])
        #     return board_duplicates_exist(rc)
        
        # for r in range(R):
        #     if board_duplicates_exist(board[r]):
        #         return False
        
        # for c in range(C):
        #     tmp_col = []
        #     for r in range(R):
        #         tmp_col.append(board[r][c]) 

        #     if board_duplicates_exist(tmp_col):
        #         return False
        # for r_sub in range(0, R, R_sub):
        #     for c_sub in range(0, C, C_sub):
        #         if sub_duplicates_exist(r_sub, c_sub):
        #             return False
        # return True

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(R):
            for c in range(C):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True


        
      

        