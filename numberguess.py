from random import randint as random
max=int(input("What would you like the largest number to be?: "))
number = random(0,max)
global leave
leave=0
global guesses
guesses=0
def choice():
  guess=int(input("guess: "))
  if guess!= number:
    guesses=+1
    if guess > number:
      print("Too big. Try again.")
    elif guess < number:
      print("Too small. Try again.")
    else:
      print("Invalid guess. Please try again.")
      guesses=-1
  else:
    print("Good job! The nubmer was",str(number),". You got it in",str(guesses),"guesses.")
    leave=1
while leave==0:
  choice()
