import numpy as np

ls = np.random.randint(1, 101, 100)

result = ["fizzbuzz" if i%15 == 0 else "fizz" if i%3==0 else "buzz" if i%5 == 0 else i for i in ls]
print(result)
