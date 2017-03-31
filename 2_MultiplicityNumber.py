#2_MultiplicityNumber.py
#given a number, output True if it is a multiple of 3 and not a multiple of 5
i = int(input('Enter integer data: '))
if i % 3 == 0 and i % 5 != 0:                               #checking the conditions
    print('True. Введённое число кратно 3 и не кратно 5')   #output if True
else:
    print('False')                                          #output if False
