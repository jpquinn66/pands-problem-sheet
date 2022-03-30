##program to open text file and cound number of es
##Author JP Quinn G00411303

filename = 'moby_dick.txt'
with open (filename,'r',encoding='utf-8') as f:

    data = f.read()

    letter = 'e'

    a =  data.count(letter)

    f.close()

    print('The letter ',letter,' appears ',a, ' times')




