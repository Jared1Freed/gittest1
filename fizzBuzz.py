#print numbers 1-100
for i in range(100):


    # if number is divisable by 3 and 5 print "fizzBuzz"
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
#test

    # if number is divisable by 3 "fizz"
    elif i % 3 == 0:
        print("fizz")
        continue


    # if number is divisable by 5 print "buzz"
    elif i % 5 == 0:
        print("buzz")
        continue

    print(i)

