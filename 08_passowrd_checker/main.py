import string
import random
import getpass


def password_checker(password):
    issues = []
    if len(password) < 8:
        issues.append("Password must be at least 8 characters long")
    if not any(char.isdigit() for char in password):
        issues.append("Password must contain at least one digit")
    if not any(char.isupper() for char in password):
        issues.append("Password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        issues.append("Password must contain at least one lowercase letter")
    if not any(char in string.punctuation for char in password):
        issues.append("Password must contain at least one special character")
    return issues

def password_generator():
    return "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for _ in range(10))    


def main():
   password = getpass.getpass("Enter the password: ")
   issues = password_checker(password)
   if len(issues) == 0:
       print("Password is strong")
   else:
       print("Password is weak")
       print(issues)
       isGenerateNewPassword = input("Do you want to generate a new password? (y/n): ")
       if isGenerateNewPassword == "y":
           new_password = password_generator()
           print(new_password)
    
main()