


age_of_lan = 22

count = 0
while count < 3:
    guess_age = int(input("age_of_lan:"))
    if guess_age == age_of_lan:
        print("you are right!")
        break
    elif guess_age < age_of_lan:
        print("stubid!")
    else:
        print("stubid too")
    count += 1
else:
    print("fuck off!")