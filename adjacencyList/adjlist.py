# Program to make an adjaceny list of
# employess that are friends according to
# a given input csv file
import csv


def main():
    print("...Friendship Network Implementation...")
    employeelist = parse_input(filename="employees.csv")
    del employeelist[0]
    friendslist = parse_input(filename="friendships.csv")
    del friendslist[0]
    print(employeelist)
    print(friendslist)
    Matrix = compute_adjacency_list(employeelist,friendslist)
    for key, value in Matrix.items():
        if value == []:
            value = None
        print(key ,":" ,value)
    print(Matrix.get(2))
    dict= {}
    for emp in employeelist:
        dict[emp[1]] = [emp[0], emp[2]]
    print(dict)
    # dict.get("Richard")


def compute_adjacency_list(employees, friendslist1):
    matrix = {}
    for emp in employees:
        matrix[int(emp[0])] = []
    for num in friendslist1:
        matrix[int(num[0])].append(int(num[1]))
        matrix[int(num[1])].append(int(num[0]))
    return matrix



def parse_input(filename):
    inputlist = []
    inputfile = open(filename)
    inputdata = csv.reader(inputfile)
    for line in inputdata:
        inputlist.append(line)
    return inputlist



if __name__ == '__main__':
    main()




