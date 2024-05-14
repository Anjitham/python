lower = 10
upper = 50
count = 0

for number in range(lower, upper + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number,end=" ")
            count += 1
            if count == 10:
                break
