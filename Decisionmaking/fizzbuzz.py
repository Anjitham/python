number=int(input("Enter a number:"))

if number%15==0:
    print("FizzBuzz")
elif number%5==0:
    print("Buzz")
elif number%3==0:
    print("fizz")
else:
    print("====")