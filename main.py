# Part 1: Hello, birthday month
# ask users to input their name and month
from datetime import datetime

name = input('what is your name? ')
birth_month = int(input('What is the number of the month you were born in? '))

currentMonth = datetime.now().month # this will get the number of the current month

# print a greeting to the user
print('Hello, ' + name + '! Nice to meet you.')

# print number of letters in the user's name
print(f'you have {len(name)} letters in your name')


# if the user input was equal to the current month, it will print:
if birth_month == currentMonth:
    print('Happy birthday month')
# if the int input does not equal the current month, it will print:
else:
    print('Not your birthday month')


# Part 2: List of classes
list_of_classes = []  # a list to hold the classes
# ask a user to enter name of the class
class_name = input("Enter name of class or enter to stop: ")
while class_name != "": # If the input is not empty, keep asking for class
    list_of_classes.append(class_name) # Add the class to the list
    class_name = input("Enter name of class or enter to stop: ")
for c in list_of_classes: # print all classes
    print(c)

# Part 3: camelCase
sentence = input("Enter a sentence to switch to camelCase: ") # Let the user enter a sentence to turn into camelCase
words_in_sentence_list = sentence.split() # Take every word in the sentence and turn it into a list
camelCaseSentence = "" # Create a new empty string to hold the camelCased sentence
camelCaseSentence = camelCaseSentence + words_in_sentence_list[0].lower() # First word is going to be all lower case
for word in words_in_sentence_list[1:]: # Capitalize the rest of the words in the sentence (after the first word)
    camelCaseSentence = camelCaseSentence + (word.capitalize())

print("Output : ", camelCaseSentence)  # printing the required resultant string
