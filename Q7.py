count = 2
def timNhanTu(i, count):
    if i == 1 :
        return 1
    if (i % count == 0):
        print(count, end=" x ")
        return timNhanTu(i/count, count)
    count += 1
    return timNhanTu(i, count)

print("Nhập vào số nguyên tố: ")
k = int(input())
print(k, "=",end="")
timNhanTu(k,2)

