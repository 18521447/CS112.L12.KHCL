n = int(input())
Max_choose = n // 3
remainder = n % 3
if(remainder == 0):
    print(Max_choose * 7)
elif(remainder == 1):
    print((Max_choose - 1) * 7 + 4)
elif(remainder == 2):
    print(Max_choose * 7 + 1)