import re
def email_valid(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'

    if re.match(email_regex,email):
        return True
    else:
        return False
    
def main():
    email = input('enter the email address')
    if email_valid(email):
       print("email is valid")
    else:
       print("email is invalid")
    
if __name__ == '__main__':
    main()