class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == "-":
            y = list(x.split("-"))
            b = int(y[1][::-1])
        else:
            b = int(x[::-1])
        if (b > (-2**31) and b <= (2**31)):
            if x[0] == "-":
                return -int(b)
            return int(b)
        return 0
    