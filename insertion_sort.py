# INSERTION-SORT
import numpy as np
def insertion_sort(limit, x):
     = np.random.randint(limit , size = x)

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

question1 = int(input('How many numbers you want to order?'))
question2 = int(input('And, now, what is the limit number?'))

results = insertion_sort(question2, question1)
print(*results, sep=' -> ')
