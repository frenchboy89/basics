secret_number = 9

print("Hello, Welcome to Guessing Game Platform\n")

print("""A Secret Number has been stored on the db.
If you get it right, You get a Big profit.
if you get it wrong you won't get anything..
      """)

count = 0
for x in range(3):
    user_input = int(input("Enter Your Guessed Number from 0 - 9\n"))
    count += 1
    if user_input == secret_number:
        print("Hurray! You got 10 bucks...")
        break
    else:
        if count < 3:
            print("Damn! Try Again...")
        else:
            print("Sorry, You Lost 10 bucks")

            