import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will charge 2 dollars per day")

elif type == "t2.medium":
    print("it will charge 4 dollars per day")

elif type == "t2.xlarge":
    print("it will charge 6 dollars per day")
    
else:
    print("please provide a valid instance type")