password = "ab$3"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess != password and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the password: \n")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("\nMaximum try reached... try again after 3 eternity later!")
else:
    print("\n...Welcome User...")