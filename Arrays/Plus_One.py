class Solution:
    def plusOne(self, digits):
        carry, i = 1,0

        # Reversing the array 
        digits = digits[::-1]

        while carry:
            if i < len(digits):
                # If given digit of array is 9
                if digits[i] == 9:
                    # Replace it with zero
                    digits[i] = 0
        
                else:
                    # If digit is b/w 0-8
                    digits[i] += 1
                    # Change carry to 0 to end while loop
                    carry = 0

            else:
                digits.append(1)
                carry = 0

            i += 1

        return digits[::-1]