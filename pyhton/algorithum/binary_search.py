def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint +1
        else:
            last = midpoint - 1

    return None

def verify(index):
    if index is not None:
        print("Target found at inex: ", index)
    else:
        print("Target is not found in given list")

data = range(1,11)
value = binary_search(data,4)
verify(value)
print(f"The value of target is {data[value]}")
print(data)