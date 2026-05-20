class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + 1 if i == len(digits) - 1 else digits[i] + carry
            digits[i] = s % 10
            carry = 1 if s == 10 else 0
        if carry == 1:
            digits.insert(0, carry)
        return digits
        