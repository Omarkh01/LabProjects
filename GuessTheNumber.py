def guessNumber():
  import random
  secretNumber = random.randint(1,100)
  while True:  
    prediction = int(input())
    if prediction == secretNumber:
      print("Congratulations!, You guessed the number.")
      break
    elif prediction > secretNumber:
      print("The number is too high")
    else:
      print("the number is too low")
    
guessNumber()
