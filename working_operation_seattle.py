
import time
import random

backpack = []
seattle_list = ["Grab food at Pike's Place","Head to Yoga", "Visit the Seattle Library","Go for a hike"]

#Introduction
print "Hanging out in Seattle! Mallory's First Python Game"

raw_input()

name = raw_input("What's your name? ")

print ""
print "Hey " + name + "!" " Welcome to Seattle."
print "I made a list of things for us to do today."
print "Let's start crossing activities off!"
print "If want to exit the game just type 'time to go home'." 
print ""

raw_input()

print "You might find some items lying around Seattle."
print "If you want to save anything for later, put it your backpack."

raw_input()

#add an item to your backpack
def add_to_backpack(item):
    item.lower()
    if item not in backpack:
        backpack.append(item)
        print "Added!"
        print "Here's what you have in your backpack:"
        print backpack
    else:
        print "You already have that!"
    raw_input()

#countdown function
def countdown(n):
    while n > 0:
        print (n)
        n = n-1
        time.sleep (1)

#what are the odds game 
#doesn't work if computer guesses correctly
def what_odds():
    
    print ""
    print "The odds are 1 in..."
    
    odds = int(raw_input())
    random_num  = random.randrange(1, odds)
    
    print "Wait for the countdown then type your number!"
    
    countdown(3)
    number = int(raw_input())
    print random_num
    
    if random_num == number:
        print "I win!"
    elif random_num != number:
        print "Gosh darn it"
    raw_input()

#pikes place activity description
def pikes_place():
    print ""
    print "Where should we get food?"
    print "mini donuts at Daily Dozen Donuts"
    print "coffee and macaroons at Le Panier"
    print "cheddar and garlic roll piroshky at Piroshky Piroshky"
    print "the lox bagel cart"
    print ""
    
    breakfast = raw_input()
    
    print "Yes! I was craving " + breakfast + " too!"

    raw_input()
   
    print "What are the odds you'll buy us Hello Robin later?"
    print ""
    
    what_odds()
    
    print "Before we go, let's pick up a souvenir!"
    
    souvenir = raw_input("What should we get from Pike's Place? ")
    add_to_backpack(souvenir)
    
    print "Ok, what's next!"
    
    main()

#yoga activity description
def yoga():
    time.sleep(1)
    print ""
    print "What yoga class do you want to take?"
    print "C1 (easier)"
    print "C2 (harder)"
    yoga_class = raw_input().lower()
    if yoga_class == "c1":
        print "Oooommmmmm"
        print "Here is your C1 yoga flow"
        print "(press any button when finished)"
        raw_input()
        print "Start in child's pose"
        print "Three legged dog"
        print "Proud pigeon"
        print "Sleeping pigeon"
        print "Repeat on other side"
        print "Bonus: Flip your dog!"
        raw_input()
    elif yoga_class == "c2":
        print "Oooommmm:"
        print "Here is your C2 yoga flow"
        print "(press any button when finished)"
        raw_input()
        print "Start in mountain pose"
        print "Rag doll pose"
        print "Half way lift, back to mountain pose"
        print "One legged tadasana"
        print "Grow your branches"
        print "Repeat on othe side"
        print "Bonus: Dancer's pose!"
        raw_input()
    print "I feel great! Let's buy a matt so we can practice more at home."
    print "What color matt should we get?"
    color = raw_input()
    matt = color + " matt"
    add_to_backpack(matt)
    print "Alright I'm all yogied out."
    main()

#getting a library card from seattle library
def library_card():
    print ""
    name = raw_input("What is your name? ")
    address = raw_input("What is your address? ")
    birthday = raw_input("What's your birth date? ")
    print ""
    print "  ----------------------------------    "
    print " |      SEATTLE LIBRARY CARD        |   "
    print " |                                  |   "
    print "          " + name + "                  "
    print "         " + address + "                "
    print "          " + birthday + "              "
    print " |                                  |   "
    print " |                                  |   "
    print "  ----------------------------------    "

#library activity description
def library():
    print ""
    print "Welcome to the Seattle library!"
    print "First, you need to register for a library card"
    library_card()
    book = raw_input ("What book do you want to borrow today? ")
    add_to_backpack(book)
    print ""
    print "Ok we have our library book, now what?"
    main()

def hike():
    print "still working on this activity"
    main()

#choose activity in main function
def choose_activity():
    print seattle_list
    activity = raw_input('What should we do today? ').lower()
    return activity 

def main():
    while seattle_list > 0:
        activity = choose_activity()
        if activity == 'grab food at pikes place':
            seattle_list.remove("Grab food at Pike's Place")
            print ""
            print pikes_place()
        elif activity == 'head to yoga':
            seattle_list.remove("Head to Yoga")
            print ""
            print yoga()
        elif activity == 'visit the seattle library':
            seattle_list.remove("Visit the Seattle Library")
            print ""
            print library()
        elif activity == 'go for a hike':
            seattle_list.remove("Go for a hike")
            print ""
            print hike()
        elif activity == 'time to go home':
            break
    print "You've complete the list! Successful day in Seattle"
        break
main()
