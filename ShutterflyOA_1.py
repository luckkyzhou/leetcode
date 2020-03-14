class Solution:
    def countSubarrays(self, numbers, k):
        # Write your code here
        res = 0
        product = 1
        # Use two pointers to traverse the array.
        left = 0
        for right in range(len(numbers)):
            product *= numbers[right]
            # Move the left pointer while product > k.
            while product > k:
                product /= numbers[left]
                left += 1
            # There are (right - left + 1) number of subarrays between left and right.
            res += right - left + 1
        return res