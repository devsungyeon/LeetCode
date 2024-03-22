class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        sym = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        mins = 0
        
        s = s[::-1]
        for i in s:
            if mins <= sym[i]:
                ans = ans + sym[i]
                mins = sym[i]
            else:
                ans = ans - sym[i]
        return ans