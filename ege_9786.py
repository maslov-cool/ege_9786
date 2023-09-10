with open('17_9786.txt') as f:
    A = [int(i) for i in f]
max25 = 0
for i in sorted(A)[::-1]:
    if i % 100 == 25:
        max25 = i
        break
B = []
for i in range(len(A) - 2):
    s = (len(str(abs(A[i]))) == 4) + (len(str(abs(A[i + 1]))) == 4) + \
        (len(str(abs(A[i + 2]))) == 4)
    if s < 3 and A[i] + A[i + 1] + A[i + 2] <= max25:
        B.append(A[i] + A[i + 1] + A[i + 2])
print(len(B), max(B))








