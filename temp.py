def ask():
    while True:
        try:
            my_int = int(input("Input an integer: "))
            print("Thank you, your number squared is", my_int**2)
            break
        except Exception:
            print("Opps, you entered an invalid character.")
            print("Try again.")
            continue

ask()