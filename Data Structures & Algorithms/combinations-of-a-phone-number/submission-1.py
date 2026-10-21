
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0: return []
        letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        solutions = []
        def dfs(i, curr):
            if i >= n:
                solutions.append(curr)
                return

            for l in letters[int(digits[i])-2]:
                dfs(i+1, curr + l)
        
        dfs(0, "")
        return solutions


            
