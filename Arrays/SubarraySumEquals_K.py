class Solution:
    def subarraySum(self, nums, k):
        # Initializing result as 0
        result = 0
        current_sum = 0
        # Initializing an empty prefix with sum 0 (base case)
        prefix_sum = {0:1}

        for i in nums:
            current_sum += i
            diff = current_sum - k

            # Checking if prefix_sum = diff (i.e Subarray sum is met)
            result += prefix_sum.get(diff,0)

            # Updating prefix_sum dictionary by increasing current_sum count
            prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum,0)

        return result
             