import time
name = input("enter your name: ")
recenttime = time.strftime("%H:%M:%S")
recenttime = int(time.strftime("%H"))
c = name.capitalize()
if(4<=recenttime<12):
    print("good morning sir",c,"its",recenttime)
elif(12>=recenttime<17):
    print("good afternoon sir",c,"its",recenttime)
else:
    print("good night",c,"its",recenttime)
#print("hii",name,"its",recenttime)
#morning time = 04:00:00 to 11:59:00
#afternoon time = 12:00:00 to 16:59:00