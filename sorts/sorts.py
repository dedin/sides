# BUBBLE SORT
# Go through the list over and over again, swapping as you go(if necessary)
# until you go through the list w/out swapping. Can reduce number of iterations
# cos on every walk of the list, the largest ends up bn at its right position
# Simple, efficient on small data, but bad on large data
# Not good for a reversed ordered list or list with smallest element at the rear
# good for sorted or almost sorted list
# Has the advantage of detecting when the input is already sorted (insertion sort does
# better with this though)
# elements move toward the end faster than toward the front
# best case - (n), average and worst case - (n^2)
def bubbleSort(arr):
    n = len(arr)
    swapped = True
    while swapped:          #repeat as long as there was a swap in previous iteration
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swapped = True
        # Optimize : reduce the num of iterations for the for loop be4 the next walkthrough of the list
        n = n - 1
    return arr


#INSERTION SORT
# Has 2 sections - sorted and unsorted and it inserts one element at a time.
# Great for small n and inplace sortin, and for final finishing off for nlgn algorithms(e.g quick sort)
# The first element is sorted(trivially) and you keep
# moving to the front (if necessary) till you find the right spot for
# a value.
# This method just rewrites a num when it does not have to be moved
# and it ceates space then write, when it has to be moved
# Best case(sorted list) is - (n) and avg and worst case is - (n^2) worst case is a reversed sorted list
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n-1):
        val = arr[i]
        j = i - 1
        # start by overwriting the spot where arr[i] is and make
        # keep pushing nums over as you go
        while j >= 0 and arr[j] > val : # while num you are looking at is greater than val
            arr[j + 1] = arr[j]         # move current j one step to the right
            j = j - 1
        arr[j + 1] = val                # cos j ends up bn behind by 1 add 1 to get the spot for val
    return arr



# SELECTION SORT
# Great for small sized list, useful for when swapping and writing is expensive.
# does no more than n swaps and writes.
# Looks for 1st smallest in list and moves it to pos 1, and does the same for 2nd, 3rd ...
# starts at a point and looks at elemnts from point+1 to the end for smaller value
# It is (n^2)
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        indexOfMin = i      #make it initial minimum
        j = i + 1
        for j in range(j,n):  #search for another minimum if it exists
            if arr[j] < arr[indexOfMin]:
                indexOfMin = j

        if indexOfMin != i:  #if new minimum is not the previous minimum
            arr[i], arr[indexOfMin] = arr[indexOfMin], arr[i]
    return arr


# MERGE SORT
# breaks input down until it gets to one element and then
# merges them together
# Good for large list but could incur overhead in small list and is stable
# Best case - (n) when input is sorted, average and worst is(n^2)
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr)//2
    left = arr[0:middle]
    right = arr[middle:len(arr)]

    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left,right)

def merge(left, right):
    newarr = []
    i, j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            newarr.append(left[i])
            i = i + 1
        else:
            newarr.append(right[j])
            j = j + 1

    if j <= len(right)-1:
        newarr = newarr + right[j:]
    elif i <= len(left)-1:
        newarr = newarr + left[i:]
    return newarr


# QUICK SORT
# Divide and Conquer approach. Choose a pivot - best choice is median
# and divides the list by less than and greater than the pivot.
# It is in-place and has low overhead.It is unstable but fast. It uses lgn space
# Worst case - (n^2) when data is sorted and first or last element was chosen as pivot
# Best and average case - (nlgn) when a median or good pivot is chosen
# mostly used by languages and it uses insertion sort at the low level


# HEAP SORT
# Runs in (nlgn) time for all cases

if __name__ == "__main__" :
    arr = [5, 1, 4, 2, 8, 9]
    newarr = mergeSort(arr)
    print(newarr)
    newarr = bubbleSort(arr)
    insertionSortarr = insertionSort(arr)
    selectionSortarr = selectionSort(arr)
    print ("bubble sort is - ", newarr)
    print ("insertion sort is - ", insertionSortarr)
    print("selection sort is - ", selectionSortarr)

