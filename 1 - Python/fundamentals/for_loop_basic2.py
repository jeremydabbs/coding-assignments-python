#Biggie Size
def biggie_size(thislist):
    for x in range(0,len(thislist),1):
        if thislist[x] > 0:
            thislist[x] = str("big")
    return thislist

print(biggie_size([-1, 3, 5, -5]))

#Count Positives
def count_positives(thislist):
    count = 0
    for x in range(len(thislist)):
        if thislist[x] > 0:
            count = count + 1
    thislist[len(thislist)-1] = count
    return thislist
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

#Sum Total
def sum_total(thislist):
    total = 0
    for x in range(len(thislist)):
        total = total + thislist[x]
    return total
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

#Average
def average(thislist):
    total = 0
    for x in range(len(thislist)):
        total = total + thislist[x]
    avg = total/len(thislist)
    return avg

print(average([1,2,3,4]))

#Length
def length(thislist):
    count = 0
    for x in range(len(thislist)):
        count = count + 1
    return count

print(length([37,2,1,-9]))
print(length([]))

#Minimum
def minimum(thislist):
    if len(thislist) == 0:
        return False
    else:
        min = thislist[0]
        for x in range(len(thislist)):
            if min > thislist[x]:
                min = thislist[x]
    return min

print(minimum([37,2,1,-9]))
print(minimum([]))

#Maximum
def maximum(thislist):
    if len(thislist) == 0:
        return False
    else:
        max = thislist[0]
        for x in range(len(thislist)):
            if max < thislist[x]:
                max = thislist[x]
    return max

print(maximum([37,2,1,-9]))
print(maximum([]))

#Ultimate Analysis
def ultimate_analysis(thislist):
    minimum = thislist[0]
    maximum = thislist[0]
    sumTotal = thislist[0]
    length = len(thislist)
    for x in range(1,len(thislist),1):
        if minimum > thislist[x]:
            minimum = thislist[x]
        if maximum < thislist[x]:
            maximum = thislist[x]
        sumTotal = sumTotal + thislist[x]
    average = (sumTotal/len(thislist))    
    new_dict = {'sumTotal': sumTotal, 'average' : average, 'minimum' : minimum, 'maximum' : maximum, 'length' : length}
    return new_dict

print(ultimate_analysis([37,2,1,-9]))

#Reverse List
def reverse_list(thislist):
    for x in range(0,int(len(thislist)/2),1):
        temp = thislist[x]
        thislist[x] = thislist[len(thislist)-x-1]
        thislist[len(thislist)-x-1] = temp
    return thislist

print(reverse_list([37,2,1,-9]))