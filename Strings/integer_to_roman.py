class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        current, result = num, []

        while current > 0:
            for roman, integer in mapping.items():
                quotient, remainder = divmod(current, integer)
                if quotient > 0:
                    result.append(roman * quotient)
                    current = remainder
        return "".join(result)
