li = [2,1,3,4]
k = 5
n = len(li)
sum = 0

for i in range(0,n-1):

    for j in range(i+1,n):
        sum = 0
        sum += li[i] + li[j]

        if (sum == k):
            print("Two Sum indices are => ",i,j)

### Hashmap Approach (LeetCode)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        obj = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in obj:
                return [obj[diff], i]

            # Appending (value,index) in dictionary
            obj[n] = i