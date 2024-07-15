import random

while True:
    print("\n================== Password Generator App ==================\n\n")

    passlen = int(input("Enter the length of password (8-15): "))
    
    if 8 <= passlen <= 15:
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@Ł!&#$/\|<>*ł?£&{}[]ß€;:-_÷^˘"
        p = "".join(random.sample(s, passlen))
        print("\n\nYour password is:", p)
        if passlen == 15:
            print("\nPassword should not have 15 or more characters.\n")
    else:
        print("\nPassword length should be between 8 and 15 characters.")
        continue

    opt = input("\nDo you want to try again? (da/ne): ")

    if opt.lower() == 'da':
        continue
    elif opt.lower() == 'ne':
        print("Exiting program....")
        break
    else:
        print("Please enter da/ne:")
