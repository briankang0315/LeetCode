class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = 0

        while n < len(s):
            if n + 1 < len(s) and value[s[n]] < value[s[n + 1]]:
                total += value[s[n + 1]] - value[s[n]]
                n += 2
            else:
                total += value[s[n]]
                n += 1

        return total
