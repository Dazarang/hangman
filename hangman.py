import random
from words import list_of_words

def randomWord():
    word = random.choice(list_of_words)
    return word.upper()

def playHangman(word):
   word_line = "_" * len(word)
   tries = 9
   guessed = False
   guessed_words = []
   guessed_letters = []
   
   print("The word is " + str(len(word)) + " letters long.")
   print(showHangman(tries))
   print(word_line)
   print("\n")
   while not guessed and tries > 0:
      guess = input("Guess a letter or a word: ").upper() 
      print("\n")
      if len(guess) == 1 and guess.isalpha():    
            
         if guess in guessed_letters:
            print("You already guessed the letter", guess)
         elif guess not in word:
            print(guess, "is not in the word.")
            tries -= 1
            guessed_letters.append(guess)
         else:
            print("Good guess! " + guess + " is in the word!")
            guessed_letters.append(guess)
            
            for index, letter in enumerate(word):
               if letter == guess:
                  if not index == guess:
                     word_line = word_line[:index] + guess + word_line[index + 1:]
                  else:
                     word_line = word_line[:-1] + guess
                     
            if "_" not in word_line:
               guessed = True
            
      elif len(guess) == len(word) and guess.isalpha():
         if guess in guessed_words:
            print("You already guessed the word", guess)
         elif guess != word:
            print("That is not the word.")
            tries -= 1
            guessed_words.append(guess)
         else:
            print("Good guess! " + guess + " is the word!")
            guessed = True
            word_line = word
            
      else:
         print("Not a valid guess.")
      print(showHangman(tries))
      print(word_line)
      print("\n")
      print("Guessed letters: " + str(guessed_letters))     
      print("Guessed words: " + str(guessed_words) + "\n")
            
   if guessed:
      print("Good job you guessed the word!")
   else:
      print("You got the man hanged, the word was: " + word)
      

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



def main():
      print("Welcome to Hangman. Let's play!")
      word = randomWord()
      playHangman(word)
      
      while input("Play again? (y/n): ").upper() == "Y":
         word = randomWord()
         playHangman(word)


if __name__ == "__main__":
   main()