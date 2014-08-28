import time
import random

def getPivot(data):
    return data[0]

def partition(data):
    pivot_value = getPivot(data)
    left, equal, right = [], [], []
    for element in data:
        if element > pivot_value:
            right.append(element)
        elif element < pivot_value:
            left.append(element)
        else:
            equal.append(element)
    return left, equal, right

def qsort(data):
    if data:
        left, equal, right = partition(data)
        return qsort(left) + equal + qsort(right)
    return data

array = []
for i in range(int(raw_input())):
    nb = raw_input()
    array.append(float(nb) if '.' in nb else int(nb))

print " ".join(str(x) for x in qsort(array))

