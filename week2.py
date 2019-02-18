def selection_sort(my_array):
    swap_sayisi=0
    for i in range(len(my_array)-1,0,-1):
        positionOfMax=0
        for location in range(1,i+1):
            print("location: ",location,"i: ",i,end="\n")
            if (my_array[location] > my_array[positionOfMax]):
                positionOfMax = location
        temp = my_array[location]
        my_array[location] = my_array[positionOfMax]
        my_array[positionOfMax] = temp
        swap_sayisi +=1
    return my_array,swap_sayisi




def binary_search(my_array,item):
    counter=0
    first=0
    last=len(my_array)-1
    found=False
    while(first <= last and not found):
        midpoint=(first+last)//2
        if (my_array[midpoint]==item):
            found=True
        else:
            if (item < my_array[midpoint]):
                last=midpoint-1
            else:
                first=midpoint+1
        counter +=1
    return midpoint,found,counter




my_array=[21,23,13,44,25,2,7,16,14,12,11]
print(selection_sort(my_array))
print(binary_search(my_array,14))


