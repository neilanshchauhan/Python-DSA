def maxProfit(prices):

    # Two Pointers
    l,r = 0,1
    maxProfit = 0

    while r < len(prices):
        
        # eg: [1,7]
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            # if [7,1,5] shift left ptr to right (i.e to value 1)
            l = r
        r += 1

    return maxProfit

maxProfit([1,4,5,2,10,3])