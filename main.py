i = int(input("type some number91 to 100) > "))
if i % 15 == 0:
    print("fizzbuzz")
elif i % 5 == 0:
    print("buzz")
elif i % 3 == 0:
    print("fizz")
else:
    print(i)
