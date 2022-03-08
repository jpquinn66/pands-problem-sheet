# program to find square root of a number using Newtons method
# Author JP Quinn
# G00411303

# Newtons method New x = 0.5 * (x + b/x)

def newton_method(number, number_iters = 100):

    a = float(number)

    for i in range(number_iters):
        number = 0.5 * (number + a / number)

    return round(number,2)

a = float(input("Enter a number: "))

print("The Square root of the number is approx: ", newton_method(a))


