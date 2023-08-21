class Solution:
    """
    Beats 90.94%
    """
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        return str(x)[::-1] == str(x)
    