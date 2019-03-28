import random

print()
print()
print()
print()
print()
print('-------------------')
print('{0:^s}'.format('Welcome to Hangman!'))
print('-------------------')
print()
print()
print()
print()
print()

#Ask which version they want to play (pick the word themselves or generate a random word)
decision = input('Would you like to input a word or pick a random word from the dictionary? (myself/random): ')
while decision != 'myself' and decision != 'random':
   decision = input('Please answer with myself or random: ')

#Input word and make sure it is only lowercase letters or a space
#Ask for a word input if myself
#Find a random word if random   
if decision == 'myself':
   word = input('Input your word with only lowercase letters: ')
   for let in word:
      if let == ' ':
         continue
      elif ord(let) < ord('a') or ord(let) > ord('z'):
         word = input('Input your word with only lowercase letters: ')
         break
elif decision == 'random':
   fin = open('words.txt', 'r')
   all_words = fin.read()
   fin.close()
   all_words = all_words.split('\n')
   word = random.choice(all_words)
   while len(word) < 3:
      word = random.choice(all_words)


print('You will have letter 7 guesses.')
print('The following is what you are trying to guess!')
#Create output variable and print initial output
output = ''
for let in word:
   if let == ' ':
      print(' ',end = '')
      output += ' '
   else:
      print('_',end = '')
      output += '_'
print()
#Overall loop to go through each guess
guessed_letters = ''
i = 0
while i < 8:
   #Ask for a letter guess and amke sure it is a single letter that isn't repeated
   guess = input('Guess a letter: ')
   while len(guess) != 1 or ord(guess) < ord('a') or ord(guess) > ord('z'):
      guess = input('Please guess a single letter: ')
   while guess in guessed_letters:
      guess = input('You already guessed that letter! Guess another letter: ')
      if len(guess) != 1:
         guess = input('Please guess a single letter that you have not guessed before: ')
   #Count the # of letters from the guess that were in the word and add the index of each letter in the updates
   updates = []
   count = 0
   for let in range(len(word)):
      if word[let] == guess:
         count +=1
         updates.append(let)
   #Create and update the output progress
   output2 = []
   for x in output:
      output2.append(x)
   for y in updates:
      output2[y] = guess
   #Print if the guess is not in the word
   if count == 0:
      print('Oof. That letter is not in the word.')
      i += 1
   #Convert back to a string for the output
   output = ''
   for t in output2:
      output += t
   print()
   print(output)
   print()
   #Add guess to the guessed letters and print the guessed letters
   guessed_letters += guess + ' '
   print('Guessed Letters: {}'.format(guessed_letters))
   #Print the # of letters from the guess that were in the word
   if count > 0:
      print('Nice! You got {} letter(s).'.format(count))
   #Ask the user if they have a guess and check if their guess is correct
   guessask = input('Do you have a guess as to what the word is? (yes/no): ')
   while guessask != 'yes' and guessask != 'no':
      guessask = input('Please answer with a yes/no: ')
   if guessask == 'yes':
      tempguess = input('What do you think the word is?: ')
      if tempguess == word:
         print('Nice you got it!')
         break
      else:
         print('Darn! That is not correct.')
   #If they have 0 guesses left and don't guess the word, print that losing statement
   if 7-i == 0:
      print('Sorry! You lost. The word was {}. :( Try again!'.format(word))
      break
   #If they have any letter guesses left, print the # of guesses left
   elif 7-i > 0:
      print(('You have {} letter guesses left').format(7-i))







         




