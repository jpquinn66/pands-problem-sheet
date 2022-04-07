# pands-problem-sheet
Repository for problem sheets

File 1: bmi.py

This file stores an input as myHeight and another as myWeight, both set as integers. I used a formula found online to use these to calculate bmi

https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1

the bmi was calculated and stored as a string myBmi which was then output via print()


File 2: secondstring.py

Takes and input and stores as sentence, using code seen on w3schools [::-1] reverses code while code from stacked overflow [::2] outputs every second letter, sentence then output via print()

File 3: collatz.py

I watched the video on the collatz conjecture far too often to try figure out the formula needed. I used variable a to get a number via input, that was then made to a list, numList, I used a while statement and then if else, while a is not equal to one the program uses the if statement to check if the number is divisible by 2, if it is we divide by 2, else we multiply by 3 and add 1. each new iteration is added to numlist. the while statement ends the program when we hit 1

I adapted code from https://www.webucator.com/article/collatz-conjecture-in-python/

File 4: weekday.py

This package checks the day of the week, it prints a different string depending on if its a weekday or not. I found the datetime package on stackedoverflow. I used datetime.datetime.today().weekday, it assigned a number to weekday depending on the weekday, 0 to 6, so I used the if statement to say if its less than 5 its a weekday


https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date

File 5: squareroot.py

This program takes a number via input and uses Newtons method to get the square root. I found code on https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method which I adapted to take a float. For newtons mmethod we took a number, assigned to a, and applied the formula number = 0.5 * (number + a / number) to it and output this with a string

File 6: es.py

This file opens a text file and counts the occurences of the letter e. I downloaded the 1st chapter of moby dick for this and saved it to a txt doc, I was getting an error when I tried to open and read the file, when I googled the error I found the solution on stacked overflow, it worked once I added the encoding='utf-8' which allowed it to read the chapter in the format I had saved. I set the variable letter to e, and used data as a variable to read the file. and then data.count(letter) counted the occurences of the letter e

https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python

File 7: plottask.py

This file displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4]. For this I imported matplotlib and numpy. I imported numpy for the np.power() function, I found this on https://numpy.org/doc/stable/reference/generated/numpy.power.html. I thought the results were hard to make out as the f and g lines were quite low on the chart while h was quite high so I found the subplot option to seperate them on ##https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html I set a title for each graph using set_title







