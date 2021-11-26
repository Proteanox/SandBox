password = input("Enter Your Password: ")
password_length = len(password)
while password_length < 10:
    print("Invalid Password")
    password = input("Enter Your Password: ")
    password_length = len(password)
with open('passwords.txt', 'w') as f:
    f.write('*' * password_length)