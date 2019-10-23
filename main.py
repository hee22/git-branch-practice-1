import numpy as np

ls = np.random.randint(1, 101, 100)

print(ls)
for i in ls:
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)

