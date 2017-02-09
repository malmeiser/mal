print "Hanging out in Seattle! Mallory's First Python Game"

import time
import random

backpack = []

time.sleep(1)

name = raw_input("What's your name? ")

time.sleep(1)

#Introduction 

print "Hey " + name + "!"
print """
Welcome to Seattle! Let's figure out what we should do this weekend. 
If you ever want to hit the snooze button and head 
back to bed for the rest of the day, just type 'go back to bed'.
"""

time.sleep (10)

print """
You might find some items lying around Seattle, 
if you want to save anything for later go ahead and put it your backpack.
"""

items = raw_input ("Anything you want to pack before we start on our adventure?")
backpack.append(items)

print backpack

time.sleep (4)


def pikes_place():
    time.sleep(1)
    print "What should we eat first?"
    breakfast = raw_input("""
            donuts
            coffee
            lox bagel
            divide and conquer
            let's decide after coffee
            """)
    time.sleep(1)
    print "yum, good choice"
    time.sleep(1)
#Add go to library, add book to items

def waterfall_hike():
    time.sleep(1)
    print "Brrrr too cold for a hike!"

def pie_bar():
    pie_decision = raw_input("""What kind of pie should we get?
        peanut butter chocolate
        apple crumble
        """)
    if pie_decision == "peanut butter chocolate" or pie_decision == 'apple crumble':
        print "Seriously? Only one slice?"
        time.sleep (1)
        pie_bar()
    elif pie_decision == 'both':
        print "I knew we were friends for a reason"
    else:
        print "try again"
        time.sleep (1)
        pie_bar()
#Add pie for later to items

def out_of_city():
    print "still working on this activity"

def lazy_day():
    print "still working on this activity"
#add madlibs activity

def choose_activity():
    print "What do you want to do today?"
    activity = raw_input("""
    Hang out at Pikes Place
    Waterfall Hike
    PieBar
    Get out of the city
    Lazy day inside
    
    """).lower()
    if activity == 'hang out at pikes place':
        print pikes_place()
    elif activity == 'waterfall hike':
        print waterfall_hike()
    elif activity == 'pie bar':
        print pie_bar()
    elif activity == 'get out of the city':
        print out_of_city()
    elif activity == 'lazy day inside':
        print lazy_day()
    else:
        print "Hmmm I don't think thats on my list"
        choose_activity()

#Need to figure out how to do loop including exit
#Add transition between activities
#Dictionary with items you've picked up
choose_activity()
choose_activity()
choose_activity()
choose_activity()
choose_activity()
choose_activity()




