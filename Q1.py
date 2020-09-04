print("Nhập vào 2 số:")
rows = int(input())
cols = int(input())
arr = []
for x in range(rows):
    row = []
    for y in range(cols):
        row.append(x * y)
    arr.append(row)
print(arr)