import random
print("code of love calculator")
name1 = input("your name: ")
name2 = input("your crush name: ")
love = random.randint(1,100)
print(f"\n{name1} + {name2}")
print(f"love percentage: {love}%")
if love > 90:
    print("shaadi pakki hai! ")
elif love > 70:
    print("bohat gehra connection hai")
else:
     print("thori koshish aur karo")