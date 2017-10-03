def adjacentElementsProduct(inputArray):
   result = []
   for i in range(1,len(inputArray)):
      product = inputArray[i] * inputArray[i-1]
      result.append(product)
   return max(result)
