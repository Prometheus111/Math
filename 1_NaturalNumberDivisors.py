#1_NaturalNumberDivisors.py
#calculate the number of natural divisors of the number x
#(include 1 and the number itself; x <= 30000)
x = int(input('Enter the number x (x <= 30000): '))     #input number x
def f(x):                                               
    n = 0                                               
    print('All natural divisors of a number x:')        #output of all natural divisors
    for i in range(1, x + 1):                           
        if (x % i == 0):                                #for all natural divisors
            n += 1                                      #calculate divisors
            print(i)                                    #output divisors
    print('Total natural divisors of the number x:', n) 
f(x)                                                    #function call
