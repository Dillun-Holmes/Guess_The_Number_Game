import random
line = (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def guess_the_number():
    secret_number = random.randint(1, 100)
    attemps = 0
    print(line)
    print("<          Made by Dillun Holmes            >")
    print(line,"\n\n")

    print(line)
    print("   ######   #     #  ######   #####  ##### ")
    print("  #         #     #  #       #      #      ")
    print("  #     ### #     #  ######   ####   ####  ")
    print("  #      #  #     #  #            #      # ") 
    print("   ######   #######  ######  #####  #####  ") 
    
    print(line)
    print("\n  Im thinking of a number between 1 and 100.\n")
    print(line)

    while True:
        try:
            guess = int(input("\n Take a Guess :"))
            attemps += 1

            if guess > secret_number:
                print("Too high! Try a Lower number")
            elif guess < secret_number:
                print("Too low! Try a higher number")
            else:
                print(line)
                print(f" Great Succcess!! It took you {attemps} attempts")
                print(line)
                input()
                break
        except ValueError:
            print("Invalid input. Enter A valid Number.")

guess_the_number()
print(line)
print(" Thankyou for playing.")
print(line)
