def buy_and_sell(arr):
  #Fill this in.
    lowestPrice = min(arr)
    offset = arr.index(lowestPrice)
    priceSlice = arr[offset:]
    highestPrice = max(priceSlice)

    return highestPrice - lowestPrice

  
print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5