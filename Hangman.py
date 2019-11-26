Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
def check(word,guesses,guess):
  status = ""
  matches = 0
  for letter in word:
    if letter in guesses:
      status += letter
    else:
      status += "*"
      
    if letter == guess:
      matches +=1
      
  if matches > 1:
    print("Yes! The word contains",matches,'"' + guess + '"'+'s')
  elif matches == 1:
    print("Yes! The word contains the letter '" + guess + '"')
  else:
    print("Sorry.The word does not contain the letter '" + guess + '"')
  return status      
def hangman():
  word = random.choice(["mountain","companion","book","television"])
  limit = 10
  guesses = []
  guessed = False
  print("The word contains",len(word),"letters.")
  #print("\n")
  while not guessed:
    text = "\nYou have left {} tries: ".format(limit)
    guess = input(text)
    limit -=1
    if guess in guesses:
      print("You already guessed " + guess +"")
    elif len(guess) == len(word):
      guesses.append(guess)
      if guess == word:
        guessed = True
      else:
        print("Sorry, that is incorrect.")
    elif len(guess) == 1:
      guesses.append(guess)
      result = check(word,guesses,guess)
      if result == word:
        guessed = True
      else:
        print(result)
    else:
      print("Invalid entry.")
    if limit == 0:
      print("\nYou could not find the word. The hidden word was", word)
      return

  print("\nThe hidden word is",word + "! You got it in",len(guesses),"tries.")
hangman()                  
    
