# OUTTHINK PROGRAM : prints numbers from 1 to n inclusive
# if i is divisible by p or q it prints OUT, if i contains
# either p or q in its decimal it prints THINK, if both conditions are true, it prints
# OUTTHINK. else it prints the number
def main1():
    line = input()
    N = int(line[0] + line[1])
    p = int(line[3])
    q = int(line[5])
    print(N, p, q)
    outputStr = ""
    for i in range(1, N+1):
        stri = checker(i, p, q)
        outputStr = outputStr + str(stri) + ","
    print(outputStr)

def divisibleBy(i, p, q):
    if i % p == 0 or i % q == 0:
        return True
    else:
        return False

def containsDigit(i, p, q):
    numStr = str(i)
    if str(p) in numStr or str(q) in numStr:
        return True
    else:
        return False

def checker(i, p, q):
    if divisibleBy(i, p, q) and containsDigit(i, p, q):
        return "OUTTHINK"
    elif divisibleBy(i,p,q):
        return "OUT"
    elif containsDigit(i,p,q):
        return "THINK"
    else:
        return i




# #IBM desires to develop a service to help a client quickly find a manager who can resolve the conflict between two
# employees. When there is a conflict between two employees, the closest common manager should help resolve the conflict.
# The developers plan to test the service by providing an example reporting hierarchy to enable the identification of
# the closest common manager for two employees. Your goal is to develop an algorithm for IBM to efficiently perform this
# task. To keep things simple, they just use a single relationship "isManagerOf" between any two employees.
# For example, consider a reporting structure represented as a set of triples:
#     Tom isManagerOf Mary
#     Mary isManagerOf Bob
#     Mary isManagerOf Sam
#     Bob isManagerOf John
#     Sam isManagerOf Pete
#     Sam isManagerOf Katie
# The manager who should resolve the conflict between Bob and Mary is Tom(Mary's manager). The manager who should
# resolve the conflict between Pete and Katie is Sam(both employees' manager). The manager who should resolve the
# conflict between Bob and Pete is Mary(Bob's manager and Pete's manager's manager).
# Assumptions:
#     There will be at least one isManagerOf relationship.
#     There can be a maximum of 15 team member to a single manager
#     No cross management would exist i.e., a person can have only one manager
#     There can be a maximum of 100 levels of manager relationships in the corporation
# Input:
#     R1,R2,R3,R4...Rn,Person1,Person2 R1...Rn - A comma separated list of "isManagerOf" relationships.
#     Each relationship being represented by an arrow "Manager->Person".
#     Person1,Person2 - The name of the two employee that have conflict
# Output:
#     The name of the manager who can resolve the conflict
# E.g
# Sam->Pete,Pete->Nancy,Sam->Katie,Mary->Bob,Frank->Mary,Mary->Sam,Bob->John,Sam,John

def main():
    newLine = ""
    line = input()
    for char in line:
        if char == "-":
            char = ","
        if char == ">":
            char = ""
        newLine = newLine + char
    word = ""
    nameList = []
    for char in newLine:
        if char != ",":
            word = word + char
        else:
            nameList.append(word)
            word = ""
    nameList.append(word)
    person1 = nameList[-1]
    person2 = nameList[-1-1]
    del(nameList[-1])
    del(nameList[-1])
    mang = relations(nameList, person1, person2)
    print(mang)


def relations(nameList, person1, person2):
    relationshipDict = {}
    # make a dictionary of manager to employees
    for i in range(0, len(nameList), 2):
        key = nameList[i]
        if key in relationshipDict:
            relationshipDict[key].append(nameList[i + 1])
        else:
            relationshipDict[key] = [nameList[i + 1]]

    #look for the key that has person1 in his dictionary
    # this works cos a person can only have one manager
    mang1 = ""
    mang2 = ""
    for key, value in relationshipDict.items():
        if person1 in value:
            mang1 = key
        if person2 in value:
            mang2 = key
    # same manager?
    if mang1 == mang2:
        print("SAME MANAGER")
        return mang1
    #manager1 is under manager2?
    elif mang1 in relationshipDict[mang2]:
        return mang2
    #manager2 is under manager1?
    elif mang2 in relationshipDict[mang1]:
        return mang1
    #none of the above
    else:
        print("NO CLOSEST MANAGER")
        return None






# Given sequence of passages, filter out one whose test is wholly contained as a
# subpassage of one or more of the other passages
# E.g
# "Computer Science Department"|Computer-Science-Department|the "computer science department"
# gives - Computer-Science-Department|the "computer science department"
# 
# IBM cognitive computing|IBM "cognitive" computing is a revolution| ibm cognitive  computing|'IBM Cognitive Computing' is a revolution?
# gives IBM "cognitive" computing is a revolution


# import sys
# def main():
#     line = input()
#     print(line)
#     count = 0
#     maxSoFar = 0
#     strSoFar = ""
#     str = ""
#
#     for char in line:
#         if char != "|":
#             count += 1
#             str = str + char
#         else:
#             if maxSoFar < count:
#                 maxSoFar = count
#                 count = 0
#                 strSoFar = str
#                 str = ""
#             else:
#                 count = 0
#                 str = ""
#     print (maxSoFar)
#     print(strSoFar)
#     return strSoFar
#
# if __name__ == "__main__":
#    str =  main()
#    print(str)
#




main()
