def search_(x, lst1):
    low= 0
    high= len(lst1)-1
    while low <= high:
        mid = (low + high)//2
        item= lst1[mid]
        if x == item:
            return mid
        elif x < item:
             high = mid -1
             return low
        else:
            low = mid + 1
            return high
    return -1
list=[5,2,7,8,9,1,4,6,3]
x=6
print(search_(x, list))
