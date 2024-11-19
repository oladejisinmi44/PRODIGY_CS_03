#password strenth checker program
import re

#Password must be at least 8 characters long
password = input("Enter Your Password:")
if len(password) < 8:
    print("password must be at least 8 characters long")
    #password must contain at least one uppercase letter
elif not re.search("[A-Z]", password):
    print("Password must contain at least one UpperCase letter.")
    #password must contain at least one lowercase letter
elif not re.search("[a-z]", password):
    print("Password must contain at least one lowerCase letter.")
    #password must contain at least one number
elif not re.search("[0-9]", password):
    print("Password must contain at least one number.")
else:
    print("Password is Strong")