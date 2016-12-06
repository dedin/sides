"""
 Program prints numbers i from 1 to n inclusive. If i is
 divisible by p or or q it prints OUT, if i contains
 either p or q in its decimal it prints THINK, if both conditions are true, it prints
 OUTTHINK. else it prints the number

 Input : N p q E.g 10 3 5
 Output : A comma separated string.
 Soln : For each number in the range, check which condition
        it satisfies, build a list of all the strings from the
        condition check, then join the list with a comma.
"""


def out_think():
    line = input()
    N = int(line[0] + line[1])
    p = int(line[3])
    q = int(line[5])
    print(N, p, q)
    outputStr = []
    for i in range(1, N + 1):
        stri = checker(i, p, q)
        outputStr.append(str(stri))
    ",".join(outputStr)
    print(outputStr)


def divisible_by(i, p, q):
    if i % p == 0 or i % q == 0:
        return True
    else:
        return False


def contains_digit(i, p, q):
    numStr = str(i)
    if str(p) in numStr or str(q) in numStr:
        return True
    else:
        return False


def checker(i, p, q):
    if divisible_by(i, p, q) and contains_digit(i, p, q):
        return "OUTTHINK"
    elif divisible_by(i, p, q):
        return "OUT"
    elif contains_digit(i, p, q):
        return "THINK"
    else:
        return i


"""
 Find a closest common manager to quickly resolve conflict between 2 employees
 Program finds the closest manager by hierarchy

 Input : A comma separated list(string) of "manager->person" relationships, followed by 2 employees that
         have conflict.

 Output: The name of the manager that can resolve the conflict

 Example:
         Jane->Alex,Dan->Jane,Dan->Ellen,Alex,Ellen  should output Dan

 Notes : There is at least on relationship, No one person has 2 managers, maximum of 100
         levels of manager relationships, maximum of 15 people to a manager.

 Soln :  remove -> from the list of strings, form each name from the characters and
         put all names in a list. identify last 2 names keep and delete them from major list
         make a hashmap of manager to employee. get each person's manager, compare managers
         or look into the hashmap value of one manager for the other to find higher level manager
         if necessary.

"""


def closest_common_mngr():
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
    person2 = nameList[-1 - 1]
    del (nameList[-1])
    del (nameList[-1])
    mang = relations(nameList, person1, person2)
    print(mang)


def relations(nameList, person1, person2):
    relationshipDict = {}
    # make a hashmap of manager to employees
    for i in range(0, len(nameList), 2):
        key = nameList[i]
        if key in relationshipDict:
            relationshipDict[key].append(nameList[i + 1])
        else:
            relationshipDict[key] = [nameList[i + 1]]

    # look for the key that has person1 in his dictionary
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
    # manager1 is under manager2?
    elif mang1 in relationshipDict[mang2]:
        return mang2
    # manager2 is under manager1?
    elif mang2 in relationshipDict[mang1]:
        return mang1
    # none of the above
    else:
        print("NO CLOSEST MANAGER")
        return None


def main():
    out_think()
    closest_common_mngr()


if __name__ == "__main__":
    main()
