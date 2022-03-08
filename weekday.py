# File to check if it is a weekday
#Author JP Quinn

#helped by stackoverflow

import  datetime

weekno = datetime.datetime.today().weekday()

if weekno <5:
   print ("Today is a weekday")

else:
    print ("Weekend")

