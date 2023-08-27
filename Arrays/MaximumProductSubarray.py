# Neetcode Approach

def maxProduct(nums):
    res = max(nums)
    curMax, curMin = 1,1

    for i in nums:
        temp = i*curMax
        curMax = max(i*curMax,i*curMin,i)
        curMin = min(temp,i*curMin,i)

        res = max(res,curMax)
    
    return res

# Striver's Approach (Easier)

def maxProduct(nums):
  
    # result = -Infinity
    res = float('-inf')
  
    pref, suff = 1,1
    n = len(nums)

    for i in range(n):
        if pref == 0:
            # Simply starting again with value = 1
            pref = 1
        if suff == 0:
            suff = 1

        pref = pref * nums[i]
        
        # Multiplying from the end of array
        suff = suff * nums[n-i-1]

        res = max(res,max(pref,suff))
    
    return res

maxProduct([2,3,-2,4,-1,5])
