def kiemTraSoNguyenTo(n):
    i = 2
    while i < n / 2 + 1:
        if n % i == 0: 
            return False
        i += 1
    return True

j = 10000
count = 0
while j < 99999:
    if (kiemTraSoNguyenTo(j)):
        print(j, end="; ")
        count += 1
    j += 1
print(count)