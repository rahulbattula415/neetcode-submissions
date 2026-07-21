class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if r >= len(board) or r < 0 or c >= len(board[0]) or c < 0:
                return False
            if (r, c) in visited:
                return False
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            visited.add((r, c))
            found = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            visited.remove((r, c))
            return found
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                visited = set()
                if dfs(r, c, 0):
                    return True
        return False
