#2_MultiplicityNumber.py
#given a number, output True if it is a multiple of 3 and not a multiple of 5
i = int(input('Enter integer data: '))
#checking the conditions
if i % 3 == 0 and i % 5 != 0:
    #output if True
    print('True. The number entered is a multiple of 3 and not a multiple of 5')
else:
    #output if False
    print('False')
