########################################################################
##
## CS 101 Lab
## Program # Week 4-Functions
## Name: Olivia Manuel
## Email: owmdd7@mail.umkc.edu
##
## PROBLEM: SLOTS! SLOTS! SLOTS, SLOTS, SLOTS, SLOTS!
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed

import random

def play_again() -> bool:
    #Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes
    play = input('Do you want to play again? Yes or No: ')
    play = play.lower()
    while play != 'y' and play != 'yes' and play != 'n' and play != 'no': #handle any input not yes/no & y/n
      play = input('You must enter Yes or No to continue. Please try again: ')
    else:
      if play == 'y' or play == 'yes':
          play = True
      elif play == 'n' or play == 'no':
          play = False  
    return play
     
def get_wager(bank : int) -> int:
    #Asks the user for a wager chip amount. Continues to ask if the result is <= 0 or greater than the amount they have
    wager_amount = input('How many chips would you like to wager?: ')
    while wager_amount.isdigit() == False: #handle any non-integer input
      wager_amount = input('Invalid input. How many chips would you like to start with?: ')
    else:
      wager_amount = int(wager_amount)
    while wager_amount < 1: #handle input outside of acceptable range
       wager_amount = int(input('Wager amount too low, wager must be greater than 0 and less than or equal to your current chip total.'))
    while wager_amount > bank: #handle input outside of acceptable range
      wager_amount = int(input('Wager amount too high, wager must be greater than 0 and less than or equal to your current chip total.'))
    return wager_amount    

def get_slot_results() -> tuple:
    #Returns the result of the slot pull
    reelA = random.randint(1, 10)
    reelB = random.randint(1, 10)
    reelC = random.randint(1, 10)
    return reelA, reelB, reelC

def get_matches(reela, reelb, reelc) -> int:
    #Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike.
    matches = 0
    if reela == reelb and reelb == reelc:
      matches = 3
    elif reela == reelb or reelb == reelc:
      matches = 2
    return matches

def get_bank() -> int:
    #Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101
    chip_start = input('How many chips would you like to start with?: ')
    while chip_start.isdigit() == False:  #handle any non-integer input
      chip_start = input('Invalid input. How many chips would you like to start with?: ')
    else:
      chip_start = int(chip_start)
    while chip_start < 1: #handle input outside of acceptable range
      chip_start = int(input('Value too low, you may only choose 1 to 100 chips to start.'))
    while chip_start > 100: #handle input outside of acceptable range
      chip_start = int(input('Value too high, you may only choose 1 to 100 chips to start.'))
    return chip_start

def get_payout(wager, matches):
    #Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match
    matches = matches
    if matches == 3:
      wager = wager * 10
    elif matches == 2:
      wager = wager * 3
    elif matches == 0:
      wager = wager * -1
    return wager


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        original_chip_start = bank #store original starting chip value
        spins = 0
        chip_totals = [bank] #list for storing chip totals each spin (used later for greatest chip total)
        while bank > 0:  # Replace with condition for if they still have money.
            spins += 1
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            chip_totals.append(bank)
            greatest_chip_total = max(chip_totals)            
            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

        print('Wow, you suck at this.')   
        print("You lost all", original_chip_start, "in", spins, "spins")
        print("The most chips you had was", greatest_chip_total)
        if greatest_chip_total > 1000:
          print('But you did manage to break 1000 chips, so I\'m definitely inviting you to Vegas with me when I graduate.\n')
        playing = play_again()