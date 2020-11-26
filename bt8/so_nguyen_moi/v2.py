if __name__ == '__main__':
    n = input().strip()
    digits = list(map(int, list(n)))
    total = sum(digits)

    replaced = False

    alternative_digit_for = {
        0: 9, 
        1: 8, 
        2: 7
    }

    for i, digit in enumerate(digits):
        removed_digit = total - digit
        remainder = removed_digit % 3

        new_digit = alternative_digit_for[remainder]
        
        if new_digit > digit:
            digits[i] = new_digit
            replaced = True
            break
    
    if not replaced:
        remainder = (total - digits[-1]) % 3
        new_digit = alternative_digit_for[remainder]
        
        if new_digit == digits[-1]:
            new_digit -= 3

        digits[-1] = new_digit

    
    result = ''.join(map(str, digits))

    print(result)
