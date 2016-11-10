# program that finds largest and smallest
# number in a list given in 2 sections -
# one ascending, one descending0-
def main():
    arr = [1,2,3,4,5,6,7]
    min = findMin(arr)
    print(max(arr))
    print(min, max)

def findMin(arr):
    if len(arr) == 1 or arr[0] < arr[1]:
        return arr[0]
    else:
        return arr[len(arr) - 1]

def findMax(arr):
    if len(arr) == 1 or arr[0] > arr[1] :
        return arr[0]
    start = 0
    end = len(arr) - 1
    mid = start + end // 2
    while arr[mid] < arr[mid-1] and arr[mid] > arr[mid + 1]:
        if arr[mid+1] > arr[mid]:
            mid = (mid + end)//2
        else:
            mid = (start + mid) //2
    return arr[mid]

if __name__ == "__main__":
    main()




# Program that reads a file of
# grades and courses and writes
# the number of IDs with total score
# of 100 or more, into a file.
inputFile = open("input.txt", "r")
data = [line.strip("\n").replace(" ", "").split(",") for line in inputFile.readlines()]
print (data)
dict = {}
count = 0
cut = 100
for i in range(len(data)):
    key = data[i][0]
    if key in dict:
        dict[key] += int(data[i][2])
        if dict[key] >= cut:
            count += 1
    else:
        dict[key] = int(data[i][2])
        if dict[key] >= cut:
            count += 1
print(dict)
outputFile = open("output.txt", "w")
outputFile.write(str(count))


