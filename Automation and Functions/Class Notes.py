############################################################################
########################### Homework Example ###############################

# # # Phase 1 : Pseudocode
# The following is essentially what we want our program to do
# And it's a good starting point from which to build our program
""" # Three quotation marks is how you do a block comment in Python
for each letter in the list,
    # check to see if the letter is a consonant or a vowel.
    If it's a consonant:
        consonant_string += letter # this is a more concise version of consonant_string = consonant_string + letter
    Else:
        vowel_string += letter
"""

# # # Phase 2 : Initializations
full_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# Note that we could also use the following to get the above list:
import string # Tell Python I want to use the string module
full_list = string.ascii_uppercase[:10]

# # # Phase 2.5: try and except
try:
    # note: don't use "range"! it's a protected variable
    user_choice = int(input("Please enter a number between 1 and 10: "))
except:
    # oops! that wasn't right
    print("That was an incorrect value.")
    # We could use: 
    #   user_choice = int(input("Make sure to enter a number between 1 and 10: "))
    # but that will only capture a second error
    # Let's create a boolean
    keep_asking = True
    while keep_asking:
        try:
            user_choice = int(input("Make sure to enter a number between 1 and 10: "))
            keep_asking = False
        except:
            keep_asking = True

# Truncate the list
the_list = full_list[:user_choice]

############################################################################
############################## List Operations #############################

# Now let's look at some list operations:

first_list = [1,3,5,4,2]
print(first_list)

# Two options for printing
# 1: type what you want to print as a string
print("The first list is " + str(first_list))

# 2: Use the format operator
print("The first list is {}".format(first_list))

second_list = []
for number in range(1, 6):
    # Following is the same as second_list = second_list + [number]
    second_list += [number]
print("The second list from a for loop is {}".format(second_list))

# What if we want the first and second lists to have the same order?
# -> sort
first_list.sort()
print("The sorted first list is {}".format(second_list))

# We've been adding lists to lists, but we could also use append:
third_list = []
for number in range(1, 6):
    third_list.append(number)
print("The third list is {}".format(third_list))

# What if we want to change the number before we add it to the list?
squared_list = []
for number in range(1, 6):
    squared_list += [number**2]
print("The squared list is {}".format(squared_list))

###### List comprehensions
squared_listcomp = [number**2 for number in range(1, 6)]
print("And the squared list is now {}".format(squared_listcomp))

################### End of what we talked about in class ###################
############################################################################

##################### 2nd List Comprehension Example #######################

# Let's do an example where we have a list of lists, where each inner list
# is a person's name, and whether that person agreed to participate in your survey
# Now we want a smaller list that only includes the names of the participants

first_list = [['James', 'Yes'], ['John', 'No'], ['Janet', 'No'], ['Judy', 'Yes']]
participant_list = [x for x in first_list if x[1] == 'Yes']


############################# Lambda Functions #############################

# Now let's rewrite the above example, but with a lambda function:

first_list = [['James', 'Yes'], ['John', 'No'], ['Janet', 'No'], ['Judy', 'Yes']]
participant_list = list(filter(lambda x: x[1]=='Yes', first_list))

############################# File Input/Output #############################

# Now, let's open a file for writing
# And write "Hello World!"

# Writing to a file
with open('write2file.txt', 'w') as f:
    f.write("Hello World!")

# Next:
# Open a file for reading
# Read the line we wrote earlier

# Reading from a file
with open('write2file.txt', 'r') as f:
    file_contents = f.readline()

print(file_contents)

# What if we weren't sure how many lines were in our file?

# First, let's write multiple lines to our file:
num_lines = 6
with open('write2file.txt', 'w') as f:
    for i in range(0, num_lines):
        # Note the use of the newline operator \n
        # Otherwise, everything prints on the same line
        f.write("Hello World! \n")

# And now let's read them:
file_contents = ""
with open('write2file.txt', 'r') as f:
    for line in f:
        file_contents += line

print("Now the file contents are:\n{}\n".format(file_contents))
