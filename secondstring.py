## program that asks users to enter a sentence and then outputs every second letter in reverse

sentence = input('Please enter a sentence: ')
sentence = (sentence) [::-1] # slice method found on w3schools reverses string
sentence = (sentence) [::2]  # method on stackoverflow returns every 2nd letter

print(sentence)



