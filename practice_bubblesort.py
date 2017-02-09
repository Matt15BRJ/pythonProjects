def bubbleSort(alist):
    for x in range(len(alist)-1,0,-1):
        for i in range(x):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(blist):
    for filler in range(len(blist)-1,0,-1):
        positionMax = 0
        for loc in range(1,filler+1):
            if blist[loc]>blist[positionMax]:
                positionMax=loc
        temp2 = blist[filler]
        blist[filler]=blist[positionMax]
        blist[positionMax]=temp2
              
alist = [67,45,2,13,1,998]
blist = [89,23,33,45,10,12,45,45,45]
bubbleSort(alist)
selectionSort(blist)
print(alist)
print(blist)              

