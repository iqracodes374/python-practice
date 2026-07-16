# if else statment
a = int(input("enter you age: "))
print("your age is:" ,a )
# conditional operatar
#<,>,<=,>=,!=
if (a>18):
    print("you can drive")
else:
    print("you cannot drive")
# elif statment
num = int(input("enter your value of num: "))
if (num<0):
    print("number is nagetive")
elif (num==0):
    print("number is zero ")
else:
    print("number is positive")
# nested if else statment
num = 18
if (num<0):
    print("number is nagetive ")
elif (num>0):
    if (num<=10):
        print("the number is between 1 to 10")
    elif (num>10 and num<=20):
        print("the number is between 10 to 20")
    else:
        print("the number is greater than 20")
else:
    print("the number is zero")
