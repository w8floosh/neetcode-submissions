class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions = []
        def dfs(curr, op, cp):
            if op == cp == n: 
                solutions.append(curr)
                return
            
            if op <= n: 
                dfs(curr + '(', op+1, cp)
            if op > cp and cp <= n:
                dfs(curr + ')', op, cp+1)
        
        dfs("", 0, 0)
        return solutions
        
