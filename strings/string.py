# REVERSE A STRING
def reversee(str):
    begin = 0
    end = len(str) - 1
    strlist = [i for i in str]
    while(begin < end):
        temp = strlist[end]
        strlist[end] = strlist[begin]
        strlist[begin] = temp
        begin += 1
        end -= 1
    return ''.join(strlist)


# REVERSE A NUMBER
def numReverse(number):
    new_num = 0
    while number != 0:
        dig = number % 10
        new_num = new_num * 10 + dig
        number = number //10
    return new_num


def main():
    str = "hello"
    newstr = reversee(str)
    print(newstr)
    number = 200
    newNumber = numReverse(number)
    print(newNumber)


main()