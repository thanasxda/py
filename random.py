#!/usr/bin/env python
import random2
seed = input("input:\n")
n_min = 1
n_max = 99
n_numbers = 12
random2.seed(seed)
numbers = [random2.randint(n_min, n_max) for i in range(0, n_numbers)]
print("generated numbers:", numbers)
