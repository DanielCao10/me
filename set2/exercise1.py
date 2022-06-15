"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ["what", "does", "this", "line", "do", "?"]

# This will print the list into seperate strings.
for word in some_words:
    print(word) # It printed them into seperate strings.

#Same as above since the change in variable has no effect.
for x in some_words:
    print(x)

# It will print the list
print(some_words) #It printed the list

#len checks the amount of items in the list in this case three since the list has more than three items it will print the list.
if len(some_words) > 3:
    print("some_words contains more than 3 words") #It printed the list.

#Checks the OS
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) #It checked the OS


usefulFunction()
