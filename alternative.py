# # # Alternate case/word.

# User input a given string to make the alternative charater or word upper and lower case

user_input = input("Please enter a string: ")  # User input


# # # Pseudo code for applying alternate case on a string

"""
define the alternate case conversion to be applied on a string 

        for the input string, you iterate each character

             if the character is even, the case is converted to a upper case

             else if the character is odd, the case is converted to lower case 
             
        return the alternate string

Apply the alternate case converstion to the inputted string 

Display the results 

"""

# # # Code for alternate case on a string

def alternate_conversion(input_str):    # Defining alternate case conversion
    alternate = ""
    for i in range(len(input_str)):     
        if i % 2 == 0:                           # For an even character, output a upper case
            alternate += input_str[i].upper()
        else:                                    # Else for a an odd character. output a lower case
            alternate += input_str[i].lower()     
    return alternate


alternate_string = alternate_conversion(user_input)  # Apply alternate case conversion

print("The alternate case on the inputted string is ",alternate_string ) # Displaying the output for alternate charater case 

# # #  Pseudo code for alternate word 

"""
Split the string into seperate words 

for a given input string, the words are iterated  

    if the word is even, output a upper case word 

    else if the word is odd, output a lower case word

    if the iteration is less than the amount of words < 1, ouput " " (This allows the string to be outpuuted with spaces between the words)

return the output word 

apply the alternate words case conversion on the inputted string

Display the output string

"""

# # # Code for making the alternative word upper and lower case 

def alternate_word_case_conversion(input_str):

    words = input_str.split()  # Split the input string into a list of words

    alternate_word = ""

    for i in range(len(words)):
        if i % 2 == 0:
            alternate_word += words[i].upper()
        else:
            alternate_word += words[i].lower()

        if i < len(words) - 1:  # Adds a space in the output sring 
            alternate_word += " "

    return alternate_word


alternate_word_string = alternate_word_case_conversion(user_input)   # Apply alternate word case conversion

print("The alternate word case is,",alternate_word_string) # Displaying  the output of alternate word case



