                           ### Welcome to Hangman Game ###
# Import required libraries
import random
import time

# Initial Steps to invite in the game:
print("**** \U0001F600 Welcome To Hangman Game \U0001F600 ****")
name = input("Enter your name : ")                          # Here the user is asked to enter the name first
welcome = ("Hello "+ name.capitalize())
print("*" *40)
print(welcome.center(40," "))
print("*" *40)
time.sleep(2)
print("The game is about to start!\nLet's Play Hangman!")
print("Try to guess the color in less than 10 attempts")
time.sleep(2)

# this asks the user to play the game again or exit
def play_again():
        ans = input("you want to play again? y= yes or n = no \n")
        if ans == 'y':
                hangman()
        else:
                print("Thank You For Playing!")
                exit()
# main function             
def hangman():
    # list of colors
    colors = ['peach','orange','blue','red','purple','scarlet','indigo','green','emerald','lime','cobalt','coral','aqua'
             'black', 'violet', 'grey', 'yellow','brown','white','magenta','pink','golden','charcoal','teal','amber'] 
    
    color = random.choice(colors)            # Function will choose one random color from the list of colors  
    valid_letters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ""
    
    while len(color)> 0:
        main = ""
        
        for letter in color:                 # all letters from the input word taking one at a time. 
            if letter in guessmade:          # comparing the letter with the letter in guess 
                main = main + letter
            else:
                main = main + "_" + " "
                
        #check win        
        if main == color:
                print("The color is ",main)  # this print the correct word 
                print("Congrates \U0001F600 !! You Won\n")
                play_again()
                break
                
        print("Guess the color :" , main)       
        guess = input()                      # this ask user to guess the word 
               
                
        if guess in valid_letters:
            guessmade = guessmade + guess    # every input letter will be stored in guessmade
        
        else:
            print("Enter a valid character") # if user has input the invalid letter then it will ask user to enter valid input
            guess = input()
          
           
        if guess not in color:
            turns = turns - 1                # for every failure 1 will be decreased in turns 
            
            if turns == 9 :
                print("Wrong Answer")
                time.sleep(1)
                print(" 9 turns left")
                print("-------------")
                
            if turns == 8 :
                print("Wrong Answer")
                time.sleep(1)
                print(" 8 turns left")
                print("-------------")
                print("      O      ")
                
            if turns == 7 :
                print("Wrong Answer")
                time.sleep(1)
                print(" 7 turns left")
                print("-------------")
                print("      O      ")   
                print("      |      ")
                
            if turns == 6 :
                print("Wrong Answer")
                time.sleep(1)
                print(" 6 turns left")
                print("-------------")
                print("      O      ")   
                print("      |      ")   
                print("     /       ")
                
            if turns == 5 :
                print("Wrong Answer")
                time.sleep(1)
                print(" 5 turns left")
                print("-------------")
                print("      O      ")   
                print("      |      ")   
                print("     / \     ")
                print("             ")
            
            if turns == 4 :
                print("Wrong Answer")
                time.sleep(1)
                print(" 4 turns left")
                print("-------------")
                print("     \O      ")   
                print("      |      ")   
                print("     / \     ")
                print("             ")
            
            if turns == 3 :
                print("Wrong Answer")
                time.sleep(1)
                print(" 3 turns left")
                print("-------------")
                print("     \O/   | ")   
                print("      |      ")   
                print("     / \     ")
                print("             ")
                     
            if turns == 2 :
                print("Wrong Answer")
                time.sleep(1)
                print(" 2 turns left")
                print("-------------")
                print("     \O/  _| ")   
                print("      |      ")   
                print("     / \     ")
                print("             ")
                
            if turns == 1 :
                print("Wrong Answer")
                time.sleep(1)
                print(" 1 turns left")
                time.sleep(1)
                print("Last Breaths counting, Takecare for that !!")
                print("-------------")
                print("     \O/_|   ")   
                print("      |      ")   
                print("     / \     ")
                print("             ")
                
            if turns == 0 :
                print("Wrong Answer, You Lost")
                time.sleep(1)
                print(" 0 turns left")
                print("You let a kind Man Die \U0001F62A !!!")
                print("-------------")
                print("      |      ")
                print("      |      ")
                print("      O      ")   
                print("     /|\     ")   
                print("     / \     ")
                print("             ")
                time.sleep(1)
                play_again()
            
            

hangman()                                                  # hangman() would start again if the play_again executes to yes

