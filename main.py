def sum(a):
    length=len(a)
    if length==1:
        return a[0]
    return a[0]+ sum(a[1:])
user_input = input("Enter numbers separated by space: ")
a = list(map(int, user_input.split()))
print('The sum of array a is:',sum(a))