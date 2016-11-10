# LINEAR SEARCH
# Used to search in a list. list
# does not have to be sorted.

def linearSearch(arr, num):
    i = 0
    found = False
    while i < len(arr) and found == False:
        if arr[i] == num:
            found = True
        i = i + 1

    if found == False:
        arr.append(num)
    else:
        print("found it!")
    #   OR
    # found = False
    # for i in range(len(arr)):
    #     if arr[i] == num:
    #         found = True
    #         break
    # if found:
    #     print("found iit!")
    # else:
    #     arr.append(num)
    return arr, i

# BINARY SEARCH
# used on sorted list
def binarySearch(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) //2
        if arr[mid] == num:
            return True
        elif num < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

    # found = False
    # mid = len(arr)//2
    # if arr[mid] == num:
    #     print("found iit!")
    #     print(arr[mid])
    #     found = True
    #     return found
    # if num < arr[mid]:
    #     binarySearch(arr[:mid], num)
    # elif num > arr[mid]:
    #     binarySearch(arr[mid+1:], num)


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    found = binarySearch(arr, 4)
    # print("item was found in ", count, "searches")
    print(found)

