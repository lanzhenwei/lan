_username = "lan"
_password = "12a"
username = input("username:")
password = input("password:")
count = 0
while count < 3:
    if username == _username and password == _password:
        print("Bingo!")
        break
    else :
        print("shit!")

    count += 1
    if count == 3:
        confirm =input("wow")
        count = 0

