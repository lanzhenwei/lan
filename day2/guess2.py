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
    if count == 3:
        confirm = input("Do you want try again?")
        if confirm !='n':
            count = 0


#else:
#    print("fuck off!")