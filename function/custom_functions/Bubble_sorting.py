# Bubble sorting
arr = [7, 3, 9, 2, 0, 4, 8, 1, 6, 5]
def bubble_sort(seq):
    n = len(seq)
    for i in range(n-1):
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                temp = seq[j]
                seq[j] = seq[j+1]
                seq[j+1] = temp
    return seq

print(bubble_sort(arr))