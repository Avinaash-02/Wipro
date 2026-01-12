n = str(input("Enter your password: "))
method = int(input("Choose 1 to Display your password in reverse Order , Choose 2 to keep it hidden  "))
match method:
    case 1:
        print(n[::-1])
    case 2:
        print(f'Password is confidential :{"#"*len(n)}')
