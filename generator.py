import random
##################################################################################################################
ask = input("Would you like to generate a password? y or n (use lowercase!) ")
##################################################################################################################
if ask == "y":

    symbol_ask = input("Would you like to use symbols in your password? ex: ()-+. y or n ")

    if symbol_ask == "y":

        number_ask_y = input("How much numbers would you like in your passwords? (1 - 30) ")

        if number_ask_y == "1":

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

            length = 1
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "2":

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

            length = 2
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "3":

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

            length = 3
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "4":

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

            length = 4
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "5":

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

            length = 5
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "6":

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

            length = 6
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "7":

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

            length = 7
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "8":

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

            length = 8
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "9":

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

            length = 9
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "10":

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

            length = 10
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "11":

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

            length = 11
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "12":

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

            length = 12
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "13":

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

            length = 13
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "14":

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

            length = 14
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "15":

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

            length = 15
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "16":

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

            length = 16
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "17":

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

            length = 17
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "18":

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

            length = 18
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "19":

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

            length = 19
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "20":

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

            length = 20
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "21":

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

            length = 21
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "23":

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

            length = 23
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "24":

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

            length = 24
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "25":

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

            length = 25
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "26":

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

            length = 26
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "27":

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

            length = 27
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "28":

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

            length = 28
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "29":

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

            length = 29
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "30":

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

            length = 30
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
    if symbol_ask == "n":

        number_ask_y = input("How much numbers would you like in your passwords? (1 - 30) ")

        if number_ask_y == "1":

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

            length = 1
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "2":

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

            length = 2
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "3":

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

            length = 3
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "4":

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

            length = 4
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "5":

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

            length = 5
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "6":

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

            length = 6
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "7":

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

            length = 7
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "8":

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

            length = 8
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "9":

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

            length = 9
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "10":

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

            length = 10
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "11":

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

            length = 11
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "12":

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

            length = 12
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "13":

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

            length = 13
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "14":

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

            length = 14
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "15":

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

            length = 15
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "16":

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

            length = 16
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "17":

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

            length = 17
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "18":

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

            length = 18
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "19":

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

            length = 19
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "20":

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

            length = 20
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "21":

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

            length = 21
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "23":

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

            length = 23
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "24":

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

            length = 24
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)

        if number_ask_y == "25":

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

            length = 25
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "26":

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

            length = 26
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "27":

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

            length = 27
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "28":

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

            length = 28
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "29":

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

            length = 29
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
        if number_ask_y == "30":

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

            length = 30
            amount = 3

            for x in range(amount):
                password = "".join(random.sample(all, length))
                print("Password is: " + password)
##################################################################################################################

##################################################################################################################
if ask == "n":
    print("Quit succesfully")
##################################################################################################################
else:
    print("Generator Closed.")
