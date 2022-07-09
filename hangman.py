import random

def chooseWord(word_list):
    word = random.choice(word_list)
    return word.upper()

def playHangman(word):
   word_line = "_" * len(word)
   tries = 9
   guessed = False
   guessed_words = []
   guessed_letters = []
   
   print("Welcome to Hangman!")
   print("The word is " + str(len(word)) + " letters long.")
   print(showHangman(tries))
   print(word_line)
   print("\n")
   while not guessed and tries > 0:
      guess = input("Guess a letter or a word: ").upper() 
      if len(guess) == 1 and guess.isalpha():    
            
         if guess in guessed_letters:
            print("You already guessed the letter", guess)
         elif guess not in word:
            print(guess, "is not in the word.")
            tries -= 1
            guessed_letters.append(guess)
         else:
            print("Good guess! " + guess + " is in the word!")
            
            for index, letter in enumerate(word):
               if letter == guess:
                  if not index == guess:
                     word_line = word_line[:index] + guess + word_line[index + 1:]
                  else:
                     word_line = word_line[:-1] + guess
            
      elif len(guess) == len(word) and guess.isalpha():
         if guess in guessed_words:
            print("You already guessed the word", guess)
         elif guess != word:
            print("That is not the word.")
            tries -= 1
            guessed_words.append(guess)
         else:
            print("Good guess! " + guess + " is the word!")
            guess = True
            word_line = word
            
      else:
         print("Not a valid guess.")
      print(showHangman(tries))
      print(word_line)
      print("\n")
      print("Guessed letters: " + str(guessed_letters))     
      print("Guessed words: " + str(guessed_words))
            
         
   
   return None
   

def showHangman(tries):
    hang_level = [
    ### 10 errors
    """ 
         ______ 
        |     |
        |     O
        |    \|/
        |     |
        |    / \\
        |    
     ___|___
    /       \\
    """, ## 9 errors
        """
         ______ 
        |     |
        |     O
        |    \|/
        |     |
        |    / 
        |    
     ___|___
    /       \\
    """, ## 8 errors
        """
         ______ 
        |     |
        |     O
        |    \|/
        |     |
        |    
        |    
     ___|___
    /       \\
    """, ## 7 errors
        """
         ______ 
        |     |
        |     O
        |    \|
        |     |
        |    
        |    
     ___|___
    /       \\
    """, ## 6 errors
    """
         ______ 
        |     |
        |     O
        |     |
        |     |
        |    
        |    
     ___|___
    /       \\
    """, ## 5 errors
        """
         ______ 
        |     |
        |     O
        |     
        |     
        |    
        |    
     ___|___
    /       \\
    """,  ## 4 errors
            """
         ______ 
        |     |
        |     
        |     
        |     
        |    
        |    
     ___|___
    /       \\
    """, ## 3 errors
            """
         ______ 
        |     
        |     
        |     
        |     
        |    
        |    
     ___|___
    /       \\
    """,  ## 2 errors
    """
         
        |     
        |     
        |     
        |     
        |    
        |    
     ___|___
    /       \\
    """,  ## 1 error   
        """
         
            
            
            
            
           
           
     _______
    /       \\
    """        
        
    ]
    
    return hang_level[tries]


wordList = ["Hangman"]

# print(chooseWord(wordList))
# print(showHangman(0))
playHangman(chooseWord(wordList))