class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        roots = [i for i in range(n)]
        sizes = [1] * n
        def find(x):
            while roots[x] != x:
                roots[x] = roots[roots[x]]
                x = roots[x]
            return x

        components = n
        for src, dst in edges:
            rsrc, rdst = find(src), find(dst)
            if rsrc == rdst: continue
            # merge the shortest tree with the tallest
            if sizes[rsrc] < sizes[rdst]:
                rsrc, rdst = rdst, rsrc
            roots[rdst] = roots[rsrc]
            sizes[rsrc] += sizes[rdst]
            components -= 1

        return components

