#This program asks a users height and weight and calculates BMI
print ('Hello, what is your name?')
myName = input()
print ('nice to meet you ' + myName)

print(myName + ' please enter your height (in centimetres)')
myHeight = input()
myHeight = int(myHeight)/100

print(myName + ' can you please enter your weight (in kilograms)')
myWeight = input()
myWeight = int(myWeight)

myBmi = myWeight / (myHeight ** 2)
myBmi = str(myBmi)

print(myName + ' your BMI is '+ myBmi)
