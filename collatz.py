## a program to output values based on collatz conjecture
##Author John Quinn (G00411303)

## code help from https://www.webucator.com/article/collatz-conjecture-in-python/

print ('Please enter a number:')
a = input()
a = int(a)
numList = [a]

while a!= 1:
    print(a)
    if (a %2) == 0:
        a = a/2
    else: 
        a=(a*3)+1
        numList.append(a)


    



