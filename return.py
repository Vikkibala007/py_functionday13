# return the values
def oddeven(i):
    '''this function return the value add or even'''
    if(i%2==0):
        return "it is even"
    else:
        return "it is add "
print(oddeven.__doc__)
j=int(input("enter your number"))
print(oddeven(j))
