"""
 Given a number, what is the largest number that can be gotten when
 you take average of any 2 adjacent numbers?

 Input : number

 Output : largest number from taking average

 Soln : take each 2 adjacent numbers, find  the average, join
        it to the remaining "string" of numbers and compare
        with previous maximum
        [:i] means give me every letter before i
       [i:] means give me every letter from i to the end
"""

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


"""
  Given some directory structure information, find the longest path to a
  an image file

  Input : A string of directory structure

  Output: path to the image file and length of the path

  APPROACH: (Depth First Search)
     At whatever level you are, keep going back up until you find a dir
     that is 1 less than the current level you are on
     At every item, you are assuming it is the one you want until it fails the if statement test
"""


def path_solution(path_str):
    path_list = path_str.splitlines()
    print path_list
    last_level_seen = -1
    max_len = 0
    max_str = ""
    stack = [-1]
    str_stack = []
    #get each item in the list with the tabs included
    for item in path_list:
        bare_name = item.lstrip('\t')
        item_level = len(item) - len(bare_name)         # use number of tabs to get the level of each item
        # there are 2 options here:::
        #
        # (1) YOU ARE STILL SEARCHING, and current item is in the same level as
        #     previous item IE. the last item cannot be in the path you are trying to generate cos its on same level.
        #   - pop last item from the stack (and replace with current, eventually)
        #   - reduce last level to backtrack in the directory in case you need to pop more previous files or dirs
        #   - keep popping while you see files/dirs that cant be in your path (cos their level is either the same or gre
        #    ter(last level - 1) than current level
        # (2) YOU ARE STILL SEARCHING and current item is in a level that is less than last item, E.G dir2 to file1.txt
        #     then you dont need last item and you want to backtrack and keep popping until you get to a level that is
        #     1 less than your current level.
        while item_level <= last_level_seen:
            stack.pop()
            str_stack.pop()
            last_level_seen -= 1
        # When you are in the right spot in the stack put your length + path separator + previous last on the stack
        stack.append(len(bare_name) + stack[-1] + 1)
        str_stack.append(bare_name)
        last_level_seen = item_level                    # make last level seen to be current item's level
        if '.jpeg' in item:
            max_len = max(max_len, stack[-1])
            break
    max_str = "/".join(str_stack)
    return max_len, max_str






def main():
    maxNum = solution(623315)
    print("maximum number from average is", maxNum)
    path_str = "dir1\n\tdir11\n\tdir12\n\t\tpicture.jpeg\n\t\tdir121\n\t\tfile1.txt\ndir2\n\tfile2.gif"
    longest_path, longest_str = path_solution(path_str)
    print longest_path
    print longest_str


main()