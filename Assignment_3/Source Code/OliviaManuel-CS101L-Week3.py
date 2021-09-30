Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''
Olivia Manuel
CS101L
Week 3 Assignment
'''
print('Welcome to the Flarsheim Guesser!')
print('*********************************')
playing = 'Y'
while playing == 'Y':
  print('Please think of a number between and including 1 and 100.')

#ask remainder when divided by 3
  divby3 = int(input('What is the remainder when your number is divided by 3?: '))

#validate input for divby3
  while divby3 < 0 or divby3 > 2:
    print('The value entered must be 0 or greater and less than 3')
    divby3 = int(input('What is the remainder when your number is divided by 3?: '))

#ask remainder when divided by 5
  divby5 = int(input('What is the remainder when your number is divided by 5?: '))

#validate input for divby5
  while divby5 < 0 or divby3 > 4:
    print('The value entered must be 0 or greater and less than 5')
    divby5 = int(input('What is the remainder when your number is divided by 5?: '))

#ask remainder when divided by 7
  divby7 = int(input('What is the remainder when your number is divided by 7?: '))

#validate input for divby7
  while divby7 < 0 or divby7 > 6:
    print('The value entered must be 0 or greater and less than 7')
    divby7 = int(input('What is the remainder when your number is divided by 7?: '))

#iterate 1 through 100
  for x in range(1, 101):
    if ((x % 3 == divby3) and (x % 5 == divby5) and (x % 7 == divby7)):
      print('Your number is', x)
      print('Congratulations, I\'ve just blown your mind.')
  
  #play again?
  playing = input('Do you want to play again? Y to continue, N to quit: ')
  while playing != 'Y' and playing != 'N':
    playing = input('I don\'t understand. Do you want to play again? Y to continue, N to quit: ')