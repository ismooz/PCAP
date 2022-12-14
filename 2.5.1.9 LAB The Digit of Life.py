birthdate = input("Please enter your birthdate like DDMMYYYY : ")

def dateSum(date):
    while len(date) > 1:
        sum = 0
        for n in date:
            sum += int(n)
        date = str(sum)
    print(sum)
    
dateSum(birthdate)

# Autre solution proposée par IA

"""birthdate = input("Please enter your birthdate like DDMMYYYY : ")

def dateSum(date):
    date_sum = 0
    for n in date:
        date_sum += int(n)
    # If the length of the date sum is greater than 1, we need to add the digits
    # together until the length is 1
    while len(str(date_sum)) > 1:
        new_sum = 0
        for nd in str(date_sum):
            new_sum += int(nd)
        date_sum = new_sum
    print(date_sum)

dateSum(birthdate)""" 
