A = [2, 2, 4, 2, 1, 2, 2, 3, 3, 4, 4, 2, 3, 4, 1, 2, 3, 4, 4, 2]

i = 0
print(A)
for i in range(len(A)):

    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print(A)
