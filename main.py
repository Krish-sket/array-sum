def sum(a):
    length=len(a)
    if length==1:
        return a[0]
    return a[0]+ sum(a[1:])
a=[1,5,3,77,5,8]
print('The sum of array a is:',sum(a))