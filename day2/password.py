
_username = "lan"
_password = "123"

username = input("username:")
password = input("password:")

if _username == username and _password ==password:
    print("Wecome {name} to login... ".format(name=username))
else:
    print("Invalid username or password!" )