"""
Chase Gillis  2/15/23	CSCI-UA 2 - 006
Assignment #4 Problem #2
I worked alone.
Title: Collatz Conjecture
"""


#Set variables and accumulators
accumulator = 1
incaccumulator = 0
facaccumulator = 0
even = 0
odd = 0
fac = ''
total = 1

#Check if input is valid
while True:
    number = int(input('Enter a positive number: '))
    if number <= 0:
        print('Invalid entry. Try again')
        continue
    elif number == 1:
        print('This number is already equal to one.')
        continue
    else:
        break
#State what needs to be stated prior to loops
startingnumber = number
ognum = number
inc = ''
#format
print()
print('Calculating....')
print()
#set initial loop
while number != 1:
    number = int(number)
    total = total + number
    #Set for even numbers
    if number % 2 == 0:
        typ='Even!'
        ognum = number
        print(accumulator, ".", ' ', number, sep='', end='')
        if (startingnumber != number) and (startingnumber % number == 0):
            print('->', typ, inc, end='')
        else:
            print('->', typ, inc)
        if (startingnumber != number) and (startingnumber % number == 0):
            fac = print('Factor of ', startingnumber, '!', sep='')
            facaccumulator += 1
        else:
            fac = ''
        
        number = number / 2
        number = int(number)
        accumulator += 1
        even += 1
        if number > ognum:
            inc = 'Increased! '
            incaccumulator += 1
        else:
            inc = ''
    #set for odd numbers
    else:
        typ='Odd!'
        ognum = number
        print(accumulator, ".", ' ', number, sep='', end='' )
        if (startingnumber != number) and (startingnumber % number == 0):
            print('->', typ, inc, end='')
        else:
            print('->', typ, inc)
        if (startingnumber != number) and (startingnumber % number == 0):
            fac = print('Factor of ', startingnumber, '!', sep='')
            facaccumulator += 1
        else:
            fac = ''
        
        number = (number * 3) + 1
        number = int(number)
        accumulator += 1
        odd += 1
        if number > ognum:
            inc = 'Increased! '
            incaccumulator += 1
        else:
            inc = ''
#Format and display results
print(accumulator, ".", ' ', number, sep='', end='' )
print('-> Odd!')
odd = odd + 1
print()
print('It took a total of', accumulator, 'steps to reach the Collatz conjecture!')

print('Along the way, there were:')

print('->', even, 'even number(s)')

print('->', odd, 'odd number(s)')

print('->', incaccumulator, 'increase(s)')

print('->', facaccumulator, 'factor(s) of', startingnumber)
#Do some math
y = total / accumulator
average = format(y, '.2f')

print('The average number in the sequence is', average)

