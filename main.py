# game title
print(r'''  __                 ___                                
 /__      _   _  _    | |_   _. _|_   \    / _  ._ _| | 
 \_| |_| (/_ _> _>    | | | (_|  |_    \/\/ (_) | (_| o 
                                                         ''')
print()
# instructions
print("Welcome to Guess That Word!")
print("===========================")
print("Can you guess the secret word?") 
print("- It is five letters in length.")
print("- You will be prompted to enter ONE letter for each turn.")
print("- If the letter you guess is not in the secret word, it will count as one strike!")
print("- If you correctly guess all the letters in the secret word before reaching five strikes, you win! Good luck!")
print("============================")
print()
# Create a variable for secret word
actual = "state"

# create a funtion: prompting user to enter a single letter
def getletter():
  # Create a variable to hold the letter with a dummy value
  letter = ""
# Until the user enters a string with ONE character...
  while(len(letter) != 1):
    # Prompt the user to enter a letter
    letter = input("Enter a letter: ")
  # return the variable, 'letter'  
  return letter
  
# create function: display correctly guessed letters & underscore for incorrectly guessed
def displayactual(word, guesses):
  # Go through each letter in the secret word, and determine HOW we display it
  for letter in word:
    # If this letter (from the secret word) has been guessed, display the letter
    if(letter in guesses):
      print(letter, end = " ")
    # otherwise, display an underscore " _"
    else:
       print("_", end = " ")
  print()
# Create a function that determines if the user has won the game
def won_game(word, guesses):
   # ...and create a variable that is set to "True"
  won = True
   # Go through each letter in the secret word
  for letter in word:
     # Check if the letter has been guessed
    if(letter not in guesses):
       # If it has NOT been guessed, set the variable we created to False, and stop the loop
      won = False
      break
  # return the result    
  return won
  
# Create a variable for the count to hold number of strikes, set to 0
strike_count = 0
#sum = strike_count
# list to hold user guesses as values
guesses = []

                ## MAIN BODY OF CODE ## 
  
# while loop to prompt user to enter a guess UNTILL they win OR reach FIVE strikes
while(not(won_game(actual, guesses)) and (strike_count < 5)):
  #prompt user to enter a letter
  userguess = getletter()
  # if statement in case input is more than one character - use the "getletter()" functin to ensure user validation
  guesses.append(userguess)
  displayactual(actual, guesses)
  # if statement for when a guess is accurate & add to list of guesses
  if userguess not in actual:
    strike_count += 1    
  # display how many strikes they have so far & remind them how many   
    print(f"{userguess} is not in the word.")
    print(f"You have {strike_count} strike. If you get 5, you lose!") 
        
if(won_game(actual, guesses) is True):
  print("You wone!")
else:
  print("You lost!")