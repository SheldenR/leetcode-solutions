class Solution:
    # Very interesting solution, not at all my first thught
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            return str1[0:math.gcd(len(str1), len(str2))]
        return ""
