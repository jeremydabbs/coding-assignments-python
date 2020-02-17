# Countdown
def countdown(num):
    x=num
    newlist = []
    for x in range(num,-1,-1):
        newlist.append(x)
    return newlist
print(countdown(5))

# Print and Return
def print_and_return(a,b):
    print(a)
    return(b)
print_and_return(1,2)

# First Plus Length
def first_plus_length(thislist):
    return (thislist[0] + len(thislist))

first_plus_length([1,2,3,4,5])

# Values Greater than Second
def values_greater_than_second(thislist):
    newlist = []
    count = 0
    if len(thislist) < 2:
        return False
    else:
        for x in range(0,len(thislist),1):
            if thislist[x] > thislist[1]:
                newlist.append(thislist[x])
                count = count + 1
            else:
                continue
        print(count)
        return newlist
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# This Length, That Value
def length_and_value(size, value):
    newlist = []
    for x in range(0,size,1):
        newlist.append(value)
    return newlist
print(length_and_value(4,7))
print(length_and_value(6,2))