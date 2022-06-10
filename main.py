import os
name = input("What is your name?")
print("hello," + name)
host = input("What Server would you like to check?")
print("Alright let me check that for you, " + name)
hostname = host
response = os.system("ping -c 1" + hostname)
if response == 0:
    print(hostname, "is up!")
else:
    print(hostname, "is down!")
