num = int(input("input a number: "))

temp = 1

count = [1,]

while temp <= num:
    if temp == num:
        print(count)
        break
    else:
        temp += 1
        count.append(temp)
