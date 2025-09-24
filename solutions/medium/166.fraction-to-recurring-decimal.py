/**
 * Leetcode Solution for: 166. Fraction to Recurring Decimal
 * Difficulty: Medium
 * URL: https://leetcode.com/problems/fraction-to-recurring-decimal/submissions/1781322472/?envType=daily-question&envId=2025-09-24
 * Submitted: 2025-09-24T14:29:59.658Z
 */

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        negative = (numerator < 0) ^ (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)

        integer_part = numerator // denominator
        result = "-" if negative else ""
        result += str(integer_part) + "."

        remainder = numerator % denominator
        remainders = {}