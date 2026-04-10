class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = self.extract_digs(slow)
            fast = self.extract_digs(self.extract_digs(fast))
            if fast == 1:
                return True
            elif slow == fast:
                return False

    def extract_digs(self, n):
        next_number = 0
        while n > 0:
            digit = n % 10
            n //= 10
            next_number += digit ** 2
        return next_number