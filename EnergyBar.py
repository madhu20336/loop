fix_number=5
chance=10
while chance>0:
    digit=0
    number=int(input("enter a number to win the game: "))
    if fix_number==number:
        print("you are win ! ,your guessing number is correct")
        break
    elif number==fix_number:
        diff=number-fix_number
        chance=chance-diff
        if chance < 0:
            print("chance finished")
            break
        else:
            print("remaining chance have  finishe",chance)
    elif number<fix_number:
        diff=fix_number-number
        chance=chance-diff
        if chance<0:
            print("chance finishe")
        else:
            print("remaining chance have  finishe",chance)
    else:
        print("your chance is finishe!")
        print("again try")