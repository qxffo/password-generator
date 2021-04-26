import random
##################################################################################################################
urmom = "1k pounds"

ask = input("Would you like to generate a password? y or n (use lowercase!) ")
##################################################################################################################

symbol_ask = input("Would you like to use symbols in your password? ex: ()-+. y or n ")

if symbol_ask == "y":

    number_ask_y = int(input("How much numbers would you like in your passwords? (1 - 30) "))
    amount_ask_y = int(input("How much passwords would you like to generate? "))

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "(){}[};:.,-+=|/"

    upper, lower, nums, syms = True, True, True, True

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols

    length = number_ask_y
    amount = amount_ask_y

    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(ask + password)

if symbol_ask == "n":

    number_ask_n = int(input("How much numbers would you like in your passwords? (1 - 30) "))
    amount_ask_n = int(input("How much passwords would you like to generate? "))

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "(){}[};:.,-+=|/"

    upper, lower, nums, syms = True, True, True, False

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols

    length = (number_ask_n)
    amount = (amount_ask_n)

    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
##################################################################################################################
else:
    print("Generator Closed.")
