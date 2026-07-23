# required arguments
def average(a,b):
    print("the average of" , (a+b)/2)
average(4,6)
# default arguments
def name(fname,mname = "ahmad",lname = "abid"):
    print("hello",fname,mname,lname)
name("fatima","noor","hamza")
# keyword arguments
def name(fname,mname,lname):
    print("hello",fname,mname,lname)
name(lname="rabiya",fname="noor",mname="hira")
# variable length argument
def average(*numbers):
    sum = 0
    for i in numbers:
     sum = sum+i
    print("the average is:" , sum/ len(numbers))
average(10,5)