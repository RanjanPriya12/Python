def findFactorial(num):
    if num<=1:
        return 1;
    return num*findFactorial(num-1)

#print(findFactorial(5))

def secondLargestNumber(arr):
    max1 = max2 = float('-inf')
    for x in arr:
        if x>max1:
            max2=max1;
            max1=x;
        elif x>max2:
            max2=x;
    return max2;

print(secondLargestNumber([4,1,2,6,5,9,7,10]))