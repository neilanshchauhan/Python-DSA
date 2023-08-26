nums = [0,1,2,2,3,0,4,2]
val = 2
x = 0
n = len(nums)

for i in range(n):
    if nums[i] != val:
        # Swapping
        nums[x] = nums[i]
        x += 1

# Printing number of elements after removing/excluding "val"
print(x)