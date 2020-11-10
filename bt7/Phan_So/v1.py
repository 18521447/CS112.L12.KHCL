def my_gcd(n1: int, n2: int) -> int:
    if n2 == 0:
        return n1
    if n1 == 0:
        return n2
    if n1 < n2:
        n1, n2 = n2, n1
    return my_gcd(n2, n1 % n2)


a = int(input())
b = int(input())
c = int(input())
d = int(input())

count = 0
flag = False
cd = c / d
while a / b < cd:  # nếu a/b != c/d thì a/b luôn luôn < c/d
    a += 1
    b += 1
    count += 1

    flag1 = my_gcd(a, b)
    a = a // flag1
    b = b // flag1

if a / b > cd:
    print(0)
else:
    print(count)
