def add_array(arr,divisible,remainder_1,remainder_2):
    sum_var = 0
    for i in (arr):
        if int(i) % 3 == 0:
            divisible.append(i)
        elif int(i) % 3 == 1:
            remainder_1.append(i)
        else:
            remainder_2.append(i)
        sum_var += int(i)
    divisible.sort(reverse = True)
    remainder_1.sort(reverse = True)
    remainder_2.sort(reverse = True)
    return sum_var
    
def calculating(sum_var,remainder_1,remainder_2):
    if sum_var % 3 == 1:
        if len(remainder_1) > 0:
            remainder_1.pop()
        else:
            remainder_2.pop()
            remainder_2.pop()    
    if sum_var % 3 == 2:
        if len(remainder_2) > 0:
            remainder_2.pop()
        else:
            remainder_1.pop()
            remainder_1.pop()
            
if __name__ == '__main__':
    arr = input().strip()
    arr = [str(i) for i in arr]
    divisible = []
    remainder_1 = []
    remainder_2 = []
   
    result = []
    sum_var = add_array(arr,divisible,remainder_1,remainder_2)
    
    calculating(sum_var,remainder_1,remainder_2)
    
    result =[]
    result = sorted(divisible + remainder_1 + remainder_2,reverse = True)
    result = ''.join(result)
    print(result)

# làm sao rút gọn if else trên add_array
# 3 cái test > 0.15