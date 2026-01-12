name = int(input("Enter your Username: ").split())
passkey = int(input("Enter your Username: ").split())
def validate(name,passkey):
    if name == "admin" and passkey=='passkey':
        return True
    return False
if validate(name,passkey):
    print("SuccessFully Logged in")
else:
    print("Enter correct Details man!!")
