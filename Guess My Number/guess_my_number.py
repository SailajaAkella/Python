low = 0
high = 100
print("Please think of a number between 0 and 100!")
while(True):
    ans = round((low + high) // 2)
    
    print("Is your secret number ",ans,"?")
    num = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if(num in ('h','l','c')):

        if(num == 'h'):
            high = ans
        elif(num == 'l'):
            low = ans
        elif(num == 'c'):
            print("Game over. Your secret number was: ",ans)
            break
    else:
        print("Sorry, I did not understand your input.")
    