'''
Olivia Manuel
CS101L
Assignment 6

Summary: This program allows the user encode and decode a message using a caesar cipher. 
'''

#############################FUNCTIONS####################################

def menu():
  print('e = encode a message')
  print('d = decode the message')
  print('q = quit\n')

def caesar(plain_text, key):
    encrypted = ""
    for c in plain_text:
        if c.isupper(): #check if it's an uppercase character
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 26 + ord('A') # shift the current character by key positions
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower(): #check if its a lowecase character
            c_index = ord(c) - ord('a') # subtract the unicode of 'a' to get index in [0-25) range
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
    return encrypted

def uncaesar(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper(): 
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - key) % 26 + ord('A')  # shift the current character to left by key positions to get its original position
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower(): 
            c_index = ord(c) - ord('a') 
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
    return decrypted

#############################PROGRAM######################################

print('Welcome to Caesar Cipher\n')
playing = True
while playing: #continue/quit loop
  menu()
  option_choose = input('Please enter your choice: ')
  option_choose = option_choose.lower() #convert to lower

  if option_choose == 'e':
    string_encode = input('Enter the string to encode: ')
    
    while string_encode.isalpha() == False: #validate input is alphabet only
      string_encode = input('String must only contain letters. Enter the string to encode: ')
      
    amount_shift = input('Enter the amount to shift: ')
    print()
    while amount_shift.isdigit() == False: #validate input as digit
      amount_shift = input('Shift amount must be an integer greater than 0 and less than 26.\nEnter the amount to shift: ')
    while int(amount_shift) > 25 or int(amount_shift) < 0: #validate integer between 0 and 26
      amount_shift = input('Shift amount must be an integer greater than 0 and less than 26.\nEnter the amount to shift: ')

    print('Original Message:', string_encode, '\nEncoded Message:', caesar(string_encode, int(amount_shift)), '\n') #utilize caesar function

  elif option_choose == 'd':
    string_decode = input('Enter the string to decode: ')

    while string_decode.isalpha() == False: #validate input is alphabet only
      string_decode = input('String must only contain letters. Enter the string to decode: ')
    
    amount_unshift = input('Enter the amount to shift: ')
    print()
    while amount_unshift.isdigit() == False: #validate input as digit
      amount_unshift = input('Shift amount must be an integer greater than 0 and less than 26.\nEnter the amount to shift: ')
    while int(amount_unshift) > 25 or int(amount_unshift) < 0: #validate integer between 0 and 26
      amount_unshift = input('Shift amount must be an integer greater than 0 and less than 26.\nEnter the amount to shift: ')

    print('Original Message:', string_decode, '\nDecoded Message:', uncaesar(string_decode, int(amount_unshift)),'\n') #utilize uncaesar function

  elif option_choose == 'q': #quit loop
    playing = False
    print('Caesar Thanks You!')
  else:
    print('Invalid option') 