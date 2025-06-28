class Solution:
    def romanToInt(self, s: str) -> int:
        roman = list(s)

        number = list(map(lambda x: 1 if x == "I" else x, roman))
        number = list(map(lambda x: 5 if x == "V" else x, number))
        number = list(map(lambda x: 10 if x == "X" else x, number))
        number = list(map(lambda x: 50 if x == "L" else x, number))
        number = list(map(lambda x: 100 if x == "C" else x, number))
        number = list(map(lambda x: 500 if x == "D" else x, number))
        number = list(map(lambda x: 1000 if x == "M" else x, number))

        actual = []
        n = 0
       
        while n < len(number):
            if n+1 < len(number):
                if (number[n] < number[n+1]):
                    m = number[n+1] - number[n]
                    n += 2
                    actual.append(m)
                else:
                    actual.append(number[n])
                    n+=1
            else:
                actual.append(number[n])
                n+=1
        total = sum(actual)
        return total
