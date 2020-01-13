#guessing game


numbers = [13,15,17,21,25]

while True:
    answer = input("Predict a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit")
    if answer in numbers:
        print("You guessed correct!")
    else:
        print("You guessed wrong")

        
