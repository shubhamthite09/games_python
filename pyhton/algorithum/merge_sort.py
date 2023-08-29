import random

def merge_sort(list):
    if len(list) <= 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)
def split(list):
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left, right
def merge(left, right):
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    return l


alist = [45,78,90,23,45]
l = merge_sort(alist)
print(l)
