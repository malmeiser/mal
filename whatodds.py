import time
import random

#countdown function
def countdown(n):
    while n > 0:
        print (n)
        n = n-1
        time.sleep (1)

#what are the odds game 
#doesn't work if computer guesses correctly
def what_odds():
    
    print "The odds are 1 in..."
    
    odds = int(raw_input())
    if odds == 1:
        print "One in one! Ok I'm in."
    else:
        random_num  = random.randrange(1, odds)
        print "Wait for the countdown then type your number!"
    
        countdown(3)
        number = int(raw_input())
        print random_num
    
   
        if number in range (0, odds):
            if random_num == number:
                print "I win!"
            elif random_num != number:
                print "Gosh darn it"
        else:
            print "You can't pick that number!"
            what_odds()
            raw_input()
what_odds()
what_odds()
what_odds()
what_odds()