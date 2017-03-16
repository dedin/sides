"""
 Largest number with n digits. Number consists only of 3 and only 5,
 or both. When it is both, number of 5s is divisible by 3 and number of 3s is divisible by 5

 Input : an integer N

 Output : largest number with N digits

 Soln: Look at your priority (5s) and get as many of that as possible, by getting as many multiples of 3
       as you can get out of the number without not exhausting the number
       if number is not 3 or 5, keep subtracting 5 (for 3s) from number while number is
       not divisible by 3. otherwise, once number becomes divisible by 3, we have a multiple (set) of 3
       for 5s and we will have had at least one set of 5 for 3s.
       if number is originally divisible by 3, e.g 6,9 then you dont need any 3 and your whole
       string will be 5s which is the prioritized number.
"""

def largest_num(num):
    if num is 3:
        print "555"
    elif num is 5:
        print "33333"
    else:
        y = num
        while num%3 != 0:
            num = num - 5
        if num < 0:
            print -1
        else:
            print num * '5' + (y - num) * '3'


def main():
    n = int(input())
    largest_num(n)


if __name__ == '__main__':
    main()