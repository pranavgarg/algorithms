class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.outputs = []
        self.gen_permutations(range(n), 0)
        return self.outputs

    def gen_permutations(self, n, i):
        if i == len(n) - 1:
            if self.validate_permute(n):
                self.print_permute(n)
            return
        for j in range(i, len(n)):
            n[i], n[j] = n[j], n[i]
            self.gen_permutations(n, i+1)
            n[j], n[i] = n[i], n[j]

    def validate_permute(self, arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if abs(arr[i] - arr[j]) == abs(i - j):
                    return False
        return True

    def print_permute(self, arr):
        l = len(arr)
        temp = [[''] for _ in range(l)]
        for i in range(l):
            for j in range(l):
                if arr[i] == j:
                    temp[i].append("Q")
                else:
                    temp[i].append(".")
            temp[i] = ''.join(temp[i])

        self.outputs.append(temp)


s = Solution()
print s.solveNQueens(4)