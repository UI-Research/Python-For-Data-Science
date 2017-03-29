print("Hello World!")

# Slide 11
hello_list = ["Hello", " ", "World", "!"]
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Indexing a list example:")
print("------------------------")
print("First element (Slide 16):")
print(hello_list[0])
print("First three elements (Slide 18):")
print(hello_list[0:3])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("For Loop Output (Slide 21):")
print("---------------------------")
for number in range(0, 5):
    print(number)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("For Each Loop Output (Slide 23):")
print("--------------------------------")
for number in [0,1,2,3,4]:
    print(number)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("While loop output (Slide 25):")
print("-----------------------------")
base = 5
num = 1
power = 3
n = 1
while n <= power:
    num = num * base
    n = n + 1
print(num)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("For Loop example with a list (Slide 27):")
print("----------------------------------------")
new_string = ""
for elt in hello_list:
    new_string = new_string + elt

print(new_string)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("While Loop example with a list (Slide 28):")
print("------------------------------------------")
new_string = ""
my_index = 0
while my_index < len(hello_list):
    new_string = new_string + hello_list[my_index]
    my_index += 1

print(new_string)

# Initialize hello_dictionary (Slide 42)
hello_dictionary = {"Hello": 0, " ": 1, "World": 2, "!": 3}
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Indexing a dictionary example (Slide 37):")
print("-----------------------------------------")
print(hello_dictionary["Hello"])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Exponent function containing a while loop (Slide 50):")
print("-----------------------------------------------------")
def exp(base, power):
    num = 1
    n = 1
    while n <= power:
        num = num * base
        n = n + 1
    print(num)

exp(5, 3)

