# Problem ID: 166
# Title: Fraction to Recurring Decimal
# Runtime: 0 ms

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        negative = (numerator < 0) ^ (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)

        integer_part = numerator // denominator
        result = "-" if negative else ""
        result += str(integer_part) + "."

        remainder = numerator % denominator
        remainders = {}
        decimal = []

        while remainder != 0:
            if remainder in remainders:
                repeatIdx = remainders[remainder]
                decimal.insert(repeatIdx,"(")
                decimal.append(")")
                break
            remainders[remainder] = len(decimal)
            remainder *= 10
            digit = remainder // denominator
            decimal.append(str(digit))
            remainder %= denominator
        return result + "".join(decimal)