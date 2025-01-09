odd = []
even = []
not_valid = []
for num in range(6):
    number = input(f"please input number {num+1} of 6 :")
    if number.isdigit() or (number.startswith('-') and number[1:].isdigit()):
        number = int(number)
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    else:
        not_valid.append(number)
    
    
print(f"all the odd numbers are {odd}")
print(f"all the even numbers are {even}")
print(f"these are not valid inputs {not_valid}")
