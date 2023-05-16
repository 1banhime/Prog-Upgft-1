n1 = int(input("input the 1st number: "))
n2 = int(input("input the 2nd number: "))
n3 = int(input("input the 3rd number: "))
n4 = int(input("input the 4th number: "))
n5 = int(input("input the 5th number: "))

tally = [n1, n2, n3, n4 ,n5]

tally.sort()

print("the lowest number is ", tally[0], "the biggest number is ", tally[-1], ".")