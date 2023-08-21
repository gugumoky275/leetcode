class Solution:
    """
    Faster than 93.12%, O(log(N)) since digit iteration
    """
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):  # Quick exit condition on negatives, and nums that end in 0 (since no int can start with 0)
            return False

        n = 0
        x_copy = x
        while x_copy:  # Build the reverse num and check with its copy
            n = n * 10 + x_copy % 10
            x_copy //= 10
        
        return x == n
