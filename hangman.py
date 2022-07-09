import random

def chooseWord(word_list):
    word = random.choice(word_list)
    return word
  
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


wordList = ["Hangman", "HangedMan"]

print(chooseWord(wordList))