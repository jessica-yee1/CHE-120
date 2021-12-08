# Jessica Yee (JY), 20974409
# Michael Tchoulak(MT), 20958551
import random
HANGMAN_PICS = ['''
   ☁
  ⋆⋆     
       
       
      ''', '''
    ☁
   O   
  ₊⁺₊    
       
      ''', '''
     ☁  
   O   
 ₊⁺|   
       
      ''', '''
  ☁
   O   
  /|⁺₊   
       
      ''', '''
    ☁
   O   
  /|\  
 ₊⁺    
      ''', '''
  ☁
   O   
  /|\  
  /⁺₊    
      ''', '''
   ☁
   O   
  /|\  
  / \  
      '''] #JY we can modify this to add more/less parts to enable more/less 
HANGMAN_PICS.reverse()
animals  = 'ant baboon badger bat bear beaver camel cat clam cobra couga coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
fruits = 'grape melon pumpkin tomato apple avocado banana cantaloupe cherry durian gooseberries guava kiwi mango pear peach pineapple plum pomegranate strawberry watermelon raspberry blackberry blueberry lychee lemon lime honeydew cranberry coconut dragonfruit fig papaya starfruit olive'.split()
school = 'pencil eraser marker whiteboard chalkboard desk chair student teacher exam library gym calculus english history geography french spanish algebra biology physics chemistry science textbook test homework grades music band clubs project lunch recess stapler binder folder notebook detention essay'.split()
ocean = 'buoy deepwater nautical ocean sea saltwater coast tide algae gulf kelp seagrass barracuda barnacle fish dolphin crab seal jellyfish lobster oyster turtle urchin seagull seahorse shark shrimp sponge stingray walrus whale driftwood shore wave tsunami boat ship conch seashell current reef coral flounder octopus plankton scallop worms'.split()
#JY word bank, the words can be inputted as one string rather than individual strings for each word thanks to the split() function

def getRandomWord(wordList):
    """
    This function returns a random string from the passed list of strings.
    """
    wordIndex = random.randint(0,len(wordList)-1) #JY in the list of words, chooses the index of a random word and assigns to variable
    return wordList[wordIndex] #JY returns the word assigned to the random index

missedLetters = '' #JY empty string because letters have not been guessed yet
correctLetters = ''

    
def theme_chooser() :   
    v=input("Choose a theme! You have a choice between animals, school, ocean and fruits: ")
    if  v.lower().startswith('a'):
        print("hhoo")
        return animals
    if v.lower().startswith('s') :
        return school
    if  v.lower().startswith('o') :
        return ocean
    if  v.lower().startswith('f'):
        return fruits
    else :
        print("I have no idea what that means, I think you'll like this one")
        return animals
secretWord = getRandomWord(theme_chooser())#JY assigns the random word chosen from word bank to variable
print(secretWord)           
 
gameIsDone = False #JY all while loops "while True" will continue until gameIsDone=False

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)]) #JY displays the image of hangman relative to the number of incorrect letters guessed
    print()
    
    print('Missed letters:', end='') #JY displays letters guessed that aren't correct
    for letter in missedLetters:
        print(letter, end='') #JY prints each character in missedLetters separated by a space
    print()
    
    blanks = '_ '*len(secretWord) #JY blanks representing the length of the word to be guessed
    
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters: #JY if the letter guessed is in the ith index of the answer
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:] #JY goes to index of the blank BEFORE where the correct letter is, replaces the '_' with the correct letter, keeps the rest blank
        
    for letters in blanks:
        print(letters, end='')
    print()

def getGuess(alreadyGuessed):
    """
    Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    """
    while True:
        print('Guess a letter.')
        guess = input() #JY makes the input of the user a string
        guess = guess.lower() #JY makes the input lowercase
        if len(guess) != 1: #JY if the input isnt a single letter
            print('Please enter a single letter')
        elif guess in alreadyGuessed: 
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz': #JY checks if the input is in the alphabet(valid letter)
            print('Please enter a LETTER')
        else:
            return guess #JY returns the input of the user IFF it proves to be a valid input

def playAgain():
    """
    This function returns True if the player wants to play again; otherwise, it returns False.
    """
    print('Do you want to play again? yes or no? (y/n)')
    return input().lower().startswith('y')

# print('H A N G M A N') #JY prints title of game

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    
    guess = getGuess(missedLetters + correctLetters) #JY keeps track of all guesses of the user(correct and incorrect) so there are no repeats
    
    if guess in secretWord:
        correctLetters = correctLetters + guess #JY adds all correct letters into the empty string to keep track
        
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is ' + secretWord + '! You have won!')
            gameIsDone = True #JY ends game
    else:
        missedLetters = missedLetters + guess #JY adds all incorrect guesses to keep track
        
        if len(missedLetters) == len(HANGMAN_PICS)-1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was ' + secretWord + '')
            gameIsDone = True
            
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(theme_chooser())
        else:
            break 