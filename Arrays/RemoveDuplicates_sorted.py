# Without In-Place

li = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4,4]
n = len(li)
x = []

for i in range(n - 1):  # Loop until n - 1
    if li[i] != li[i + 1]:
        x.append(li[i])

# Add the last element separately since the loop doesn't cover it
x.append(li[n - 1])

print(x)


### LeetCode (In-Place => No Extra Space, Make changes only in given array)

class Solution:
    def removeDuplicates(self, nums):
        l = 1

        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1

        return l


