class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = int(a,2) + int(b,2)
        return "{:b}".format(ans)
