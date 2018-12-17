number = int(input("What is your age? "))

# between 0 and 150
if number < 0 or number > 150:
    print("Not possible age!")

# between 0 and 149
if number not in range(0, 150):
    print("Range check not passed")
else:
    print("Passed check! Age: " + str(number))

    if number <= 12:
        print("Child age: " + str(number))
    elif number <= 20:
        print("Teenager age: " + str(number))
    elif number <= 29:
        print("Twen age: " + str(number))
    else:
        print("Old age: " + str(number))
