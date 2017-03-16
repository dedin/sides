# Given a number, e.g 623315, what is the largest number that can be gotten when
# you take average of any 2 adjacent numbers?
# [:i] means give me every letter before i
# [i:] means give me every letter from i to the end
from __future__ import division
import math
def solution(number):
    number = str(number)
    maxSoFar = 0
    for i in range(0,len(number)-1):
        newDigit = int(math.ceil((int(number[i]) + int(number[i+1]))/2))
        newNumber = int(number[:i] + str(newDigit) + number[i+2:])
        if maxSoFar < newNumber:
            maxSoFar = newNumber
    return maxSoFar



# Given some directory structure information, find the longest path to a
# an image file.

# def solution(S):
#     str = "/"
#     dirnum = 0
#     subdirnum = 0
#     filenum = 0
#     level = 0
#     maxSoFar = 0
#     for char in S:
#         if char != "/n":
#             dirnum += 1
#         else:



def main():
    maxNum = solution(623315)
    print("maximum number from average is", maxNum)
    path_str = "dir1 dir11 dir12
  picture.jpeg
  dir121
  file1.txt
dir2
 file2.gif"
    longest_path = path_solution(path_str)

# str = "dir1\n" \
#       " dir11\n" \
#       " dir12\n" \
#       "     pic.jpeg\n" \
#       "     dir121\n" \
#       "dir2\n" \
#       " file2"
main()

# find the path to the picture file and print it out. shortest or longest
#
dir1
 dir11
 dir12
  picture.jpeg
  dir121
  file1.txt
dir2
 file2.gif