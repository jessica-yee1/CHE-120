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

    
def theme_chooser() :   #MT function responsible for determining which theme the user would like. Asks for an input, and checks to see the first character and matches it to a theme. Returns said theme and prints message.
    v=input("Choose a theme! You have a choice between animals, school, ocean and fruits: ")
    if  v.lower().startswith('a'): #MT checks to see what the user input starts with, then returns the corresponding list
        print("\nYou find yourself looking up at the sky through large trees, laying on damp soil. The sound of leaves rustling snaps you back to reality and you sit up. You look around in awe as you find yourself in a movie-like forest, realizing you don't remember coming here. The leaves rustle again and you turn to see a deer standing near you. \n\"Finally you're up! You've got to wake up!\" It says. \nYou stare in awe, rubbing your eyes to make sure you weren't hallucinating.  \n\"Did this deer just talk? I must be dreaming.\" You say to yourself. \n\"You're in a dream, but I can help you wake up. Guess the animal I'm thinking of and you'll wake up!\" It says.")
        return animals
    if v.lower().startswith('s') :
        print("\nYou open your eyes to a very familiar scene. Disoriented, you rub your eyes and begin to explore, concluding that you were indeed in an exact replica of your high school, although you don't remember exactly how you ended up here. As you try to piece together what had happened, you're interrupted by a familiar voice. Its your English teacher. \n\"You're dreaming, you've got to wake up.\" She says. \n\"Dreaming?\" You respond. \n\"Yes, but I can help you. You have to guess the school-related word I'm thinking of, but be smart about it. Otherwise, you might not wake up!\" She says.")
        return school
    if  v.lower().startswith('o') :
        print("\nYou open your eyes to a sandy, cold, desolate, beach. You look around and see some driftwood and kelp, with the beaches animals going about their buisness. A mysterious cloud hovers above your head it says\: \n \"Hello dear child, we must act quickly\" \nConfused you do not answer, but the clouds urgency is clear \n \"You're stuck within a dream, and you must find the hidden object trapping you here, quick guess letters to try and figure out the word. Each wrong guess will trap a part of you here.")
        return ocean
    if  v.lower().startswith('f'):
        print("\nOne hot summer day, as you sit on your porch refreshng yourself with a watermelon, you notice something odd about the melon. One of the seeds in your slices seems to be open like a tiny door. \nYou attempt to examine it peering closely, the cloeser you go the more confused you get. It seems like there is something inside your seed. You get so close that... You fall in!! You find yourself plummeting towards a multi-coloured floor, you scream as you descend but are cut off as you hit the supple slimey floor. You've landed in a grape! As you climb out, you notice a cloud hovering close by. He says \n\"Quickly we haven't much time, you must awake yourself, for you are stuck within a dream!\" \nAs your gaze wanders to the horizion you see you've been transported to some sort of fruit-land, with apples, pineapples and more surronding you on all sides. Banana snakes sliterthing on the floor, watermelon hippos relaxing in the water. \nThe cloud spoke again \"You must guess which fruit is holding you here quick! Otherwise you might not wake up\"")
        return fruits
    else :
        print("\nI have no idea what that means, but I think you'll like this one.")
        return animals
secretWord = getRandomWord(theme_chooser())#MT uses the output word bank from the function theme chooser, to find a word within the bank        
 
gameIsDone = False #JY all while loops "while True" will continue until gameIsDone=False

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)]) #JY displays the image of hangman relative to the number of incorrect letters guessed
    print()
    
    print('Missed letters:', end='') #JY displays letters guessed that aren't correct
    for letter in missedLetters:
        print(letter, end='') #JY prints each character in missedLetters separated by a space
    print()
    
    blanks = '_'*len(secretWord) #JY blanks representing the length of the word to be guessed
    
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
        print('Guess a letter. (Hint: The word is ' + str(len(secretWord)) + ' letters long!)')
        guess = input() #JY makes the input of the user a string
        guess = guess.lower() #JY makes the input lowercase
        if len(guess) != 1: #JY if the input isnt a single letter
            print('Please enter a single letter')
        elif guess in alreadyGuessed: 
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz': #JY checks if the input is in the alphabet(valid letter)
            print('Please guess a LETTER')
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
            print('Correct! The word was ' + secretWord + '!\nThe world begins to fade away to darkness. You open your eyes and find yourself tucked in your bed.\nIt really was all just a dream.\n')
            gameIsDone = True #JY ends game
    else:
        missedLetters = missedLetters + guess #JY adds all incorrect guesses to keep track
        
        if len(missedLetters) == len(HANGMAN_PICS)-1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was ' + secretWord + '.\nYou couldn\'t guess the word fast enough! You\'re stuck in the dream!\n')
            gameIsDone = True
            
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(theme_chooser())
        else:
            break 